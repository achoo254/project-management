# Codebase Summary

## Repository Overview

**Type:** Internal Project Management Repository (Non-Software)
**Purpose:** Centralized tracking of iNET Tech Department staff performance, project assignments, and OKR/KPI targets
**Language:** Vietnamese (team communication)
**Platform:** Windows (local machine) + my.inet.vn portal (web)

## Directory Structure

```
project-management/
├── README.md                           # Basic project description (Vietnamese)
├── CLAUDE.md                           # Claude Code AI instructions
├── .env                                # Session cookies for my.inet.vn auth (git-ignored)
├── .gitignore                          # Git ignore rules
├── P2_Form_BP_Cong_Nghe.xlsx          # Master P2 evaluation template (root)
│
├── docs/                               # Documentation (this folder)
│   ├── project-overview-pdr.md        # Project purpose, team, workflows
│   ├── codebase-summary.md            # This file
│   ├── code-standards.md              # Conventions & standards
│   └── project-roadmap.md             # Current state & improvements
│
├── agent/                              # Documentation for manual processes
│   └── huong dan doc - ghi KPI tren my inet.md  # Guide for KPI entry (Vietnamese)
│
├── members/                            # Per-member P2 evaluation files
│   ├── P2_Form_BP_Cong_Nghe - Chuong.xlsx
│   ├── P2_Form_BP_Cong_Nghe - Dat.xlsx
│   ├── P2_Form_BP_Cong_Nghe - Duc.xlsx
│   ├── P2_Form_BP_Cong_Nghe - Ho.xlsx
│   └── P2_Form_BP_Cong_Nghe - Hoang.xlsx
│
├── weekly meetings/                    # Team meeting notes
│   ├── 2025/                          # Historical 2025 notes (9 files)
│   │   ├── 01-12-2025.md
│   │   ├── 03-11-2025.md
│   │   ├── 08-12-2025.md
│   │   ├── 10-11-2025.md
│   │   ├── 15-12-2025.md
│   │   ├── 17-11-2025.md
│   │   ├── 22-12-2025.md
│   │   ├── 24-11-2025.md
│   │   └── 29-12-2025.md
│   ├── 2026/                          # (Future: organize 2026 notes here)
│   ├── 02-02-2026.md                  # Feb 2026 meeting
│   ├── 05-01-2026.md                  # Jan 2026 meeting
│   ├── 12-01-2026.md                  # Jan 2026 meeting
│   ├── 19-01-2025.md                  # Jan 2025 meeting
│   ├── 26-01-2026.md                  # Jan 2026 meeting
│   └── 02-03-2026.md                  # Mar 2026 meeting (current)
│
├── scripts/                            # Python automation scripts (openpyxl)
│
└── .claude/                            # Claude AI custom tools
    └── okr-kpi-myinet/                # OKR/KPI automation skill
        └── SKILL.md                    # Browser automation guide for KPI entry
```

## File Descriptions

### Core Configuration
| File | Purpose | Owner |
|------|---------|-------|
| `README.md` | Project title & brief description | Team Lead |
| `CLAUDE.md` | AI agent instructions | Team Lead |
| `.env` | Session cookies for my.inet.vn (SECRET) | Team Lead |
| `.gitignore` | Git exclusions (.env, .idea, .vscode) | Repository Admin |

### Documentation
| File | Purpose | Audience |
|------|---------|----------|
| `docs/project-overview-pdr.md` | Project goals, team, workflows, success metrics | Team Lead, Developers |
| `docs/codebase-summary.md` | Repository structure & file descriptions (this file) | All team members |
| `docs/code-standards.md` | Conventions: file naming, meeting format, Excel structure | All team members |
| `docs/project-roadmap.md` | Current initiatives, planned improvements, timeline | Team Lead, Developers |

### Evaluation Data
| File | Purpose | Format | Owner |
|------|---------|--------|-------|
| `P2_Form_BP_Cong_Nghe.xlsx` | Master P2 evaluation template (scoring, formulas) | Excel | Team Lead |
| `members/*.xlsx` | Per-member evaluation forms (5 members) | Excel | Individual/Lead |

### Meeting Notes
| File | Period | Purpose | Format |
|------|--------|---------|--------|
| `weekly meetings/2025/` | Nov-Dec 2025 | Historical team meetings | Markdown |
| `weekly meetings/2026/` | Jan-Mar 2026 | Current team meetings | Markdown |
| (Root level) | Jan-Mar 2026 | Recent meetings (migration pending) | Markdown |

### Automation Tools
| File | Purpose | Language | Status |
|------|---------|----------|--------|
| `.claude/okr-kpi-myinet/SKILL.md` | OKR/KPI automation for my.inet.vn | Browser JS + Claude AI | Active |
| `agent/huong dan doc - ghi KPI tren my inet.md` | Manual KPI entry guide (Vietnamese) | Documentation | Reference |
| `scripts/` | Python openpyxl scripts for P2 bulk updates | Python 3.x | Active |

