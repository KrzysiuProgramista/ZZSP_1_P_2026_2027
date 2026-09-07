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

    @property
    def size(self) -> int:
        return len(self.norm)

    @property
    def name(self) -> str:
        return os.path.basename(self.path)


def git_added_dates(repo: Path) -> dict[str, str]:
    """Earliest commit date per path, from one pass over the history."""
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
    dates: dict[str, str] = {}
    when = None
    for line in out.stdout.splitlines():
        if line.startswith("\x01"):
            when = line[1:]
        elif line.strip() and when:
            dates.setdefault(line.strip(), when)
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
            s = Sub(path=rel, pupil=pupil_dir.name, assignment=assignment,
                    source=src, added=dates.get(rel))
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
    def later(self) -> Sub:
        """Whichever of the two appeared in git second."""
        if self.a.added and self.b.added:
            return self.b if self.b.added >= self.a.added else self.a
        return self.b

    @property
    def earlier(self) -> Sub:
        return self.a if self.later is self.b else self.b


def compare(subs: list[Sub], min_chars: int, threshold: float,
            only_pupils: set[str] | None) -> tuple[list[Hit], list[Sub]]:
    eligible = [s for s in subs if s.size >= min_chars]
    skipped = [s for s in subs if s.size < min_chars]
    hits: list[Hit] = []
    for a, b in combinations(eligible, 2):
        if a.pupil == b.pupil:
            continue
        if only_pupils and a.pupil not in only_pupils and b.pupil not in only_pupils:
            continue
        j = jaccard(a.grams, b.grams)
        if j < threshold:
            continue
        struct = _ratio(a.fp, b.fp) if (a.fp and b.fp) else None
        hits.append(Hit(a, b, j, _ratio(a.norm, b.norm), struct))
    hits.sort(key=lambda h: -h.jac)
    return hits, skipped


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
    for h in sorted(hits, key=lambda h: -h.jac):
        mine = h.later if h.later.pupil == pupil else h.earlier
        other = f" (`{h.earlier.pupil}`)" if name_others and mine is h.later else ""
        lines.append(f"| `{mine.path}` | **{h.jac:.0%}**{other} | {mine.size} chars |")
    lines += [
        "",
        f"Flagged because the overlap is at or above {threshold:.0%} on a "
        "substantial amount of code.", "",
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


def job_summary(hits: list[Hit], skipped: list[Sub], subs: list[Sub],
                min_chars: int, threshold: float) -> str:
    out = ["## Similarity check", ""]
    pupils = sorted({s.pupil for s in subs})
    out.append(f"{len(subs)} Python file(s) from {len(pupils)} pupil folder(s). "
               f"Gate: {min_chars} normalised chars. Threshold: {threshold:.0%} "
               f"k-gram overlap.")
    out.append("")
    if hits:
        out += [f"### {len(hits)} pair(s) flagged", "",
                "| later | earlier | k-gram | text | struct | chars |",
                "|---|---|---|---|---|---|"]
        for h in hits:
            st = f"{h.struct:.0%}" if h.struct is not None else "n/a"
            out.append(f"| `{h.later.pupil}` <br>`{h.later.path}` "
                       f"| `{h.earlier.pupil}` <br>`{h.earlier.path}` "
                       f"| **{h.jac:.0%}** | {h.text:.0%} | {st} "
                       f"| {min(h.a.size, h.b.size)} |")
        out += ["", "A report file was written into the *later* submitter's folder.", ""]
    else:
        out += ["### Nothing flagged", ""]
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


# --------------------------------------------------------------- main
def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", default=".", type=Path)
    ap.add_argument("--min-chars", type=int, default=300,
                    help="skip files with less normalised source than this (default 300)")
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
    hits, skipped = compare(subs, args.min_chars, args.threshold, only)

    print(f"{len(subs)} file(s), {len(subs) - len(skipped)} above the "
          f"{args.min_chars}-char gate, {len(hits)} pair(s) flagged", file=sys.stderr)

    by_pupil: dict[str, list[Hit]] = {}
    for h in hits:
        by_pupil.setdefault(h.later.pupil, []).append(h)

    # ---- report files ----------------------------------------------------
    if args.write_reports:
        wanted = {}
        for pupil, ph in by_pupil.items():
            for h in ph:
                folder = repo / pupil / h.later.assignment
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
            "later": {"pupil": h.later.pupil, "path": h.later.path,
                      "assignment": h.later.assignment, "added": h.later.added},
            "earlier": {"pupil": h.earlier.pupil, "path": h.earlier.path,
                        "assignment": h.earlier.assignment, "added": h.earlier.added},
            "jaccard": round(h.jac, 4), "text": round(h.text, 4),
            "struct": round(h.struct, 4) if h.struct is not None else None,
            "chars": min(h.a.size, h.b.size),
        } for h in hits],
    }
    out_json = args.json_out or (repo / SUMMARY_JSON)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    if args.annotate:
        for h in hits:
            print(f"::warning file={h.later.path}::{h.jac:.0%} overlap with "
                  f"another submission in this class. See {REPORT_NAME} in your "
                  f"folder. Your teacher will review it.")

    if args.summary:
        args.summary.write_text(
            job_summary(hits, skipped, subs, args.min_chars, args.threshold),
            encoding="utf-8")

    return 0   # never fail the build


if __name__ == "__main__":
    raise SystemExit(main())
