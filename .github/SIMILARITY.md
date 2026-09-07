# The similarity check

Every time anyone pushes, a GitHub Action compares the Python files in this
repository against each other and writes its findings into the Actions tab.

## What it does

It measures how much of your code overlaps with somebody else's, after
stripping comments, docstrings and whitespace so that reformatting changes
nothing. If the overlap is high on a substantial piece of code, a file called
`SIMILARITY_REPORT.md` appears in your folder.

## What it does *not* do

- It does not decide that you cheated. Your teacher decides that.
- It does not compare short exercises. Below about 300 characters of real code,
  two correct answers to a tightly specified task are often identical, and
  comparing them tells nobody anything. Those files are listed as
  "too short to judge" and never flagged.
- It does not fail your commit. There is no red cross.

## If a report appears in your folder

Read it, then talk to your teacher. There are three honest answers and all of
them are fine to say out loud:

1. **"I wrote it myself."** On a small task, two people solving it properly can
   land on nearly the same code. This happens and it is not a problem.
2. **"We worked on it together."** Collaboration is allowed on plenty of tasks.
   Not mentioning it is what causes trouble.
3. **"I copied it."** Rewrite it your own way and push again. The report file
   removes itself once the overlap drops.

If two submissions arrive in the **same commit**, neither of you was first, so
the report goes into both folders and says so. It is not pointing at either of
you in particular.

Do not delete the report by hand — it is regenerated on every push, so deleting
it just brings it back and looks worse than leaving it.

## How it works, if you are curious

`.github/scripts/similarity_check.py`, standard library only. It compares
25-character shingles of the normalised source (a Jaccard overlap), because that
turned out to be the only measure that separates copied work from independent
work on beginner exercises. Plain text diffing is too noisy, and comparing
program *structure* with variable names removed is useless here — almost every
correct answer to `for i in range(10)` has the same structure.
