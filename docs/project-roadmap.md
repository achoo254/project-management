# Project Roadmap

## Current Status (August 2026)

### Phase 1: Foundation — COMPLETE (Q4 2025)
- [x] Establish the meeting cadence
- [x] Create the master P2 evaluation template
- [x] Set up member-specific evaluation files
- [x] Deploy the first OKR/KPI automation skill
- [x] Document the KPI entry process on my.inet.vn
- **Outcome:** team coordination framework operational

### Phase 2: Active OKR/KPI Tracking — COMPLETE (Mar–Jun 2026)
- [x] Monthly OKR/KPI declared on my.inet.vn for all in-scope members
- [x] Automation moved from browser to **direct JSON API** (`curl`) — faster and no longer breaks on Angular DOM changes
- [x] Full API contract captured and verified (create / update / delete / search, plus the `difficulty` field)
- [x] P2 forms reorganized into `members/{năm}/T{tháng}/`
- [x] `weekly meetings/` retired — OKR baseline is now the portal, not repo notes
- **Outcome:** an OKR entry can be created and verified over HTTP alone, no browser involved

### Phase 3: Audit & Evidence — IN PROGRESS (Jun 2026 →)
- [x] Monthly OKR+P2 review runbook (`monthly-okr-p2-review-guide.md`)
- [x] Read-only audit skill `p2-monthly-okr-audit`
- [x] P2+ evaluation drafting through the `p2evaluation` API (draft only; the manager locks scores)
- [x] Effort-weighted grading with difficulty derived from code footprint rather than self-declaration
- [x] Reviews delivered for T5, T6 and T7 2026 as self-contained HTML reports
- [x] Runbook hardened against three verification traps that had produced wrong conclusions
- [x] OKR content rules published for the whole team (`quy-tac-viet-noi-dung-okr.html`)
- [ ] Trend view across periods instead of reading each month in isolation
- [ ] Track how many entries need rework because of format or evidence gaps
- **Goal:** every self-reported result is either confirmed by independent evidence or explicitly marked unverifiable

## Active Initiatives

Per-member OKR/KPI is **not duplicated in this document** — it changes monthly and the portal is the source of truth. Read the current month from `accountkpi/search` or the KPI detail page; read the last reviewed period from the newest folder under `okr-kpi/` (periods T5–T7 2026 are still in `plans/reports/`).

Training sessions are recorded as they happen in `dao-tao/DD-MM-YYYY/` (most recent: software architecture 10/07/2026, Docker part 1 22/07/2026).

## Planned Improvements

Sizing uses complexity tiers, not hours: **S** = 1–3 files isolated · **M** = 4–10 files, one module · **L** = 10+ files or cross-module · **XL** = structural change or migration.

### Priority 1: Cross-period P2 & OKR trend view — tier M
**Goal:** see how a member moves across months instead of re-reading one period at a time

#### Tasks
1. Aggregate P2 scores across periods from the portal (`p2evaluation/get` + `history[]`)
2. Aggregate OKR completion and difficulty mix per member per month
3. Render one self-contained HTML view: score trajectory, difficulty mix, verdict history

**Success criteria**
- [ ] One page answers "is this member trending up or down, and on what"
- [ ] Difficulty mix visible per month, so a run of all-S months is obvious
- [ ] Generated from the API and repo files, with no manual re-entry

---

### Priority 2: OKR content quality gate — tier S
**Goal:** catch format and evidence problems before the month is graded

#### Tasks
1. Validate entries against the published content rules: HTML only in `description`, GitLab anchor present, `result` carries numbers, `difficulty` set, `note` empty
2. Flag months where no entry reaches L/XL while the self-assessment claims "Tốt"
3. Report per member early in the month, while entries can still be fixed

**Success criteria**
- [ ] Zero entries with HTML leaking into `target`/`result`
- [ ] Every entry carries a resolvable GitLab anchor or an explicit reason it cannot
- [ ] Content problems surface before the review, not during it

---

### Priority 3: Document the P2 evaluation criteria — tier S
**Goal:** a second evaluator reaches the same score on the same evidence

#### Tasks
1. Extract the criteria definitions and per-role weights from the master template into readable form
2. Write worked examples for each level: what `Đạt` versus `Tốt` actually looked like in a real month
3. Record the agreed thresholds, including the "Tốt requires a stretch deliverable" rule

**Success criteria**
- [ ] Guide published and reviewed by the team
- [ ] Two evaluators scoring the same month land within one level
- [ ] New evaluators can apply the criteria without a walkthrough

