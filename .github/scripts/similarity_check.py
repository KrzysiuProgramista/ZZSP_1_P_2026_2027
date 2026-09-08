#!/usr/bin/env python3
"""Compare pupils' Python submissions against each other.

Standard library only - nothing to install.

Layout it expects, one folder per pupil at the top level:

    STUDENT_NAME/<assignment>/file.py

Metrics, in the order they matter:

  jaccard  overlap of 25-character shingles of the normalised source.
           THE discriminating signal. Calibrated on 572 same-task pairs of real
           first-year homework: median 0.18, p90 0.63.
  text     difflib on the normalised source (comments and docstrings stripped).
           Noisier: median 0.77 on the same corpus, so it only corroborates.
  struct   difflib on an AST with every identifier renamed. Reported for
           information and NEVER used to flag: on beginner exercises its median
           is 0.84 and its p90 is 1.00, because `for i in range(10)` has the
           same shape whoever writes it.

The length gate matters more than the threshold. Below --min-chars of normalised
source, two correct answers to a tightly specified exercise are simply identical,
so anything shorter is skipped rather than compared.

The gate is 100 by design choice, which is deliberately permissive: on the
calibration corpus, pairs under 150 normalised characters had a k-gram median of
0.03 but a 90th percentile of 0.69, so at this gate the check will surface real
convergence on trivial exercises. Treat a flag on a short file as "look at it",
not as a finding. Raise the gate to 300 to suppress that class of noise.

`normalise()` is adapted from PLAGIARISM_CHECKER/NEW_VERSION/plagiarism_checker.py,
with autojunk disabled and the fingerprints computed once per file instead of once
per pair.
"""

from __future__ import annotations

import argparse
import ast
import io
import json
import os
import re
import subprocess
import sys
import tokenize
from dataclasses import dataclass, field
from difflib import SequenceMatcher
from itertools import combinations
from pathlib import Path

REPORT_NAME = "SIMILARITY_REPORT.md"
SUMMARY_JSON = ".similarity/report.json"
SHINGLE = 25

# Folders at the top level that are not pupils
NOT_PUPILS = {".git", ".github", ".similarity", "node_modules", "__pycache__"}


# --------------------------------------------------------------- normalising
def normalise(source: str) -> str:
    """Strip comments and docstrings, collapse literals, keep token order.

    Adapted from NEW_VERSION/plagiarism_checker.py.
    """
    try:
        parts: list[str] = []
        for tok in tokenize.generate_tokens(io.StringIO(source).readline):
            if tok.type in (tokenize.COMMENT, tokenize.NEWLINE,
                            tokenize.NL, tokenize.ENCODING, tokenize.INDENT,
                            tokenize.DEDENT):
                continue
            parts.append("STR" if tok.type == tokenize.STRING else tok.string)
        return " ".join(p for p in parts if p.strip())
    except (tokenize.TokenError, IndentationError, SyntaxError):
        source = re.sub(r"#[^\n]*", "", source)
        return re.sub(r"\s+", " ", source).strip()


class _AstNormaliser(ast.NodeTransformer):
    """Rename every identifier so only the structure survives."""

    def __init__(self) -> None:
        self._map: dict[str, str] = {}

    def _ph(self, name: str) -> str:
        return self._map.setdefault(name, f"V{len(self._map)}")

    def visit_Name(self, n):  # noqa: N802
        n.id = self._ph(n.id)
        return n

    def visit_arg(self, n):
        n.arg = self._ph(n.arg)
        n.annotation = None
        return n

    def visit_FunctionDef(self, n):  # noqa: N802
        n.name = self._ph(n.name)
        self.generic_visit(n)
        return n

    visit_AsyncFunctionDef = visit_FunctionDef

    def visit_ClassDef(self, n):  # noqa: N802
        n.name = self._ph(n.name)
        self.generic_visit(n)
        return n

    def visit_Constant(self, n):  # noqa: N802
        n.value = type(n.value).__name__
        return n


def ast_fingerprint(source: str) -> str | None:
    try:
        return ast.dump(_AstNormaliser().visit(ast.parse(source)))
    except (SyntaxError, ValueError, RecursionError):
        return None


def shingles(normalised: str, k: int = SHINGLE) -> set[str]:
    dense = re.sub(r"\s+", "", normalised)
    if len(dense) < k:
        return set()
    return {dense[i:i + k] for i in range(len(dense) - k + 1)}


# autojunk would treat common characters as noise on long strings, which
# silently distorts the ratio on source code.
def _ratio(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b, autojunk=False).ratio()


def jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


