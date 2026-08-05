# Code Standards & Conventions

## File Naming Conventions

### Meeting Minutes & Training (`hop-cxo/`, `dao-tao/`)
- **Format:** one folder per session, named `DD-MM-YYYY/`
- **Examples:** `hop-cxo/07-07-2026/`, `dao-tao/22-07-2026/`
- **Contents:** raw sources (transcript `.txt`/`.srt`, extraction notes `.md`) plus one self-contained HTML deliverable
- **Deliverable naming:** describe the content, not the date or a plan ID — `Bien_ban_hop_CXO_7_7_2026_Update.html`, `docker-phan-1-nen-tang.html`
- There is no `weekly meetings/` directory; it was removed. Monthly OKR/KPI data lives on my.inet.vn, not in repo notes.

### P2 Evaluation Data — portal only
- **Evaluation levels live on my.inet.vn**, never in a repo file. Read them with `POST /api/client/v1/p2evaluation/get` body `{account, period}`; criteria + weights with `POST /p2config/list`.
- `P2_Form_BP_Cong_Nghe.xlsx` (root, immutable) is the **scoring formula template only** — weights and VLOOKUP wiring, no levels. Owned by the department head.
- `members/` holds historical workbooks up to T5/2026. ⛔ **Not a data source**: do not read levels from them, do not create new per-member workbooks, do not reconcile portal against them.

### Monthly OKR/P2 Audit Reports (`okr-kpi/`)
- **Location:** `okr-kpi/MM-YYYY/review-okr-p2-<scope>-<YYMMDD>.html`
  - `MM-YYYY` = **the period under review**, not the month the audit ran (a July review executed on 04/08 still goes in `okr-kpi/07-2026/`)
  - `<scope>` = `team` for a whole-team roll-up, or a username when split per member
  - `<YYMMDD>` = the date the audit ran, so re-auditing a period never overwrites the earlier run
  - An accompanying `.md` detail record sits in the same folder under the same base name
- **Source JSON is mandatory** and sits beside the report under the same base name (`.json`); the HTML is rendered from it by `.claude/skills/p2-monthly-okr-audit/scripts/build_html_report.py` (schema v2). Never hand-write the HTML.
- **Required content:** both `selfScores` and `scores` (state explicitly when the manager has not scored yet, and whether `status` is empty / `draft` / `locked`), `total`/`grade` re-verified against the formula, **every** OKR entry with an S/M/L/XL effort badge plus evidence (path/SHA or issue + landed date), a suggested-adjustment column, and any claim that could not be verified marked as such
- See `okr-kpi/README.md` for the full convention. Reports for T5–T7 2026 predate it and stay where they are (`plans/reports/`, `plans/dattqh/reports/`, `members/2026/T5/`).

### Other Reports & Plans
- **Plans:** `plans/<user>/<slug>/` — scoped per person to avoid merge conflicts (see `plans/README.md`)
- **Other reports** (not the monthly OKR/P2 audit): `plans/reports/<kind>-<YYMMDD>-<scope>.html`
- Name files by content, never by phase number or plan ID — renamed plans turn such references into garbage
- Aggregated reports for humans are **HTML**; `.md` is only for the accompanying detail record

### Configuration Files
- **Credentials:** `.env` (git-ignored, never commit)
  - my.inet.vn cookies: `sid`, `ssid` — **lowercase variable names**
  - GitLab: `GITLABS_ACCESS_TOKEN` / `GITLAB_PRIVATE_TOKEN` (project access tokens, not personal)
  - `sid` is a JWT with **TTL ≈ 1 day** — expect to refresh it almost every working session
- **.gitignore:** all `.env*` are ignored; if a secret ever lands in git, **rotate it** (`git rm --cached` is not enough, it stays in history)

### Automation Tools
- **Skill files:** `.claude/skills/<skill-name>/SKILL.md`
  - `gitlab-okr-kpi` — writes OKR/KPI and P2 drafts to my.inet.vn, plus GitLab API operations
  - `p2-monthly-okr-audit` — read-only monthly audit of P2-Delivery against git + KPI evidence
  - Frontmatter: name, description, license, version, argument-hint
  - Long detail goes in `references/*.md`, not inline in SKILL.md

## OKR/KPI Content Standards

Full rules with worked examples: [`quy-tac-viet-noi-dung-okr.html`](./quy-tac-viet-noi-dung-okr.html). Summary of the binding conventions:

