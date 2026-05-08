# Project Overview & Product Development Requirements

## Project Purpose

Internal project management system for iNET Tech Department. Centralized tracking of staff performance evaluations, project assignments, OKR/KPI targets, and team synchronization across monthly initiatives.

## Organization

**Department:** iNET Tech Department
**Location:** Internal management portal (my.inet.vn)
**Team Members:** Đạt (Trưởng phòng), Đức, Hổ, Chương, Tuấn Anh

## Key Processes

### 1. Monthly OKR/KPI Planning
- **Frequency:** Monthly meetings (held weekly, assignments published monthly)
- **Output:** Meeting notes in `weekly meetings/` folder (format: `DD-MM-YYYY.md`)
- **Content:** Per-member task assignments with OKR (strategic objectives) and KPI (key performance indicators)
- **Automation:** okr-kpi-myinet skill reads meeting notes and fills KPI forms on my.inet.vn via browser automation

### 2. Performance Evaluation (P2)
- **Tool:** Excel-based evaluation forms
- **Master Template:** `P2_Form_BP_Cong_Nghe.xlsx` (root directory)
- **Member Forms:** `members/` directory - one file per team member
- **Content:** Structured evaluation criteria. Formula: `P2+ Tổng = (P2-Core × A) + (P2-Delivery × B)`
- **Note:** Tuấn Anh được đánh giá P2 riêng (không trong repo này)
- **Automation:** Python scripts (openpyxl) for bulk updates and formula management

### 3. Weekly Team Synchronization
- **Cadence:** Weekly meetings
- **Format:** Markdown notes with attendees, accomplishments, training sessions, action items
- **Storage:** `weekly meetings/` folder organized by month (2025, 2026 subdirectories)

## Workflows & Dependencies

### OKR/KPI Automation Flow
```
Meeting Notes (weekly meetings/)
           ↓
Read targets (okr-kpi-myinet skill)
           ↓
Extract OKR/KPI per member
           ↓
Authenticate to my.inet.vn (.env cookies)
           ↓
Fill KPI forms via browser automation
           ↓
Verify entries on my.inet.vn
```

**Key Input:** `.env` file contains session cookies (MY_INET_SID, MY_INET_SSID) for my.inet.vn authentication.

### P2 Evaluation Flow
```
Master template (root)
           ↓
Copy to member-specific file
           ↓
Update via Python scripts or manual entry
           ↓
Review and finalize scores
           ↓
Archive or distribute results
```

## Current State (March 2026)

### Active Projects & Assignments

| Member | OKRs | KPIs |
|--------|------|------|
| Hổ | 100% Design System | — |
| Tuấn Anh | Cải thiện quy trình xử lý lạm dụng tự động | Cải thiện hệ thống số hóa tài liệu |
| Đức | Nâng cấp vFirewall v2 | Hoàn thiện FE CloudPanel |
| Chương | — | Hoàn thiện service hosting |
| Đạt (Trưởng phòng) | Team leadership & OKR/KPI oversight | — |

### Training Topics (March 2026)
- Week 1: Brainstorming App Desktop Localman (Postman-like)
- Week 2: Chatbot – Tuấn Anh
- Week 3: TBD (Chương)
- Week 4: Design System – Hổ

## Success Metrics

1. **OKR/KPI Completion Rate:** % of assigned OKRs/KPIs completed on schedule
2. **KPI Form Accuracy:** % of entries correctly filled on my.inet.vn matching meeting targets
3. **P2 Evaluation Timeliness:** All member evaluations completed by deadline
4. **Meeting Attendance:** Consistent weekly participation from core team
5. **Documentation Accuracy:** Meeting notes accurately reflect decisions and assignments

## Constraints & Assumptions

- **Authentication:** Session cookies (SID/SSID) must be manually updated when sessions expire
- **Browser Automation:** okr-kpi-myinet skill requires stable browser connection to my.inet.vn
- **Excel Files:** No real-time sync; manual updates or Python script runs required
- **Vietnamese UI:** All forms and portals use Vietnamese language; documentation targets Vietnamese-speaking team

## Risk Assessment

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Expired .env cookies | Automation blocked | Monthly .env refresh reminder |
| Excel formula errors | P2 scoring inaccurate | Script validation before bulk updates |
| Missed meeting deadlines | OKR/KPI data stale | Automated reminders, weekly sync |
| Browser UI changes on my.inet.vn | Automation breaks | Manual monitoring, update okr-kpi-myinet skill |

## Next Steps (Priority Order)

1. Automate OKR/KPI entry → reduce manual form-filling time
2. Simplify P2 evaluation process → create reusable scoring templates
3. Archive historical meeting notes → improve searchability
4. Create P2 evaluation dashboard → track team performance trends
5. Document P2 evaluation criteria → train new evaluators
