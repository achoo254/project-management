# Codebase Summary

## Repository Overview

**Type:** Internal Project Management Repository (Non-Software)
**Purpose:** Monthly OKR/KPI tracking, P2+ performance evaluation, meeting minutes, and internal training material for the iNET Tech Department
**Language:** Vietnamese (team communication), English for technical terms
**Platform:** Cloned on several developer machines (macOS / Windows) + the my.inet.vn portal (web)

Monthly OKR/KPI data **and P2 evaluation levels** live on **my.inet.vn**, not in this repo. What lives here: standards, runbooks, audit reports, meeting minutes, training material, and the P2 scoring formula template.

## Directory Structure

```
project-management/
├── README.md                              # Entry point: structure, workflows, team
├── CLAUDE.md                              # Claude Code instructions + change-logging conventions
├── P2_Form_BP_Cong_Nghe.xlsx              # P2 scoring FORMULA template only (immutable, no levels)
├── .env.example                           # Template for the iCloud env file: sid, ssid, GITLABS_*
├── .gitignore                             # Ignores all .env* plus editor dirs
│
├── docs/
│   ├── quy-tac-viet-noi-dung-okr.html     # OKR content rules (shareable, self-contained)
│   ├── monthly-okr-p2-review-guide.md     # Monthly OKR+P2 review runbook
│   ├── code-standards.md                  # Naming, formats, API and Excel conventions
│   ├── codebase-summary.md                # This file
│   ├── project-overview-pdr.md            # Purpose, processes, success metrics
│   ├── project-roadmap.md                 # Current state & planned improvements
│   ├── env-configuration-guide.md         # Env vars of the related application projects
│   └── decisions/
│       └── 0000-adr-template.md           # ADR template for long-lived decisions
│
├── members/
│   ├── 2026/                              # Authoritative layout: one folder per period
│   │   ├── T3/  T4/                       # P2 forms for 2026-03, 2026-04
│   │   └── T5/                            # P2 forms + evidence audit report (HTML)
│   ├── T5/                                # Legacy copies (pre year/month layout)
│   └── P2_Form_BP_Cong_Nghe - *.xlsx      # Historical workbooks — NOT a data source
│
├── okr-kpi/                               # Monthly OKR+P2 audit reports (from period 07-2026 on)
│   ├── README.md                          # Location, naming and content convention
│   ├── 07-2026/                           # MM-YYYY = period under review, not the month audited
│   └── MM-YYYY/
│       └── review-okr-p2-<scope>-<YYMMDD>.html
│
├── plans/
│   ├── README.md                          # Per-user scoping convention
│   ├── dattqh/                            # Plans owned by dattqh (+ its own reports/)
│   └── reports/                           # Other reports + audit reports for T5–T7 2026
│
├── hop-cxo/
│   └── DD-MM-YYYY/                        # CXO meeting minutes + whisper transcripts
│
├── dao-tao/
│   └── DD-MM-YYYY/                        # Training sessions: HTML slides, transcripts, notes
│
├── scripts/                               # Read-only dump helpers for the formula template (openpyxl)
│   ├── dump_p2_member.py
│   ├── dump_p2_all_sheets.py
│   └── dump_p2_dat.py
│
└── .claude/
    ├── settings.json                      # Project Claude Code settings
    ├── hooks/                             # Local hooks
    └── skills/
        ├── gitlab-okr-kpi/                # Write path: OKR/KPI + P2 drafts + GitLab API
        └── p2-monthly-okr-audit/          # Read-only monthly P2-Delivery audit
```

## File Descriptions

### Core Configuration
| File | Purpose | Owner |
|------|---------|-------|
| `README.md` | Structure, workflows, quick start, team table | Department head |
| `CLAUDE.md` | AI agent instructions; where to record "why" for changes | Department head |
| iCloud env file (path lives in `scripts/load-env.sh`) | my.inet.vn cookies (`sid`, `ssid`) + GitLab tokens — **SECRET, outside the repo**, synced across the owner's Macs | Each developer, in their own iCloud Drive |
| `scripts/load-env.sh` | Loads that file into the shell (`source scripts/load-env.sh`) — the single read point | Department head |
| `.env.example` | Variable names without values, template for the iCloud file | Department head |
| `.gitignore` | Excludes all `.env*`, `.idea`, `.vscode` | Repository admin |

### Documentation
| File | Purpose | Audience |
|------|---------|----------|
| `docs/quy-tac-viet-noi-dung-okr.html` | How to write OKR content: field formats, difficulty scale, grading thresholds, common mistakes | All team members |
| `docs/monthly-okr-p2-review-guide.md` | Monthly review runbook: data sources, 3-layer method, verification traps, report format | Department head |
| `docs/code-standards.md` | File naming, OKR/KPI content standards, P2 scoring conventions, API automation rules | All team members |
| `docs/codebase-summary.md` | Repository structure & file descriptions (this file) | All team members |
| `docs/project-overview-pdr.md` | Project purpose, processes, success metrics | Department head, developers |
| `docs/project-roadmap.md` | Current initiatives, planned improvements, decision log | Department head, developers |
| `docs/env-configuration-guide.md` | Env vars of the related application projects | Developers |
| `docs/decisions/` | ADRs for long-lived architectural decisions | All team members |