### Field formats (my.inet.vn KPI form)
| Vietnamese Label | API field | Format | Content |
|------------------|-----------|--------|---------|
| Chi tiết KPI | `description` | **Rich text HTML** (`<p> <strong> <em> <ul> <ol>`) | KR name in bold on the first line, short scope description, GitLab issue anchor on the last line |
| Mục tiêu | `target` | **Plain text only** (HTML gets escaped and shows raw) | Commitment for the month, verifiable, one sentence |
| Kết quả | `result` | **Plain text**, multi-line allowed | Actual landed outcome with concrete numbers and dates |
| Độ khó / phức tạp | `difficulty` | `S` / `M` / `L` / `XL` — **mandatory** | Estimated objectively from code footprint (files, LOC, commits, layers) |
| Ghi chú | `note` | Leave empty | No links, no effort labels, no plan paths |
| *(period)* | `monthStr` | `MMYYYY` | e.g. `082026` |

### Content rules
1. **Vietnamese with full diacritics.** Keep English technical terms as-is (observability, pipeline, deploy) — do not force-translate.
2. **Objectives must be measurable.** "100% Design System" is not verifiable; "hoàn thành 4/4 Objective DS-R4, publish v1 lên registry" is.
3. **One GitLab issue per OKR**, written as an anchor carrying the issue title — never a bare `#166`.
4. **Results carry numbers and dates** so an auditor can match them against git objects and HTTP responses.
5. **One KR per entry** — never merge several KRs into one, the monthly report reconciles entry count against `monthStr`.
6. **Difficulty is re-derived from code during audit** — self-declared effort is not trusted.

### Grading thresholds
- **"Tốt"** requires high completion **and** at least one stretch deliverable at `L`–`XL`. Many `S`/`M` tasks cap out at "Đạt".
- OKR for month N must land (merged to main / issue closed) **on or before the last day of month N**. Landing the next month counts as late.
- "Đã build lên production" is not evidence. Point at a release tag, the prod bundle's `last-modified`, or a successful `deploy` pipeline job.
- `status = "waiting"` means awaiting manager approval, **not** unfinished work.

## P2 Scoring Conventions

### Where the data lives
- **Levels:** my.inet.vn only (`p2evaluation/get` → `selfScores` / `scores`). Entered on the portal form, drafted via API, locked by the manager.
- **Criteria, weights, level→score:** `p2config/list` (per department). Verify each period — weights can change.
- **Formula reference:** `P2_Form_BP_Cong_Nghe.xlsx` at root. Read-only reference for how the score is composed; ⛔ never a place to record an evaluation.

### Formula (re-verify every report)
- `delivery = Σ(score(level) × weight)` — OKR ×0.40 · quality ×0.35 · commitment ×0.25
- `core = Σ(weight_i × level_i)` — A/B/C/D weights **differ per role**; take them from `computed.subScores` / `p2config/list`, never hard-code
- `total = core×0.5 + delivery×0.5` · `grade`: `<1` Chưa đạt · `=1` Đạt · `>1` Tốt
- Validate with `POST /p2evaluation/compute` (read-only, never submit) and compare against `selfComputed` / `computed` from the server.

### Formula template structure (`P2_Form_BP_Cong_Nghe.xlsx`, reference only)
| Sheet | Purpose |
|-------|---------|
| `TỔNG QUAN & LƯU Ý` | Overview and usage notes |
| `CẤU TRÚC & TRỌNG SỐ` | Criteria structure and per-role weights |
| `ĐÁNH GIÁ HIỆU SUẤT P2` | Formula layout for the scoring sheet — kept so the composition can be checked; levels are **not** filled in here |
| `MÔ TẢ - PHỤ LỤC` | Criteria descriptions / appendix |
| `NHÂN SỰ` | Personnel reference data |
| `Summary_Ranking` | Aggregated ranking |

### Score values
- **P2-Core** (per role, A/B/C/D): `Đạt` / `Chưa đạt`
- **P2-Delivery** (okr / quality / commitment): `Chưa đạt` / `Đạt` / `Tốt`
- Values must match my.inet.vn exactly, including diacritics and casing.

## Documentation Standards

### Markdown Files in `docs/`
- **Encoding:** UTF-8
- **Line Endings:** LF (Unix style)
- **Headings:** one H1 (`#`) as the document title, H2/H3 for sections
- **Tables:** Use pipe syntax; include header separator
- **Code Blocks:** Specify language for syntax highlighting
- **Links:**
  - Internal: Relative paths starting with `./` (e.g., `./project-roadmap.md`)
  - External: Full URLs with protocol (e.g., `https://my.inet.vn`)
- **Vietnamese Content:** Acceptable throughout; ensure consistency and full diacritics

### HTML Deliverables
Anything shared with the team (reports, guides, training slides, meeting minutes) is a **self-contained HTML file**:
- Inline all CSS and JS — no CDN, no external fonts, no linked assets
- Style follows the iNET Design System (viui): primary `#0582D4`, gradient `#0582D4→#619ee9`, accent `#E8353C`; font Be Vietnam Pro with system fallback
- Must be visual (cards, badges, tables, timelines), not a wall of text
- Personnel data stays local — never publish outside the company

