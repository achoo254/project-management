# Project Overview & Product Development Requirements

## Project Purpose

Internal project management system for the iNET Tech Department. Centralized tracking of monthly OKR/KPI targets, P2+ performance evaluation, meeting minutes, and internal training — with an audit trail that ties self-reported results back to verifiable evidence.

## Organization

**Department:** iNET Tech Department
**Portal:** my.inet.vn (OKR/KPI + P2+), gitlabs.inet.vn (project work)
**Team:** Đạt (Trưởng phòng, dattqh), Đức (ducnd), Hổ (hobv), Chương (chuongdt), Tuấn Anh (anhtct)
**P2 scope of this repo:** dattqh, hobv, ducnd, chuongdt. `anhtct` is evaluated by another manager.

## Key Processes

### 1. Monthly OKR/KPI Declaration
- **Cadence:** monthly — declared at the start of the month, on my.inet.vn
- **Source of work:** real project work on gitlabs.inet.vn (issues, milestones) and plans in `plans/<user>/`
- **Storage:** the `accountkpi` collection on my.inet.vn, keyed by `account` + `monthStr` (`MMYYYY`). Not stored in this repo.
- **Content rules:** [`quy-tac-viet-noi-dung-okr.html`](./quy-tac-viet-noi-dung-okr.html) — field formats, difficulty scale, grading thresholds
- **Automation:** skill `gitlab-okr-kpi` writes entries through the JSON API over `curl`

### 2. Performance Evaluation (P2+)
- **Two parts:** P2-Core (năng lực nền tảng, per role A/B/C/D) and P2-Delivery (kết quả công việc: okr / quality / commitment)
- **Single source:** my.inet.vn. Levels live in `p2evaluation/get` (`selfScores` / `scores`); criteria + weights in `p2config/list`. ⛔ No Excel involved — `P2_Form_BP_Cong_Nghe.xlsx` at root is only the scoring **formula template** and holds no levels.
- **Formula:** `P2+ Tổng = (P2-Core × coreWeight) + (P2-Delivery × deliveryWeight)`; A/B/C/D weights differ per role and are computed server-side
- **Write path:** drafted via the `p2evaluation` API. The agent only ever saves `draft`; the manager reviews and locks the official score.

### 3. Monthly Review & Audit
- **Cadence:** early month N+1, reviewing month N
- **Runbook:** [`monthly-okr-p2-review-guide.md`](./monthly-okr-p2-review-guide.md)
- **Method:** three layers — self-reported completion, real code (git + GitLab + production), then effort-weighting from code footprint
- **Output:** self-contained HTML report in `okr-kpi/MM-YYYY/` (the period under review), kept local — personnel data
- **Evidence rule:** my.inet.vn is the only source of levels — no Excel to reconcile. Read both `selfScores` and `scores`; empty `scores` means unscored (not a bad score), and `locked` means the score must be reopened before it can change.

### 4. Meetings & Training
- **CXO meetings:** minutes in `hop-cxo/DD-MM-YYYY/`, kept alongside the raw transcripts they were derived from
- **Internal training:** material in `dao-tao/DD-MM-YYYY/` as self-contained HTML slides plus source transcript

## Workflows & Dependencies

### OKR/KPI Entry Flow
```
Project work on gitlabs.inet.vn (issues, MRs)
           ↓
Write OKR content per quy-tac-viet-noi-dung-okr.html
  description = HTML (KR name + GitLab anchor) · target/result = plain text · difficulty = S/M/L/XL
           ↓
Authenticate: sid + ssid from .env, pre-flight GET /account/kpi
           ↓
POST /api/client/v1/accountkpi/create per entry (curl, no browser)
           ↓
Verify: POST /accountkpi/search with monthStr, reconcile totalElements vs rows received
```

**Key input:** `.env` holds the my.inet.vn cookies `sid` and `ssid` (lowercase names) plus `GITLABS_ACCESS_TOKEN`.

### P2+ Evaluation Flow
```
Levels from the user, or self-scores already on the portal
           ↓
POST /p2config/list — criteria, weights, valid level names
           ↓
POST /p2evaluation/get — load baseline, preserve every existing field
           ↓
POST /p2evaluation/compute — total + grade, confirm with the user
           ↓
Save as draft (/save for manager, /saveself for self) — never submit or lock
           ↓
Manager reviews and locks the official score on my.inet.vn
```