## Data Flow

### OKR/KPI Entry Flow
```
1. Team holds weekly meeting
2. Lead documents assignments in weekly meetings/DD-MM-YYYY.md
   - Format: Per-member list with OKR and KPI tasks
3. OKR/KPI Automation (okr-kpi-myinet skill):
   - Read weekly meetings file for target month
   - Extract member names + task descriptions
   - Authenticate to my.inet.vn using .env cookies
   - Fill KPI forms via browser automation
   - Include relevant GitHub issue links
4. Verification:
   - Check my.inet.vn KPI dashboard
   - Confirm all entries correctly entered
```

### P2 Evaluation Flow
```
1. Start of evaluation period
2. Lead copies master P2_Form_BP_Cong_Nghe.xlsx to members/
3. Fill member-specific data (name, period, scores)
4. Optional: Run Python script for bulk formula updates
5. Collect completed forms from all 5 members
6. Archive completed evaluations
7. Use results for performance review discussions
```

### Meeting Notes Organization
```
Current state: Some files at root, some in 2025/ subfolder
Desired state: Organize all by calendar year (2025/, 2026/, etc.)
File naming: DD-MM-YYYY.md (e.g., 02-03-2026.md = March 2, 2026)
```

## Team Members & Roles

| Name | Email | Role | P2 File |
|------|-------|------|---------|
| Trịnh Quốc Hoàn Đạt | dattqh@inet.vn | Trưởng phòng Công Nghệ (Tech Lead) | P2_Form_BP_Cong_Nghe - Dat.xlsx |
| Nguyễn Đăng Đức | duc@inet.vn | Frontend/Backend Dev | P2_Form_BP_Cong_Nghe - Duc.xlsx |
| (Hổ) | ho@inet.vn | Designer/System Designer | P2_Form_BP_Cong_Nghe - Ho.xlsx |
| Đinh Tiến Chương | chuong@inet.vn | Backend Dev | P2_Form_BP_Cong_Nghe - Chuong.xlsx |
| Nguyễn Huy Hoàng | hoang@inet.vn | DevOps/System Admin | P2_Form_BP_Cong_Nghe - Hoang.xlsx |
| Tuấn Anh | tuananh@inet.vn | Backend/Process Specialist | P2 riêng (đánh giá riêng, không trong repo này) |

## External Dependencies

### Authentication
- **my.inet.vn:** Team performance portal
- **Credentials:** Session cookies stored in `.env` (MY_INET_SID, MY_INET_SSID)
- **Refresh Frequency:** Monthly (sessions expire)

### Tools & Platforms
- **Browser:** Chrome/Chromium for okr-kpi-myinet automation
- **Python:** openpyxl library for Excel manipulation (scripts archived)
- **Office:** Excel for P2 evaluation forms
- **Documentation:** Markdown + Claude AI

## Key Metrics & Tracking

### OKR/KPI Targets (March 2026)
- **OKRs:** 5 strategic objectives assigned
- **KPIs:** 5 key performance indicators assigned
- **Completion Target:** End of March 2026
- **Tracking Method:** my.inet.vn KPI detail pages

### P2 Evaluations
- **Evaluation Period:** Quarterly (typical)
- **Number of Evaluees:** 5 members
- **Scoring Formula:** P2+ Tổng = (P2-Core × A) + (P2-Delivery × B)
- **Formula Dependencies:** Cell references for summary calculations

## Notes & Observations

1. **File Organization:** Meeting notes split between root and 2025/ subfolder - should consolidate to calendar year structure (2025/, 2026/, etc.)
2. **Scripts Directory:** Empty since recent commit - previously contained openpyxl Excel automation scripts
3. **Excel Structure:** Master template (P2_Form_BP_Cong_Nghe.xlsx) contains formulas; member files should preserve formulas
4. **Automation Status:** okr-kpi-myinet skill is primary automation tool; manual guides also exist in agent/
5. **Tuấn Anh:** Được đánh giá P2 riêng (ngoài repo này), không cần thêm file trong `members/`

## Glossary

| Term | Vietnamese | Meaning |
|------|------------|---------|
| OKR | Mục tiêu & Kết quả Chính | Objectives & Key Results (strategic quarterly targets) |
| KPI | Chỉ số hiệu suất | Key Performance Indicator (measurable performance metric) |
| P2 | Đánh giá P2 | Performance evaluation form (BP_Cong_Nghe = Tech Department) |
| Trưởng phòng | — | Department Head / Team Lead |
| my.inet.vn | — | iNET internal management portal |
| Chi tiết KPI | — | KPI Details (issue links & supporting documentation) |
| Mục tiêu | — | Objective |
| Kết quả | — | Result / Outcome |
| Ghi chú | — | Notes |
