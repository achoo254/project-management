# Project Roadmap

## Current Status (March 2026)

### Phase 1: Foundation (COMPLETE)
- [x] Establish weekly meeting cadence
- [x] Create master P2 evaluation template
- [x] Set up member-specific evaluation files (5 members)
- [x] Deploy okr-kpi-myinet automation skill
- [x] Document KPI entry process on my.inet.vn
- **Timeline:** Completed by Q4 2025
- **Outcome:** Team coordination framework operational

### Phase 2: Active OKR/KPI Tracking (IN PROGRESS)
- [x] March 2026 OKRs/KPIs assigned
- [ ] February 2026 KPI forms completed (verify completion on my.inet.vn)
- [ ] Implement monthly OKR/KPI automation (reduce manual data entry)
- [ ] Create KPI tracking dashboard view
- **Timeline:** March - May 2026
- **Goal:** 100% OKR/KPI completion rate; reduce KPI entry time from 2 hours to 30 minutes per month
- **Success Metric:** All assigned OKRs/KPIs appear on my.inet.vn by 5th of each month

## Active Initiatives (March 2026)

### Team Assignments
| Member | OKR | KPI | Priority |
|--------|-----|-----|----------|
| Hổ | 100% Design System | — | High |
| Đức | Nâng cấp vFirewall v2 | Hoàn thiện FE CloudPanel | High |
| Chương | — | Hoàn thiện service hosting | Medium |
| Tuấn Anh | Cải thiện quy trình xử lý lạm dụng | Cải thiện số hóa tài liệu | Medium |
| Đạt (Lead) | Team leadership | OKR/KPI oversight | Critical |

### Training Schedule (March 2026)
- **Week 1:** Brainstorming App Desktop Localman (Postman-like) - Collaborative
- **Week 2:** Chatbot – Tuấn Anh
- **Week 3:** TBD – Chương (content pending)
- **Week 4:** Design System – Hổ

## Planned Improvements (Q2-Q3 2026)

### Priority 1: Automation Enhancement (April-May 2026)
**Goal:** Reduce manual KPI entry time, improve data accuracy

#### Tasks
1. **Extend okr-kpi-myinet skill**
   - Add multi-member batch processing (currently single member)
   - Implement issue-to-KPI matching (auto-suggest relevant issues)
   - Add validation before save (check for required fields)
   - Support for multiple projects per member

2. **Create KPI Form Validation Script**
   - Verify all required fields filled
   - Check objective/result text length (min 20 chars)
   - Validate issue links are accessible
   - Report validation errors before submission

3. **Monthly KPI Reminder System**
   - Auto-generate summary from meeting notes
   - Send reminders to members for missing entries
   - Track completion status by deadline

**Success Criteria:**
- [ ] OKR/KPI automation completes in under 15 minutes for all members
- [ ] 100% form validation pass rate before submission
- [ ] Zero manual corrections needed on my.inet.vn after automation

**Effort Estimate:** 20-30 hours development + testing

---

### Priority 2: P2 Evaluation Process Simplification (May-June 2026)
**Goal:** Streamline P2 scoring, reduce errors, improve consistency

#### Tasks
1. **Document P2 Evaluation Criteria**
   - Extract criteria definitions from master template
   - Create scoring guide (what constitutes L1, L2, L3 or 1-5 score)
   - Provide example evaluations per score level
   - Share expectations with all evaluators

2. **Create P2 Scoring Template with Automated Calculations**
   - Validate score inputs (prevent out-of-range values)
   - Auto-calculate category averages
   - Generate final score recommendation
   - Preserve formula integrity when copying

3. **Implement P2 Bulk Update Script (reactivate)**
   - Recover openpyxl scripts from git history
   - Add error logging and rollback capability
   - Test with sample data before production use
   - Document script usage and safety procedures

**Success Criteria:**
- [ ] P2 evaluation guide published and reviewed by team
- [ ] All 5 member P2 files use consistent scoring scale
- [ ] Evaluation process time reduced by 30%

**Effort Estimate:** 15-20 hours documentation + development

---

### Priority 3: Meeting Notes Organization (April 2026)
**Goal:** Improve accessibility and historical tracking

#### Tasks
1. **Migrate Old Meeting Notes to Year Subdirectories**
   - Move all 2025 files to `weekly meetings/2025/`
   - Create `weekly meetings/2026/` structure
   - Ensure consistent DD-MM-YYYY naming
   - Update any root-level files to year folders

2. **Create Meeting Notes Archive Index**
   - Generate searchable list of all meetings by month/year
   - Link to relevant OKR/KPI assignments
   - Tag meetings by topic (infrastructure, frontend, backend, process improvement)

3. **Implement Meeting Notes Template**
   - Standardize format across all future meetings
   - Include decision log, action items, next steps
   - Enforce Vietnamese language for consistency

**Success Criteria:**
- [ ] All meeting notes organized by year
- [ ] Archive index created and maintained
- [ ] Template adopted for future meetings

**Effort Estimate:** 5-10 hours documentation

---

### Priority 4: Performance Tracking Dashboard (June-July 2026)
**Goal:** Visualize team progress, identify bottlenecks

#### Tasks
1. **Create OKR/KPI Completion Report**
   - Query my.inet.vn KPI status weekly
   - Generate completion percentage by member/category
   - Track on-time vs. late submissions
   - Identify frequently missed deadlines

2. **Build P2 Evaluation Summary Dashboard**
   - Aggregate scores across team
   - Identify high performers and development areas
   - Track evaluation timeliness
   - Generate quarterly performance reports

3. **Implement Monthly Status Report Generation**
   - Combine KPI completion + P2 scores + meeting notes
   - Auto-generate monthly team status for leadership
   - Highlight risks and blockers

