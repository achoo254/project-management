---
name: ck:okr-kpi-myinet
description: "Automate OKR/KPI entry on my.inet.vn management portal. Read monthly meeting targets, browse issues, and fill KPI forms via browser automation."
license: MIT
version: 1.0.0
argument-hint: "[month/year] or [member name]"
---

# OKR/KPI Automation - my.inet.vn

Automate reading and writing OKR/KPI on https://my.inet.vn for iNET Tech Department members.

## Team Members & KPI Links

| Name | Role | KPI URL |
|------|------|---------|
| Trinh Quoc Hoan Dat (dattqh) | Fullstack - Truong phong Cong Nghe | https://my.inet.vn/account/kpi/detail/dattqh@inet.vn |
| Bui Van Ho (hobv) | Fullstack - Truong phong Cong Nghe | https://my.inet.vn/account/kpi/detail/hobv@inet.vn |
| Nguyen Huy Hoang (hoangnh) | Fullstack - Truong phong Cong Nghe | https://my.inet.vn/account/kpi/detail/hoangnh@inet.vn |
| Dinh Tien Chuong (chuongdt) | Fullstack - Truong phong Cong Nghe | https://my.inet.vn/account/kpi/detail/chuongdt@inet.vn |
| Nguyen Dang Duc (ducnd) | Fullstack - Truong phong Cong Nghe | https://my.inet.vn/account/kpi/detail/ducnd@inet.vn |
| Tran Cong Tuan Anh (anhtct) | Fullstack - Truong phong Cong Nghe | https://my.inet.vn/account/kpi/detail/anhtct@inet.vn |

> **Add more members** by appending rows with format: `https://my.inet.vn/account/kpi/detail/{email}`

## Data Sources

1. **Monthly OKR/KPI targets**: `<project-root>/weekly meetings/` folder - read the latest file matching target month
2. **Issue details**: Retrieved from my.inet.vn issue tracker via KPI detail modal
3. **Guide reference**: `<project-root>/agent/huong dan doc - ghi KPI tren my inet.md`

## Authentication

Before any browser interaction, read `.env` file in `<project-root>` to get session cookies:

```env
# Required .env variables for my.inet.vn authentication
MY_INET_SID=<session id>
MY_INET_SSID=<secure session id>
```

**Auth flow:**
1. Read `.env` file from project root
2. Extract `MY_INET_SID` and `MY_INET_SSID` values
3. Set cookies on `my.inet.vn` domain before navigating:
   - `SID={MY_INET_SID}`
   - `SSID={MY_INET_SSID}`
4. Verify auth by loading any KPI page - if 403/redirect to login, notify user to update `.env` with fresh session values

> **How to get SID/SSID:** Login to my.inet.vn in browser → DevTools → Application → Cookies → copy SID and SSID values into `.env`

## Workflow

### Phase 1: Gather OKR/KPI Targets
1. Read the latest file in `<project-root>/weekly meetings/` folder
2. Extract each member's OKR and KPI assignments for the target month
3. Summarize: member name, task description, type (OKR or KPI)

### Phase 2: Browser Automation (per member)
Use `ck:agent-browser` or `ck:chrome-devtools` skill for browser interaction.

1. **Navigate** to member's KPI URL
2. **Click** "Them KPI" button (next to label "KPI thang MM/yyyy")
3. **KPI Modal** appears with fields:
   - Chi tiet KPI (KPI details - has "lay chi tiet cac KPI" button)
   - Muc tieu (Objective)
   - Ket qua (Result)
   - Ghi chu (Notes)
4. **Click** "lay chi tiet cac KPI" button to open issue browser
5. **In issue browser**:
   - Select "Du an" (Project) matching the member's assigned project
   - Set "Trang thai" (Status) = "Dang mo" (Open)
   - Click "Tim" (Search) and wait for results
6. **Cross-reference** issues with OKR/KPI targets from Phase 1
7. **Check** relevant issues in "Chon" (Select) column
8. **Click** "Them vao chi tiet cac KPI" to add selected issues to KPI details
9. **Read each issue link** in the KPI details to understand context
10. **Write** Muc tieu (objective) and Ket qua (result) based on issue content and meeting targets
11. **Add** Ghi chu (notes) if needed
12. **Click** "Luu lai" (Save)

### Phase 3: Verification
1. Reload member KPI page
2. Confirm new KPI entry appears for correct month
3. Report completion status per member

## Usage Examples

```
# Fill KPI for all members for current month
/okr-kpi-myinet 03/2026

# Fill KPI for specific member
/okr-kpi-myinet Ho 03/2026

# Review existing KPIs (read-only)
/okr-kpi-myinet --review 03/2026
```

## User Confirmation Rules

**CRITICAL:** Always confirm with user (via `AskUserQuestion`) in these situations:

1. **Before saving any KPI**: Show full draft (Chi tiet, Muc tieu, Ket qua, Ghi chu) and ask user to approve or edit
2. **Ambiguous issue matching**: When multiple issues could match an OKR/KPI target, list candidates and ask user to pick
3. **Missing data**: When meeting notes lack clarity on a member's target, ask user to clarify before proceeding
4. **Project selection**: If a member works on multiple projects, ask which project to select in issue browser
5. **Objective/Result wording**: When unsure how to phrase Muc tieu or Ket qua, propose options and let user choose
6. **Unexpected UI state**: If the page layout differs from expected (new buttons, changed labels), screenshot and ask user how to proceed
7. **Bulk operations**: Before filling KPI for all members, show summary table of planned actions and get confirmation

**Principle:** When in doubt, ask. Never assume. It's better to confirm once than to fix a wrong KPI entry.

## Important Notes

- **Authentication via .env**: SID/SSID cookies loaded from `.env` - no manual browser login needed
- **One KPI per OKR/KPI item**: Each OKR or KPI target from meeting notes = one KPI entry
- **Vietnamese UI**: All button labels and fields are in Vietnamese on my.inet.vn

## Error Handling

- If no issues found for a project: notify user, skip or manually input
- If member KPI link returns 403/404: skip member, report error
- If modal doesn't appear: retry once, then report to user
- If issue content is unclear: show to user and ask for objective/result text

## Weekly Meeting File Format

Expected format in `weekly meetings/MM-DD-YYYY.md`:
```markdown
- **Member Name:**
  - Task description (OKR)
  - Task description (KPI)
```

## Dependencies

- `ck:agent-browser` or `ck:chrome-devtools` for browser automation
- `.env` file with `MY_INET_SID` and `MY_INET_SSID` values for cookie-based auth
- Access to `<project-root>/weekly meetings/` folder