### Project Documentation Files
| File | Audience | Update Frequency |
|------|----------|------------------|
| `quy-tac-viet-noi-dung-okr.html` | All team members | When the KPI form or grading rules change |
| `monthly-okr-p2-review-guide.md` | Department head | After each monthly review that finds a new trap |
| `project-overview-pdr.md` | Department head, developers | Quarterly or after major changes |
| `codebase-summary.md` | All team members | After structural changes |
| `code-standards.md` | All team members | As conventions evolve |
| `project-roadmap.md` | Department head, developers | Monthly at minimum |
| `decisions/*.md` | All team members | One ADR per long-lived architectural decision |

## Environment Variables (`.env`)

### Required Variables
```bash
# my.inet.vn session authentication (lowercase names)
sid=<jwt_session_token>
ssid=<server_session_id>

# GitLab (gitlabs.inet.vn) — project access tokens
GITLABS_ACCESS_TOKEN=<token>
```

### Security Rules
1. **Never commit** `.env` — all `.env*` patterns are git-ignored
2. **Store locally** on the development machine only
3. **Refresh `sid` ≈ daily** — it is a JWT with `exp = iat + 86400`; a 302/401 pre-flight means expired
4. **Retrieve:** Browser DevTools → Application → Cookies → copy `sid` and `ssid`
5. **Share:** only via secure channels, never email or group chat
6. **If leaked:** rotate immediately — removing the file from the index does not purge git history

### Format
- One variable per line
- No spaces around `=`
- String values unquoted unless they contain spaces or special characters
- Comments: prefix with `#`

## Python Scripts

### Location: `scripts/`
Read-only helpers that dump workbook content to text so the **formula template** can be inspected (`openpyxl`). They do not write to any workbook, and they are **not** part of the audit flow — audits read the portal API, never a workbook.

| Script | Purpose |
|--------|---------|
| `dump_p2_member.py` | Dump a workbook's P2 sheet plus metadata — `dump_p2_member.py <xlsx_path> <out_txt>` |
| `dump_p2_all_sheets.py` | Dump every sheet of a workbook |
| `dump_p2_dat.py` | Convenience wrapper for one file |

### Conventions
- **Python:** 3.8+; dependency `openpyxl` (not installed system-wide — use a venv)
- **Naming:** `snake_case.py`, matching the existing scripts
- **Docstring:** first line states the purpose and usage
- **Read-only by default.** Any script that writes to a P2 workbook must back the file up first and be tested on a copy
- **Error handling:** log failures, never silently ignore

## API Automation Standards

### `gitlab-okr-kpi` skill
- **Method:** direct JSON API over `curl` — `POST /api/client/v1/accountkpi/{create,update,delete,search}`. Browser automation is legacy fallback only.
- **Authentication:** cookie pair `sid` + `ssid` from `.env`; pre-flight with `GET /account/kpi` (200 = OK, 302/401 = expired)
- **`update` is FULL REPLACE.** Fields omitted from the payload are wiped to null. Always read-modify-write: `search` → merge (keep `difficulty`) → `update`.
- **`search` pages at 30 entries and ignores `size`.** Always send `monthStr` so the backend filters; never fetch one page and filter client-side. Reconcile `totalElements` against the rows actually received.
- **`delete` is a hard delete** with no undo — verify `_id` via `search` and confirm with the owner first.
- **Avoid `bonusMoney`** — the UI overwrites `result` with "Hoàn thành" when it is set.
- **User confirmation:** show the planned entries and one full sample payload before the first write.
- **P2 evaluations are only ever saved as `draft`.** The agent never submits or locks a score; the manager does that on my.inet.vn.

## Quality Checklist

Before committing changes:

### OKR/KPI Entries
- [ ] `Chi tiết KPI` opens with the bold KR name and ends with a GitLab anchor carrying the issue title
- [ ] `Mục tiêu` and `Kết quả` contain no HTML tags
- [ ] `Kết quả` has concrete numbers and dates, not "đã hoàn thành"
- [ ] `Độ khó` selected and consistent with the real code footprint
- [ ] `Ghi chú` left empty
- [ ] `monthStr` is `MMYYYY` and matches the intended period
- [ ] Full Vietnamese diacritics throughout
- [ ] At least one `L`/`XL` entry in the month if aiming for "Tốt"
- [ ] Work landed within the month; deploy claims backed by a verifiable marker

