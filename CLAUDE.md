# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Internal project management repo for iNET Tech Department. Tracks project status, staff allocation, performance evaluations (P2 forms), monthly OKR/KPI targets, and weekly meeting notes. **Not a software codebase** - primarily data files (Excel) and documentation (Markdown).

## Repository Structure

- `members/` - Per-member P2 evaluation Excel files (`P2_Form_BP_Cong_Nghe - {Name}.xlsx`)
- `P2_Form_BP_Cong_Nghe.xlsx` - Master P2 evaluation template
- `weekly meetings/` - Monthly meeting notes with OKR/KPI assignments (format: `DD-MM-YYYY.md`)
- `agent/` - Agent guides (e.g., KPI automation instructions for my.inet.vn)
- `scripts/` - Python utility scripts for Excel manipulation and P2 form processing
- `.claude/` - Local Claude skills (e.g., `okr-kpi-myinet` for KPI automation)
- `.env` - Session cookies for my.inet.vn authentication (SID/SSID) - **never commit**

## Team Members

Dat (dattqh), Duc, Ho, Chuong, Tuan Anh

## Key Workflows

### OKR/KPI Automation
Use `/okr-kpi-myinet` skill to automate KPI entry on https://my.inet.vn. Reads meeting notes from `weekly meetings/`, authenticates via `.env` cookies, and fills KPI forms via browser automation.

### P2 Evaluation
Excel-based performance evaluation system. Master template at root, member-specific forms in `members/`. Python scripts in `scripts/` handle bulk updates, formula application, and data migration across sheets.

### Weekly Meetings
Meeting notes follow format: `DD-MM-YYYY.md` with member names and their OKR/KPI assignments for the month.

## Working with Excel Files

Scripts use `openpyxl` for Excel manipulation. When modifying P2 forms, preserve existing formulas and sheet structure. Each member file mirrors the master template with individual data.

## Language

Content is primarily in Vietnamese. UI labels on my.inet.vn are Vietnamese. Meeting notes and documentation are in Vietnamese.