### Evaluation Data
| Path | Purpose | Format | Owner |
|------|---------|--------|-------|
| `P2_Form_BP_Cong_Nghe.xlsx` | Scoring formula template — structure, per-role weights, formulas. No levels | Excel | Department head |
| `members/{năm}/T{tháng}/*.xlsx` | Historical per-member workbooks (up to T5/2026). ⛔ Not read by any workflow | Excel | — |
| `members/{năm}/T{tháng}/*.html` | Evidence audit report for the period | HTML | Department head |
| `members/*.xlsx`, `members/T5/` | Older flat copies — do not add new files | Excel | — |

### Meeting Minutes & Training
| Path | Purpose | Format |
|------|---------|--------|
| `hop-cxo/DD-MM-YYYY/` | CXO meeting minutes plus the raw whisper transcripts they were derived from | HTML + TXT |
| `dao-tao/DD-MM-YYYY/` | Internal training sessions (e.g. software architecture, Docker part 1) | HTML slides + SRT/MD |

### Automation Tools
| Path | Purpose | Method | Status |
|------|---------|--------|--------|
| `.claude/skills/gitlab-okr-kpi/` | Create/update OKR entries, draft P2+ evaluations, GitLab API operations | Direct JSON API over `curl` | Active |
| `.claude/skills/p2-monthly-okr-audit/` | Audit P2-Delivery against git commits and official KPI | Read-only, `curl` + git | Active |
| `scripts/dump_p2_*.py` | Dump workbook sheets to text to inspect the formula template | Python 3 + openpyxl, read-only | Active |

## Data Flow

### OKR/KPI Entry Flow
```
1. Member decides the month's OKR from real project work (GitLab issues / plans)
2. Content written per docs/quy-tac-viet-noi-dung-okr.html
   - description = HTML (bold KR name + GitLab anchor)
   - target / result = plain text
   - difficulty = S/M/L/XL, mandatory
3. Entry created — manually on the form, or via /gitlab-okr-kpi:
   - source scripts/load-env.sh (reads sid/ssid from iCloud), pre-flight GET /account/kpi (200 = OK)
   - POST /api/client/v1/accountkpi/create per entry, capture _id
4. Verification:
   - POST /accountkpi/search with monthStr, reconcile totalElements vs rows received
   - No browser or screenshot needed
```

### P2+ Evaluation Flow
```
1. End of month: open the P2 form on my.inet.vn for the period
2. Fill P2-Core (A/B/C/D) + P2-Delivery (okr/quality/commitment) on the portal
   - B4 = role · C8:C11 = Core A/B/C/D · C17:C19 = Delivery okr/quality/commitment
3. POST /p2evaluation/get to load the baseline (preserve every existing field)
4. POST /p2evaluation/compute to get total + grade, confirm with the user
5. Save as draft only — /save (manager) or /saveself (self); never submit or lock
6. Manager reviews and locks the official score on my.inet.vn
```

### Monthly Review Flow
```
Early month N+1, per docs/monthly-okr-p2-review-guide.md:

OKR self-report (accountkpi/search)  +  P2 self-scores (p2evaluation/get)
                          ↓
Cross-check against independent evidence
  - git log on the local repos
  - GitLab API: issues closed, MRs merged, pipeline jobs
  - HTTP production, release tags, bundle last-modified
                          ↓
Effort-weight each OKR (S/M/L/XL from code footprint, not self-declared)
                          ↓
HTML report into okr-kpi/MM-YYYY/ — local only, personnel data
```

The report must carry both `selfScores` and `scores`. A period where `scores` is empty and `status="draft"` means nobody has scored it yet — the portal shows 0 / "Chưa đạt", which is not a bad result but an unscored one, and it stays at 0 until the manager acts.

## Team Members & Roles

| Name | Account | Role | P2 File |
|------|---------|------|---------|
| Trịnh Quốc Hoàn Đạt | dattqh@inet.vn | Trưởng phòng Công Nghệ | `P2_Form_BP_Cong_Nghe - Dat.xlsx` |
| Nguyễn Đăng Đức | ducnd@inet.vn | Frontend | `P2_Form_BP_Cong_Nghe - Duc.xlsx` |
| Bùi Văn Hổ | hobv@inet.vn | Design System | `P2_Form_BP_Cong_Nghe - Ho.xlsx` |
| Đinh Tiến Chương | chuongdt@inet.vn | Frontend | `P2_Form_BP_Cong_Nghe - Chuong.xlsx` |
| Trần Công Tuấn Anh | anhtct@inet.vn | AI Research | Evaluated by another manager — not in this repo |