### Review Flow
```
Self-report (accountkpi/search + p2evaluation/get)
           ↓
Independent evidence: git log · GitLab issues/MRs/pipelines · HTTP production · release tags
           ↓
Effort-weight each OKR (S/M/L/XL from code footprint, not self-declared)
           ↓
Verdict per member + suggested adjustment → HTML report in okr-kpi/MM-YYYY/
```

## Current State

Active OKR/KPI per member is **not duplicated here** — it changes monthly and the portal is the source of truth. Look at:

- **OKR of a month:** `POST /api/client/v1/accountkpi/search` with `{account, monthStr}`, or the KPI detail page `https://my.inet.vn/account/kpi/detail/{email}`
- **P2+ of a period:** `POST /p2evaluation/get` with `{account, period}`
- **Latest reviewed period:** the newest folder under `okr-kpi/` (periods T5–T7 2026 are in `plans/reports/`)
- **Latest P2 forms:** the highest `members/{năm}/T{tháng}/` folder

## Success Metrics

1. **OKR completion rate** — effort-weighted, landed within the month (merged to main / issue closed)
2. **Evidence match rate** — share of self-reported claims that hold up against independent evidence in the monthly audit
3. **OKR content quality** — entries that satisfy the content rules (measurable objective, GitLab anchor, result with numbers, honest difficulty) without needing rework
4. **P2 timeliness** — all in-scope evaluations drafted and locked before the deadline
5. **Documentation accuracy** — docs match the actual repo layout, API behavior, and conventions

## Constraints & Assumptions

- **Authentication:** `sid` is a JWT with TTL ≈ 1 day; it must be refreshed manually from the browser almost every working session. There is no client-side refresh path — SSO exposes no token endpoint for it.
- **API is authoritative, not the form:** `accountkpi/update` fully replaces the record, and `accountkpi/search` pages at 30 while ignoring `size`. Both require deliberate handling.
- **No offline copy of levels:** evaluations exist only on the portal, so an audit is impossible without a live `sid`/`ssid` session. Nothing in the repo can stand in for it.
- **Evidence access:** GitLab tokens are project-scoped, so repos outside the token's scope cannot be verified (has already blocked one claim).
- **Vietnamese UI:** all portal forms are Vietnamese; score values must match exactly including diacritics and casing.
- **Multi-machine:** the repo is cloned on several machines, so the reason for a change must travel with `git pull` — commit body, ADR, or plan file, never a local agent session.

## Risk Assessment

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Expired `.env` cookies | Automation blocked mid-run | Pre-flight check before every write; refresh `sid`/`ssid` from the browser |
| Partial payload sent to `accountkpi/update` | Silent data loss — omitted fields wiped to null | Mandatory read-modify-write via `search` before any update |
| Trusting page 1 of `accountkpi/search` | Wrong conclusion that a member declared no OKR | Always send `monthStr`; reconcile `totalElements` against rows received |
| Self-declared effort taken at face value | Inflated OKR grade | Difficulty re-derived from code footprint during the audit |
| "Deployed to production" without a marker | Late work counted as on-time | Require release tag, prod bundle `last-modified`, or a successful `deploy` job |
| Score arithmetic taken on trust | P2 total wrong in the report | Re-compute `total`/`grade` by hand and via `/p2evaluation/compute`; put the formula in the report |
| Leaked `.env` in git | Credential exposure | All `.env*` ignored; rotate immediately if one ever lands in history |
| Personnel report published externally | Data exposure | Reports stay local in `okr-kpi/` and `plans/reports/`, never deployed or shared outside |

## Next Steps (Priority Order)

1. Keep documentation aligned with the repo as conventions change — stale docs have already misdirected work
2. Track OKR content quality: how many entries need rework because of format or evidence gaps
3. Build a P2 trend view across periods from the portal (`p2evaluation/get` per period + `history[]`) instead of reading each period in isolation
4. Document the P2 evaluation criteria well enough that a second evaluator can apply them consistently
5. Reduce the manual cookie refresh friction in the write path if the portal ever exposes a supported alternative
