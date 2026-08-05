# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Internal project management repo for iNET Tech Department. Tracks monthly OKR/KPI targets, performance evaluations (P2+ forms), meeting minutes, and internal training material. **Not a software codebase** - primarily documentation (Markdown/HTML) plus audit reports. OKR/KPI and P2 evaluation data live on my.inet.vn, not in the repo.

## Repository Structure

- `P2_Form_BP_Cong_Nghe.xlsx` - **P2 scoring formula template only** (root, immutable). Holds weights + VLOOKUP wiring, **no evaluation levels**
- `members/` - Historical P2 workbooks (up to T5/2026). ⛔ **Never a data source** - evaluation levels live only on my.inet.vn
- `docs/` - Standards, PDR, roadmap, runbooks (`monthly-okr-p2-review-guide.md`), ADRs in `docs/decisions/`
- `okr-kpi/MM-YYYY/` - Monthly OKR+P2 audit reports, one folder per period under review (see `okr-kpi/README.md`)
- `plans/<user>/` - Per-person plans; `plans/reports/` - other reports plus the T5–T7 2026 audits
- `hop-cxo/DD-MM-YYYY/` - CXO meeting minutes + transcripts
- `dao-tao/DD-MM-YYYY/` - Internal training material (HTML slides, transcripts)
- `scripts/` - Python read-only helpers to inspect the P2 formula template (`dump_p2_*.py`, openpyxl)
- `.claude/skills/` - Local skills: `gitlab-okr-kpi` (write), `p2-monthly-okr-audit` (read-only audit)
- `.env` - my.inet.vn session cookies (`sid`/`ssid`, lowercase) + GitLab tokens - **never commit**

There is no `weekly meetings/` or `agent/` directory - both were removed. Monthly OKR/KPI data now lives on my.inet.vn, not in repo meeting notes.

## Team Members

| Tên | Username | Vai trò |
|---|---|---|
| Trịnh Quốc Hoàn Đạt | dattqh | Trưởng phòng Công Nghệ |
| Nguyễn Đăng Đức | ducnd | Frontend |
| Bùi Văn Hổ | hobv | Design System |
| Đinh Tiến Chương | chuongdt | Frontend |
| Trần Công Tuấn Anh | anhtct | AI Research |

P2 scope of dattqh: dattqh, hobv, ducnd, chuongdt. ⛔ NOT anhtct (another manager owns it).

## Key Workflows

### OKR/KPI Automation
Use `/gitlab-okr-kpi` to create/update OKR entries on https://my.inet.vn. Primary method is **direct JSON API via curl** (`POST /api/client/v1/accountkpi/{create,update,delete,search}`), authenticated with `sid`/`ssid` cookies from `.env`. Browser automation is legacy fallback only.

Two traps: `update` is **full replace** (untransmitted fields get wiped - always read-modify-write via `/search` first), and `difficulty` (`S|M|L|XL`) is mandatory in the UI so it must be set in the payload on both create and update.

### Monthly OKR + P2 Review
Runbook: `docs/monthly-okr-p2-review-guide.md`. Runs early month N+1 to review month N - cross-checks self-reported OKR/P2 against real evidence (git log, GitLab MRs/issues, prod deploy markers). Read-only audit via `/p2-monthly-okr-audit`; agent only ever saves P2 as `draft`, the manager locks final scores.

### P2+ Evaluation
Two parts on my.inet.vn: **P2-Core** (năng lực nền tảng, per role A/B/C/D → Đạt/Chưa đạt) and **P2-Delivery** (kết quả công việc: okr/quality/commitment → Chưa đạt/Đạt/Tốt). ⛔ **Levels come only from the portal** (`p2evaluation/get`) or directly from the user - never from an Excel file. Criteria + weights come from `p2config/list`; the agent only ever saves `draft`.

### Meetings & Training
Minutes and training material live in dated folders (`hop-cxo/DD-MM-YYYY/`, `dao-tao/DD-MM-YYYY/`), each holding source transcripts plus a self-contained HTML deliverable.

## Working with Excel Files

The only remaining role of `.xlsx` here is the **P2 scoring formula template**. When touching it, preserve existing formulas and sheet structure - never hard-code values into summary cells. Do **not** read evaluation levels from any workbook: they are not there, and the portal is authoritative.

## Language

Content is primarily in Vietnamese. UI labels on my.inet.vn are Vietnamese. Meeting notes and documentation are in Vietnamese.

## Đồng bộ context & ghi lý do thay đổi

Vì code clone/chạy trên nhiều máy, "lý do thay đổi" phải đi theo `git pull` — KHÔNG để trong session/memory cục bộ của Claude. Quy ước:

- **Commit message phải có "why"** trong body (conventional commit), không chỉ "what".
- **Quyết định kiến trúc / đánh đổi lâu dài** → ghi ADR vào `docs/decisions/` (copy `0000-adr-template.md`).
- **Kế hoạch feature/fix** → `plans/<user>/` (scope theo người, tránh xung đột merge — xem `plans/README.md`).
- **Đặt tên file/ADR theo nội dung**, không theo số phase / mã plan (plan đổi tên thì reference thành rác).
- **Secret**: mọi `.env.*` đã gitignore — KHÔNG commit. Lỡ lộ lên git → **rotate ngay** (`git rm --cached` không đủ vì secret vẫn trong history).