GitLab user IDs (for evidence queries): dattqh=5, ducnd=27, chuongdt=26, hobv=17.

### Local repo map (evidence sources)
| Member | Local repo (`~/inet-gitlab/`) | GitLab path |
|---|---|---|
| dattqh, ducnd | `cloud-panel-application` (OneDash: backend/client/agent/victoria) | `server-tools/cloud-panel-application` |
| hobv | `design-sys-fe` (packages `@hobui/*`) | `design-system/design-sys-fe` |
| chuongdt | `developers.inet.vn` (+ portal-client/server) | `donv/developers.inet.vn` |

## External Dependencies

### Authentication
- **my.inet.vn:** performance portal — OKR/KPI (`accountkpi`) and P2+ (`p2evaluation`)
- **Credentials:** cookies `sid` + `ssid` in the iCloud env file (lowercase variable names), loaded via `source scripts/load-env.sh`
- **Refresh frequency:** `sid` is a JWT with TTL ≈ 1 day — expect a refresh nearly every session; a 302/401 pre-flight means expired
- **gitlabs.inet.vn:** project access tokens (`GITLABS_ACCESS_TOKEN`), scoped per project

### Tools & Platforms
- **curl + jq:** the whole automation path is plain HTTP — no browser required
- **Python 3.8+ / openpyxl:** P2 Excel dump scripts (not installed system-wide; use a venv)
- **Excel:** P2 evaluation forms
- **Git / GitLab API:** independent evidence for the monthly audit

## Key Metrics & Tracking

### OKR/KPI
- **Cadence:** monthly, declared at the start of the month on my.inet.vn
- **Storage:** `accountkpi` collection, keyed by `account` + `monthStr` (`MMYYYY`)
- **Grading:** effort-weighted completion — "Tốt" needs high completion **and** ≥1 stretch deliverable at L–XL
- **Deadline:** work must land (merged to main / issue closed) on or before the last day of the month

### P2+ Evaluations
- **Cadence:** monthly, one folder per period under `members/{năm}/`
- **Evaluees in this repo:** 4 (dattqh, hobv, ducnd, chuongdt)
- **Formula:** `P2+ Tổng = (P2-Core × coreWeight) + (P2-Delivery × deliveryWeight)`; A/B/C/D weights differ per role and are computed server-side
- **Status flow:** agent saves `draft` → manager reviews → manager locks the official score

## Notes & Observations

1. **Legacy P2 copies:** `members/*.xlsx` and `members/T5/` predate the `{năm}/T{tháng}/` layout. Treat the period folders as authoritative; do not add new files to the flat locations.
2. **Removed directories:** `weekly meetings/` (deleted — content was stale, OKR baseline now comes from my.inet.vn) and `agent/` (manual KPI guide, superseded by the skills). Documentation should not reference either.
3. **Excel structure:** the master template carries the formulas and per-role weights; member copies must preserve them and never hard-code summary cells.
4. **Automation is API-first:** browser automation remains only as a legacy fallback in `gitlab-okr-kpi/references/browser-automation-guide.md`.
5. **Two verification traps** that have caused wrong conclusions before: `accountkpi/search` pages at 30 and ignores `size`; and "đã build lên production" is not evidence without a deploy marker. Both are documented in the review runbook.
6. **Reports stay local:** everything in `okr-kpi/`, `plans/reports/` and the period audit HTML contains personnel data and is never published outside the company.
7. **Audit output location changed:** monthly OKR+P2 audit reports go to `okr-kpi/MM-YYYY/` from period T8/2026 onward. Earlier periods stayed where they were produced (`plans/reports/`, `plans/dattqh/reports/`, `members/2026/T5/`) and were not migrated.

## Glossary

| Term | Vietnamese | Meaning |
|------|------------|---------|
| OKR | Mục tiêu & Kết quả Chính | Monthly objectives declared on my.inet.vn, derived from GitLab project work |
| KPI | Chỉ số hiệu suất | Performance entry in the `accountkpi` collection (distinct from sales KPI in `kpi`) |
| P2+ | Đánh giá P2+ | Monthly evaluation = P2-Core + P2-Delivery |
| P2-Core | Năng lực nền tảng | Foundational competency per role (A/B/C/D), `Đạt` / `Chưa đạt` |
| P2-Delivery | Kết quả công việc | okr / quality / commitment, `Chưa đạt` / `Đạt` / `Tốt` |
| Độ khó | — | Difficulty `S`/`M`/`L`/`XL`, mandatory on the KPI form |
| Chi tiết KPI | — | The only rich-text HTML field; holds the KR name and GitLab anchor |
| Mục tiêu | — | Objective — plain text |
| Kết quả | — | Result — plain text, with numbers and dates |
| Ghi chú | — | Notes — kept empty by convention |
| Chờ duyệt | `waiting` | Awaiting manager approval; the work itself is done |
| Trưởng phòng | — | Department head (Đạt) |
| my.inet.vn | — | iNET internal management portal |