# --------------------------------------------------------------- model
@dataclass
class Sub:
    path: str                 # repo-relative
    pupil: str
    assignment: str
    source: str
    norm: str = field(repr=False, default="")
    grams: set[str] = field(repr=False, default_factory=set)
    fp: str | None = field(repr=False, default=None)
    added: str | None = None  # ISO date the file first appeared in git
    order: int | None = None  # position of that commit in history

    @property
    def size(self) -> int:
        return len(self.norm)

    @property
    def name(self) -> str:
        return os.path.basename(self.path)


def git_added_dates(repo: Path) -> dict[str, tuple[str, int]]:
    """Per path: (date, position) of the commit that first added it.

    The position is what makes the ordering strict. Author dates are only
    second-resolution and two pupils can easily share one, while several files
    added by a single commit share a date *legitimately* - in that case neither
    is "later" and the caller must not guess.
    """
    try:
        out = subprocess.run(
            ["git", "log", "--all", "--reverse", "--date-order",
             "--pretty=format:\x01%aI", "--name-only"],
            cwd=repo, capture_output=True, text=True, timeout=120, check=False,
        )
    except (OSError, subprocess.SubprocessError):
        return {}
    if out.returncode != 0:
        return {}
    dates: dict[str, tuple[str, int]] = {}
    when, position = None, -1
    for line in out.stdout.splitlines():
        if line.startswith("\x01"):
            when = line[1:]
            position += 1
        elif line.strip() and when:
            dates.setdefault(line.strip(), (when, position))
    return dates


def collect(repo: Path) -> list[Sub]:
    subs: list[Sub] = []
    dates = git_added_dates(repo)
    for pupil_dir in sorted(p for p in repo.iterdir() if p.is_dir()):
        if pupil_dir.name in NOT_PUPILS or pupil_dir.name.startswith("."):
            continue
        for py in sorted(pupil_dir.rglob("*.py")):
            rel = py.relative_to(repo).as_posix()
            try:
                src = py.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            parts = rel.split("/")
            assignment = parts[1] if len(parts) > 2 else "(root)"
            added, order = dates.get(rel, (None, None))
            s = Sub(path=rel, pupil=pupil_dir.name, assignment=assignment,
                    source=src, added=added, order=order)
            s.norm = normalise(src)
            s.grams = shingles(s.norm)
            s.fp = ast_fingerprint(src)
            subs.append(s)
    return subs


@dataclass
class Hit:
    a: Sub
    b: Sub
    jac: float
    text: float
    struct: float | None

    @property
    def ordered(self) -> tuple[Sub, Sub] | None:
        """(earlier, later), or None when the two cannot be ordered.

        None means they arrived in the same commit, or history is unavailable.
        There is genuinely no later submitter then, so both are reported.
        """
        if self.a.order is None or self.b.order is None:
            return None
        if self.a.order == self.b.order:
            return None
        return (self.a, self.b) if self.a.order < self.b.order else (self.b, self.a)

    @property
    def blamed(self) -> list[Sub]:
        """Whose folder gets the report: the later one, or both if tied."""
        o = self.ordered
        return [o[1]] if o else [self.a, self.b]


def compare(subs: list[Sub], min_chars: int, threshold: float,
            only_pupils: set[str] | None,
            notice_top: int = 10) -> tuple[list[Hit], list[Hit], list[Sub]]:
    """Return (flagged, notices, skipped).

    `flagged` crosses the threshold and earns a report file in the pupil's folder.
    `notices` are the closest pairs BELOW it. They exist because "flagged nothing"
    and "nothing resembles anything" are different statements, and on a task whose
    specification dictates every class and method name the second is never true.
    Notices are shown to the teacher and never written into a pupil's folder.
    """
    eligible = [s for s in subs if s.size >= min_chars]
    skipped = [s for s in subs if s.size < min_chars]
    scored: list[Hit] = []
    for a, b in combinations(eligible, 2):
        if a.pupil == b.pupil:
            continue
        if only_pupils and a.pupil not in only_pupils and b.pupil not in only_pupils:
            continue
        struct = _ratio(a.fp, b.fp) if (a.fp and b.fp) else None
        scored.append(Hit(a, b, jaccard(a.grams, b.grams), _ratio(a.norm, b.norm), struct))
    scored.sort(key=lambda h: -h.jac)
    hits = [h for h in scored if h.jac >= threshold]
    notices = [h for h in scored if h.jac < threshold][:notice_top]
    return hits, notices, skipped


