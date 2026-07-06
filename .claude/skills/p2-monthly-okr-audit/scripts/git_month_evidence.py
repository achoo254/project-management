"""Monthly git evidence for one repo + author, for P2-Delivery audit.

Usage:
    python git_month_evidence.py --repo "<repo path>" --authors "regex1\\|regex2" \
        --month 2026-05 [--grep "keyword a" "keyword b" ...]

Outputs JSON to stdout:
  {
    "total": int,                 # all commits by author in month
    "real": int,                  # excluding semantic-release "chore(release) [skip ci]" + merges
    "featfix": int,               # subjects starting feat/fix
    "per_day": {"YYYY-MM-DD": n}, # cadence (judge "Cam kết & tiến độ")
    "evidence": [                 # one best match per --grep term, for commit links
        {"term":..., "sha":"<7>", "full":"<40>", "subject":...}
    ]
  }

Author regex uses git --author (alternation with \\|). Pass all known identities.
Commit URL = <gitlab base>/-/commit/<full sha>  (see team-roster-and-repos.md).
"""
import argparse, json, subprocess, sys

# Windows console mặc định cp1252 → JSON tiếng Việt sẽ crash. Ép stdout UTF-8.
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass
from datetime import date

def next_month(y, m):
    return (y + 1, 1) if m == 12 else (y, m + 1)

def git(repo, args):
    r = subprocess.run(["git", "-C", repo, *args], capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.stdout

def is_git_repo(repo):
    """Local paths differ per machine/person — verify before scanning. If invalid,
    caller must ASK the user for the correct path (never assume / never count as 0 work)."""
    import os
    if not os.path.isdir(repo):
        return False
    r = subprocess.run(["git", "-C", repo, "rev-parse", "--is-inside-work-tree"],
                       capture_output=True, text=True)
    return r.returncode == 0 and "true" in r.stdout

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--authors", required=True, help=r'git --author regex, e.g. "dattqh\|DatTQH"')
    ap.add_argument("--month", required=True, help="YYYY-MM")
    ap.add_argument("--grep", nargs="*", default=[], help="keywords to fetch one evidence SHA each")
    a = ap.parse_args()

    if not is_git_repo(a.repo):
        print(json.dumps({"error": "repo_not_found",
                          "repo": a.repo,
                          "hint": "Local path khác nhau theo máy/người. HỎI USER đường dẫn đúng (hoặc xác nhận người này có làm repo này tháng đó không) — KHÔNG coi là 0 commit."},
                         ensure_ascii=False, indent=2))
        sys.exit(2)

    y, m = map(int, a.month.split("-"))
    since = f"{y:04d}-{m:02d}-01"
    ny, nm = next_month(y, m)
    until = f"{ny:04d}-{nm:02d}-01"
    base = ["log", "--all", f"--since={since}", f"--until={until}", f"--author={a.authors}"]

    subjects = [s for s in git(a.repo, base + ["--pretty=format:%s"]).splitlines()]
    total = len(subjects)
    def is_noise(s):
        sl = s.lower()
        return ("chore(release)" in sl) or ("[skip ci]" in sl) or s.startswith("Merge ")
    real = sum(1 for s in subjects if not is_noise(s))
    featfix = sum(1 for s in subjects if s.startswith(("feat", "fix")))

    per_day = {}
    for d in git(a.repo, base + ["--pretty=format:%ad", "--date=short"]).splitlines():
        d = d.strip()
        if d:
            per_day[d] = per_day.get(d, 0) + 1
    per_day = dict(sorted(per_day.items()))

    # Fetch all author commits (hash|subject) once, then substring-match grep terms in Python.
    # NB: do NOT pass git -F here — git applies --fixed-strings to --author too, breaking the
    # author alternation regex. Python matching avoids that and handles special chars like "(".
    pairs = []
    for ln in git(a.repo, base + ["--pretty=format:%H|%s"]).splitlines():
        full, _, subj = ln.partition("|")
        if full:
            pairs.append((full, subj))

    evidence = []
    for term in a.grep:
        tl = term.lower()
        hit = next(((f, s) for f, s in pairs if tl in s.lower()), None)
        if hit:
            evidence.append({"term": term, "sha": hit[0][:7], "full": hit[0], "subject": hit[1]})
        else:
            evidence.append({"term": term, "sha": None, "full": None, "subject": "(no match)"})

    print(json.dumps({"repo": a.repo, "month": a.month, "total": total, "real": real,
                      "featfix": featfix, "per_day": per_day, "evidence": evidence},
                     ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