---

### Priority 4: Reduce the cookie-refresh friction — tier S, blocked externally
**Goal:** stop losing runs to an expired `sid` mid-write

#### Tasks
1. Fail fast with a clear message and the exact recovery steps on any 302/401 pre-flight
2. Check remaining token lifetime before a batch write and warn if it will not outlast the batch
3. Revisit if SSO ever exposes a supported refresh path for clients

**Success criteria**
- [ ] No partially-written batch caused by expiry mid-run
- [ ] Recovery instructions require no lookup elsewhere

*Note: there is no client-side refresh today — SSO exposes no token endpoint, so the manual browser login stays in the loop.*

---

## Future Enhancements

### Integration
- Link P2 evaluations to the portal's employee profiles
- Use the portal's indexed GitLab data (`esgitlabcommit`, `esgitlabissue`, `gitlabproject`) as a second evidence source alongside the direct GitLab API
- Widen evidence coverage: project-scoped tokens have already blocked verification of at least one repo

### Advanced Analytics
- Correlate OKR difficulty mix with P2 outcomes across periods
- Skill matrix mapping team capability to project assignment
- Capacity planning from historical landed-work velocity

### Tool Modernization
- ~~Move P2 from Excel to a structured store~~ — done 08/2026: the portal is the only store; workbooks keep the scoring formula only
- Generate the monthly report end-to-end from API data with no manual assembly

---

## Timeline Summary

| Phase | Duration | Status | Key Deliverables |
|-------|----------|--------|------------------|
| **Phase 1: Foundation** | Q4 2025 | ✓ COMPLETE | Meeting cadence, P2 template, first automation skill |
| **Phase 2: Active Tracking** | Mar–Jun 2026 | ✓ COMPLETE | API-first automation, verified contract, period-based P2 layout |
| **Phase 3: Audit & Evidence** | Jun 2026 → | ⏳ IN PROGRESS | Review runbook, audit skill, T5–T7 reports, OKR content rules |
| **Phase 4: Trend & Integration** | Q4 2026 | 📋 PLANNED | Cross-period trends, content quality gate, criteria documentation |

---

## Success Metrics & KPIs

### Operational
| Metric | Target | Current | Owner |
|--------|--------|---------|-------|
| OKR declared for the month by all in-scope members | 100% | Met for T5–T7 2026 | Đạt |
| Monthly review delivered early in month N+1 | 100% | Met for T5–T7 2026 | Đạt |
| P2 drafted and locked before the deadline | 100% | Partly — some periods sat at `draft` with no manager score | Đạt |
| Documentation matches the actual repo and API | Zero discrepancies | Realigned 05/08/2026 | Tech team |

### Quality
| Metric | Target | Current | Measurement |
|--------|--------|---------|-------------|
| Self-reported claims confirmed by independent evidence | ≥95% | T7: 17/18 verifiable claims matched | Monthly audit |
| Entries needing rework for format or evidence gaps | 0 | Not yet measured | Content quality gate (Priority 2) |
| Months where "Tốt" is claimed without an L/XL deliverable | 0 | Not yet measured | Difficulty mix per month |

### Efficiency
| Metric | Baseline | Current | Note |
|--------|----------|---------|------|
| OKR entry method | Browser automation, fragile on UI changes | Direct HTTP, verified by API response | Browser path kept only as legacy fallback |
| Review evidence gathering | Manual reading of each repo | Scripted git + GitLab API queries per member | Repo map in the runbook |
| Report production | Hand-written | Self-contained HTML from a repeatable runbook | Personnel data stays local |

---

## Risk Management

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|-----------|
| iCloud env cookies expire (`sid` TTL ≈ 1 day) | Automation blocked, possibly mid-batch | High | Pre-flight before every write; fail fast with recovery steps |
| Partial payload sent to `accountkpi/update` | Silent data loss — omitted fields wiped to null | Medium | Mandatory read-modify-write via `search` |
| Trusting page 1 of `accountkpi/search` | Member wrongly reported as having declared no OKR | Medium | Always send `monthStr`; reconcile `totalElements` against rows received |
| Self-declared effort taken at face value | Inflated OKR grade | Medium | Difficulty re-derived from code footprint during audit |
| Deploy claimed without a verifiable marker | Late work counted as on-time | Medium | Require release tag, prod bundle `last-modified`, or a successful `deploy` job |
| P2 left at `draft` with no manager score | The period scores zero on the portal | Medium | Review report flags any period still unscored |
| Token scope gaps on GitLab | Some claims cannot be verified at all | Medium | Mark explicitly as unverifiable rather than assuming either way |
| Documentation drifts from reality | Wrong folder, wrong skill name, wrong env var sends work down a dead end | Medium | Re-verify against the repo whenever conventions change |
| Personnel report published externally | Data exposure | Low | Reports stay local in `okr-kpi/` and `plans/reports/`, never deployed |