# --------------------------------------------------------------- output
def pupil_report(pupil: str, hits: list[Hit], threshold: float,
                 name_others: bool) -> str:
    lines = [
        "# Similarity report", "",
        "This file was written automatically by the `similarity` GitHub Action.",
        "It is **not** a decision or an accusation - it flags work for your",
        "teacher to look at, and your teacher decides what it means.", "",
        f"Pupil folder: `{pupil}`", "",
        "| your file | similarity | length |",
        "|---|---|---|",
    ]
    same_push = False
    for h in sorted(hits, key=lambda h: -h.jac):
        mine = h.a if h.a.pupil == pupil else h.b
        theirs = h.b if mine is h.a else h.a
        if h.ordered is None:
            same_push = True
        other = f" (`{theirs.pupil}`)" if name_others else ""
        lines.append(f"| `{mine.path}` | **{h.jac:.0%}**{other} | {mine.size} chars |")
    lines += [
        "",
        f"Flagged because the overlap is at or above {threshold:.0%} on a "
        "substantial amount of code.", "",
        *(["Both submissions arrived in the same commit, so nobody was 'first'. ",
           "This same note is in the other folder too - it is not pointing at you.",
           ""] if same_push else []),
        "### What to do",
        "",
        "- If you wrote this yourself, say so - that is a perfectly good answer,",
        "  and on short exercises two correct solutions really can look alike.",
        "- If you worked together with someone, say that too. Working together is",
        "  allowed on plenty of tasks; not saying so is the problem.",
        "- If you copied it, rewrite it in your own way and push again. This file",
        "  disappears by itself once the overlap drops.",
        "",
        "---",
        "_Delete nothing. This file is regenerated on every push._",
    ]
    return "\n".join(lines) + "\n"


def job_summary(hits: list[Hit], notices: list[Hit], skipped: list[Sub],
                subs: list[Sub], min_chars: int, threshold: float) -> str:
    out = ["## Similarity check", ""]
    pupils = sorted({s.pupil for s in subs})
    out.append(f"{len(subs)} Python file(s) from {len(pupils)} pupil folder(s). "
               f"Gate: {min_chars} normalised chars. Threshold: {threshold:.0%} "
               f"k-gram overlap.")
    out.append("")
    if hits:
        out += [f"### {len(hits)} pair(s) flagged", "",
                "| pushed later | resembles | k-gram | text | struct | chars |",
                "|---|---|---|---|---|---|"]
        for h in hits:
            st = f"{h.struct:.0%}" if h.struct is not None else "n/a"
            o = h.ordered
            if o:
                first, second = o
                left = f"`{second.pupil}` <br>`{second.path}`"
                right = f"`{first.pupil}` <br>`{first.path}`"
            else:
                left = f"`{h.a.pupil}` + `{h.b.pupil}` <br>_same commit_"
                right = f"`{h.a.path}` <br>`{h.b.path}`"
            out.append(f"| {left} | {right} | **{h.jac:.0%}** | {h.text:.0%} "
                       f"| {st} | {min(h.a.size, h.b.size)} |")
        out += ["", "The report file goes into the later submitter's folder, or into "
                "both when the two arrived in the same commit.", ""]
    else:
        out += ["### Nothing flagged", ""]
    if notices:
        out += ["### Closest pairs below the threshold", "",
                "Shown so you can see the shape of the cohort. No report file is "
                "written for these and no pupil is told.", "",
                "| pair | k-gram | text | struct | chars |", "|---|---|---|---|---|"]
        for h in notices:
            st = f"{h.struct:.0%}" if h.struct is not None else "n/a"
            out.append(f"| `{h.a.pupil}` / `{h.b.pupil}` | {h.jac:.0%} | {h.text:.0%} "
                       f"| {st} | {min(h.a.size, h.b.size)} |")
        out += ["", "On a task whose specification dictates the class and method names, "
                "expect these to be high. That is the task, not the pupils.", ""]

    if skipped:
        out += [f"<details><summary>{len(skipped)} file(s) too short to judge "
                f"(under {min_chars} normalised chars)</summary>", ""]
        for s in sorted(skipped, key=lambda s: s.path):
            out.append(f"- `{s.path}` - {s.size} chars")
        out += ["", "On a tightly specified short exercise, two correct answers are "
                "often character-for-character alike. Comparing them says nothing.",
                "</details>", ""]
    out += ["", "_`struct` is AST similarity with identifiers renamed. It is shown "
            "for information only and never used to flag: on beginner exercises its "
            "median is 84% and its 90th percentile is 100%._"]
    return "\n".join(out) + "\n"


def _side(s: Sub) -> dict:
    return {"pupil": s.pupil, "path": s.path,
            "assignment": s.assignment, "added": s.added}