**Success Criteria:**
- [ ] Weekly OKR/KPI status report automated
- [ ] Monthly P2 summary accessible to lead
- [ ] Dashboard updated automatically (no manual entry)

**Effort Estimate:** 25-35 hours development

---

## Future Enhancements (Q4 2026+)

### Extended Team Support
- **Tuấn Anh:** Create P2 evaluation file (currently not in members/)
- **New team members:** Establish onboarding process for P2/OKR tracking

### Integration Improvements
- Connect P2 evaluations to my.inet.vn employee profiles
- Auto-sync project assignments between local tracking and portal
- Create unified team roster with contact info

### Advanced Analytics
- Trend analysis: How OKR/KPI completion correlates with P2 scores
- Skill matrix: Map team capabilities to project assignments
- Capacity planning: Balance workload based on historical velocity

### Tool Modernization
- Migrate from Excel to structured database (PostgreSQL)
- Create web UI for P2 evaluations (replace Excel files)
- Build real-time KPI dashboard (replace manual tracking)
- Mobile app for meeting notes capture

---

## Timeline Summary

| Phase | Duration | Status | Key Deliverables |
|-------|----------|--------|------------------|
| **Phase 1: Foundation** | Q4 2025 | ✓ COMPLETE | Weekly cadence, P2 template, okr-kpi-myinet skill |
| **Phase 2: Active Tracking** | Mar-May 2026 | ⏳ IN PROGRESS | March OKRs/KPIs assigned, automation operational |
| **Phase 3: Optimization** | Jun-Aug 2026 | ⏳ PLANNED | Enhanced automation, P2 process docs, performance dashboard |
| **Phase 4: Integration** | Sep-Dec 2026 | 📋 PLANNED | Extended team support, analytics, modernization foundation |

---

## Success Metrics & KPIs

### Operational Metrics
| Metric | Target | Current | Owner |
|--------|--------|---------|-------|
| OKR/KPI assignment completion rate | 100% by 5th of month | TBD (March data pending) | Đạt |
| KPI form entry time per member | <5 min (via automation) | ~15-20 min (manual) | Automation team |
| P2 evaluation completion rate | 100% by deadline | TBD | Đạt |
| Meeting attendance rate | 95%+ | Tracking needed | Đạt |
| Documentation accuracy | Zero discrepancies with actual data | TBD | Tech team |

### Quality Metrics
| Metric | Target | Current | Measurement |
|--------|--------|---------|-------------|
| OKR/KPI form validation errors | 0% | TBD | Auto-validation script |
| P2 evaluation consistency | 90%+ (scores align within 1 level across evaluators) | TBD | Quarterly review |
| Meeting notes completeness | 100% (all required sections filled) | Tracking started | Manual review |

### Efficiency Metrics
| Metric | Baseline | Target | Timeline |
|--------|----------|--------|----------|
| Monthly KPI entry time (all members) | 2 hours manual | 30 minutes automated | May 2026 |
| P2 evaluation process time | Unknown | -30% | June 2026 |
| Meeting notes organization | Scattered across folders | 100% organized by year | April 2026 |

---

## Risk Management

### Identified Risks

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|-----------|
| .env session cookies expire | OKR/KPI automation blocked | High | Monthly .env refresh, automation alert |
| my.inet.vn UI changes | okr-kpi-myinet skill breaks | Medium | Monitor for UI changes, maintain backup manual process |
| Team member turnover | Loss of P2 evaluation history, process knowledge | Low | Archive evaluations, document process in code-standards.md |
| Excel formula errors in P2 files | Inaccurate scoring | Medium | Script validation before bulk updates, peer review |
| Inconsistent meeting notes format | Hard to parse/automate | Medium | Template enforcement, quarterly validation |

---

## Dependencies & Blockers

### Current Blockers
- [ ] Verify Tuấn Anh should have P2 evaluation file or not (clarify scope)
- [ ] Confirm P2 scoring scale (1-5 or L1-L3) for documentation purposes
- [ ] Test okr-kpi-myinet automation with March meeting data (pilot run)

### External Dependencies
- **my.inet.vn availability:** Required for KPI entry automation (SLA: 99.5% uptime)
- **Browser automation library:** Requires stable Chrome/Chromium version
- **Team availability:** Meeting attendance and timely KPI/OKR assignment

### Internal Dependencies
- `.env` credentials must be refreshed monthly
- Meeting notes must be in correct format for automation to parse
- Master P2 template must preserve formulas when copied

---

## Decision Log

| Date | Decision | Rationale | Owner |
|------|----------|-----------|-------|
| 2025-Q4 | Adopt okr-kpi-myinet automation skill | Reduce manual data entry on my.inet.vn | Đạt |
| 2026-01 | Create docs/ documentation folder | Establish standards and processes | Tech team |
| 2026-03 | Schedule Performance Tracking Dashboard | Enable visibility into team progress | Đạt |
| TBD | Migrate Excel P2 to database | Modernize P2 evaluation platform | Đạt (TBD) |

---

## How to Use This Roadmap

1. **For Team Lead (Đạt):**
   - Reference "Active Initiatives" section for current month assignments
   - Use "Success Metrics" to track team performance
   - Monitor "Risk Management" section for blockers

2. **For Technical Team:**
   - Follow "Planned Improvements" for development priorities
   - Use "Timeline Summary" to plan sprints
   - Check "Dependencies & Blockers" before starting tasks

3. **For All Team Members:**
   - Review "Active Initiatives" for your assignments
   - Follow deadlines in "Timeline Summary"
   - Refer to "Code Standards" for meeting notes and P2 file formats

4. **For Future Onboarding:**
   - Start with Phase 1 (Foundation) overview
   - Review code-standards.md for conventions
   - Refer to codebase-summary.md for repository structure