### P2 Evaluation (portal)
- [ ] Levels entered on my.inet.vn, not in any file — exact values (`Đạt` / `Chưa đạt` for Core; `Chưa đạt` / `Đạt` / `Tốt` for Delivery)
- [ ] `roles[]` matches the member's actual work for that period (A/B/C/D weights differ per role)
- [ ] `total`/`grade` from the server matches the formula re-computed by hand or via `/p2evaluation/compute`
- [ ] Agent saved `draft` only; the manager locks the final score
- [ ] `status` reported correctly: empty (nobody scored) / `draft` / `locked` (needs reopen to change)

### Documentation
- [ ] UTF-8 encoding, LF line endings
- [ ] One H1 title, H2+ for sections
- [ ] Internal links are relative paths and actually resolve
- [ ] Code blocks have language specified
- [ ] HTML deliverables are self-contained (no CDN or external assets)
- [ ] Claims and dates match the change actually made

### Code/Automation
- [ ] `.env` not committed (verify `.gitignore` covers it)
- [ ] Credentials not logged or printed; tokens masked to the last 4 characters
- [ ] User confirmation implemented for destructive operations (update, delete)
- [ ] Error messages descriptive and actionable
- [ ] Commit message body explains **why**, not just what

## Glossary & Vietnamese Terms

| Term | Usage Context |
|------|---------------|
| OKR / Mục tiêu & Kết quả Chính | Monthly objectives declared on my.inet.vn, derived from GitLab project work |
| KPI / Chỉ số hiệu suất | Performance entries tracked via `accountkpi` on my.inet.vn (distinct from sales KPI in the `kpi` collection) |
| P2+ | Monthly performance evaluation = P2-Core (năng lực nền tảng) + P2-Delivery (kết quả công việc) |
| P2-Core | Foundational competency per role, criteria A/B/C/D, scored `Đạt` / `Chưa đạt` |
| P2-Delivery | Work outcome: okr / quality / commitment, scored `Chưa đạt` / `Đạt` / `Tốt` |
| Mục tiêu | "Objective" — plain-text field in the KPI form |
| Kết quả | "Result" — plain-text outcome field in the KPI form |
| Ghi chú | "Notes" — optional field, kept empty by convention |
| Chi tiết KPI | "KPI Details" — the only rich-text HTML field |
| Độ khó / phức tạp | "Difficulty" — `S`/`M`/`L`/`XL`, mandatory |
| Chờ duyệt (`waiting`) | Awaiting manager approval — the work itself is done |
| Trưởng phòng | "Department Head" — Đạt (dattqh) |
| Biên bản họp | "Meeting minutes" — stored in `hop-cxo/DD-MM-YYYY/` |
| Đào tạo / Chia sẻ | "Training / Sharing" — material in `dao-tao/DD-MM-YYYY/` |

## Common Mistakes to Avoid

1. **OKR content:** putting HTML in `Mục tiêu` or `Kết quả` → renders as raw text on the form; only `Chi tiết KPI` accepts HTML
2. **OKR content:** writing "đã hoàn thành, đã build lên production" → not evidence; give numbers, dates, and a deploy marker
3. **OKR content:** omitting `Độ khó` → the form blocks the save with *"Vui lòng chọn Độ khó/phức tạp của KPI"*
4. **API:** sending only the changed fields to `update` → every other field is wiped to null
5. **API:** fetching one page from `search` and filtering client-side → entries of the target month get lost for anyone with history
6. **P2 source:** reading evaluation levels from an `.xlsx`, or creating a new per-member workbook — levels exist only on my.inet.vn
7. **Excel:** modifying the formula template, or hard-coding values into summary cells
8. **Environment:** committing `.env`, or assuming `sid` lasts a month — it lasts about a day
9. **Deliverables:** shipping HTML that pulls fonts or CSS from a CDN → breaks offline and outside the network
10. **Documentation:** hard-coding facts that drift → link to the source file instead

## Update Frequency & Ownership

| Document | Owner | Frequency |
|----------|-------|-----------|
| OKR entries on my.inet.vn | Each member | Monthly, at the start of the month |
| P2 evaluation files | Department head + individual | Monthly (one folder per period) |
| Master P2 template | Department head | As needed (criteria changes) |
| Monthly audit reports (`okr-kpi/MM-YYYY/`) | Department head | Monthly, early in month N+1 |
| Meeting minutes (`hop-cxo/`) | Meeting lead | Per session |
| Training material (`dao-tao/`) | Session speaker | Per session |
| `.env` credentials | Each developer, locally | `sid` roughly daily; tokens as they rotate |
| Documentation (`docs/`) | Tech team / department head | Quarterly or after major changes |
| ADRs (`docs/decisions/`) | Decision owner | One per long-lived decision |