def _findings_unchanged(target: Path, payload: dict) -> bool:
    """True when the existing file says the same thing, ignoring `generated`."""
    if not target.exists():
        return False
    try:
        existing = json.loads(target.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False
    return {k: v for k, v in existing.items() if k != "generated"} == \
           {k: v for k, v in payload.items() if k != "generated"}


# --------------------------------------------------------------- main
def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", default=".", type=Path)
    ap.add_argument("--min-chars", type=int, default=100,
                    help="skip files with less normalised source than this (default 100)")
    ap.add_argument("--threshold", type=float, default=0.60,
                    help="k-gram overlap at which to flag, 0-1 (default 0.60)")
    ap.add_argument("--only", default="",
                    help="comma-separated pupil folders; restrict pairs to these")
    ap.add_argument("--write-reports", action="store_true",
                    help=f"write {REPORT_NAME} into flagged pupils' folders "
                         f"and remove stale ones")
    ap.add_argument("--name-others", action="store_true",
                    help="name the other pupil inside the committed report "
                         "(off by default; names always appear in the job summary)")
    ap.add_argument("--notice-top", type=int, default=10,
                    help="how many closest below-threshold pairs to report as "
                         "notices, for the teacher only (default 10; 0 disables)")
    ap.add_argument("--annotate", action="store_true",
                    help="emit ::warning:: workflow commands for flagged files")
    ap.add_argument("--summary", type=Path, help="write a markdown summary here")
    ap.add_argument("--json", dest="json_out", type=Path,
                    help=f"write machine-readable results here (default {SUMMARY_JSON})")
    args = ap.parse_args(argv)

    repo: Path = args.repo.resolve()
    if not repo.is_dir():
        print(f"not a directory: {repo}", file=sys.stderr)
        return 2

    only = {p.strip() for p in args.only.split(",") if p.strip()} or None
    subs = collect(repo)
    hits, notices, skipped = compare(subs, args.min_chars, args.threshold,
                                     only, args.notice_top)

    print(f"{len(subs)} file(s), {len(subs) - len(skipped)} above the "
          f"{args.min_chars}-char gate, {len(hits)} pair(s) flagged", file=sys.stderr)

    by_pupil: dict[str, list[Hit]] = {}
    for h in hits:
        for sub in h.blamed:
            by_pupil.setdefault(sub.pupil, []).append(h)

    # ---- report files ----------------------------------------------------
    if args.write_reports:
        wanted = {}
        for pupil, ph in by_pupil.items():
            for h in ph:
                sub = next(s for s in h.blamed if s.pupil == pupil)
                folder = repo / pupil / sub.assignment
                if not folder.is_dir():
                    folder = repo / pupil
                wanted.setdefault(folder, []).append(h)
        for folder, ph in wanted.items():
            target = folder / REPORT_NAME
            target.write_text(pupil_report(folder.relative_to(repo).parts[0],
                                           ph, args.threshold, args.name_others),
                              encoding="utf-8")
            print(f"wrote {target.relative_to(repo)}", file=sys.stderr)
        # remove reports that no longer apply
        for stale in repo.rglob(REPORT_NAME):
            if stale.parent not in wanted and ".git" not in stale.parts:
                stale.unlink()
                print(f"removed stale {stale.relative_to(repo)}", file=sys.stderr)

    # ---- machine-readable ------------------------------------------------
    payload = {
        "generated": os.environ.get("GITHUB_SHA", "local"),
        "minChars": args.min_chars,
        "threshold": args.threshold,
        "fileCount": len(subs),
        "pupilCount": len({s.pupil for s in subs}),
        "skipped": [{"path": s.path, "pupil": s.pupil, "chars": s.size}
                    for s in skipped],
        "flagged": [{
            "sameCommit": h.ordered is None,
            "later": _side(h.ordered[1] if h.ordered else h.b),
            "earlier": _side(h.ordered[0] if h.ordered else h.a),
            "jaccard": round(h.jac, 4), "text": round(h.text, 4),
            "struct": round(h.struct, 4) if h.struct is not None else None,
            "chars": min(h.a.size, h.b.size),
        } for h in hits],
        "notices": [{
            "pupils": sorted([h.a.pupil, h.b.pupil]),
            "paths": [h.a.path, h.b.path],
            "jaccard": round(h.jac, 4), "text": round(h.text, 4),
            "struct": round(h.struct, 4) if h.struct is not None else None,
            "chars": min(h.a.size, h.b.size),
        } for h in notices],
    }
    out_json = args.json_out or (repo / SUMMARY_JSON)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    # Only rewrite when the FINDINGS changed. `generated` alone would otherwise
    # differ on every push, so the bot would commit once per pupil per push.
    if _findings_unchanged(out_json, payload):
        print(f"{out_json.name}: findings unchanged, left alone", file=sys.stderr)
    else:
        out_json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    if args.annotate:
        for h in hits:
            for sub in h.blamed:
                print(f"::warning file={sub.path}::{h.jac:.0%} overlap with "
                      f"another submission in this class. See {REPORT_NAME} in "
                      f"your folder. Your teacher will review it.")

    if args.summary:
        args.summary.write_text(
            job_summary(hits, notices, skipped, subs, args.min_chars, args.threshold),
            encoding="utf-8")

    return 0   # never fail the build


if __name__ == "__main__":
    raise SystemExit(main())