---

## Dependencies & Blockers

### Resolved
- [x] **Is Tuấn Anh in scope?** No — `anhtct` is evaluated by another manager. P2 scope here: dattqh, hobv, ducnd, chuongdt.
- [x] **What is the P2 scoring scale?** P2-Core: `Đạt` / `Chưa đạt`. P2-Delivery: `Chưa đạt` / `Đạt` / `Tốt`. Weights differ per role and the total is computed server-side.
- [x] **Where does the OKR baseline come from now?** my.inet.vn (`accountkpi`), not repo meeting notes.

### Current
- [ ] Some periods still sit at `draft` with no manager score — needs a pass on the portal
- [ ] No measurement yet of OKR content quality (Priority 2 covers it)

### External Dependencies
- **my.inet.vn availability** for every read and write
- **SSO login in a browser** to refresh `sid` — no programmatic alternative exists
- **GitLab token scope** determines which repos can be used as evidence

### Internal Dependencies
- iCloud env file refreshed by each developer in their own iCloud Drive, roughly daily for `sid`
- Master P2 template must preserve formulas when copied
- Evidence requires the member's repos to be cloned locally under `~/inet-gitlab/`

---

## Decision Log

| Date | Decision | Rationale | Owner |
|------|----------|-----------|-------|
| 2025-Q4 | Adopt an OKR/KPI automation skill (then named `okr-kpi-myinet`) | Reduce manual data entry on my.inet.vn | Đạt |
| 2026-01 | Create the `docs/` folder | Establish standards and processes | Tech team |
| 2026-03 | Plan a performance tracking view | Enable visibility into team progress | Đạt |
| 2026-03-13 | Fold the skill into `gitlab-okr-kpi` | OKR originates from GitLab project work; one skill covers both surfaces | Đạt |
| 2026-05-04 | Replace browser automation with the direct JSON API | Browser path was slow and broke on Angular DOM changes; API is verifiable by response | Đạt |
| 2026-06-08 | Retire `weekly meetings/`; OKR baseline becomes my.inet.vn | Notes had gone stale and disagreed with the portal, which is the system of record | Đạt |
| 2026-06-08 | Reorganize P2 forms into `members/{năm}/T{tháng}/` | Evaluation is monthly; a flat folder could not express periods | Đạt |
| 2026-06-12 | Adopt ADRs (`docs/decisions/`) and per-user plan scoping (`plans/<user>/`) | The repo is cloned on several machines, so the reason for a change must travel with `git pull` | Đạt |
| 2026-07-01 | Add the monthly review runbook and a read-only audit skill | Self-assessment alone is not evidence; the audit path must be repeatable and never mutate scores | Đạt |
| 2026-07-09 | Make `difficulty` (`S`/`M`/`L`/`XL`) mandatory in every payload | The form requires it, and effort-weighted grading needs an objective input | Đạt |
| 2026-08-04 | Harden the runbook against three verification traps | Each trap had already produced a wrong conclusion in a real review | Đạt |
| 2026-08-05 | Publish the OKR content rules; realign all docs with the actual repo | Docs still referenced a deleted folder, a renamed skill, and wrong env vars — enough to send work down a dead end | Đạt |
| 2026-08-05 | Drop Excel as a P2 data source entirely — workbooks keep the scoring formula only, levels live on my.inet.vn | Two sources for the same score drift apart; audits reconciled a file nobody kept current | Đạt |

---

## How to Use This Roadmap

1. **Department head (Đạt):** check Phase 3 for what is still open, "Success Metrics" for where the team stands, and "Risk Management" before trusting any number
2. **Technical work:** follow "Planned Improvements" for priorities and tiers; check "Dependencies & Blockers" before starting
3. **All team members:** read [`quy-tac-viet-noi-dung-okr.html`](./quy-tac-viet-noi-dung-okr.html) before declaring OKR, and [`code-standards.md`](./code-standards.md) for file and format conventions
4. **Onboarding:** start with [`codebase-summary.md`](./codebase-summary.md) for the repository layout, then this file for direction and the decision log for the reasons behind it
