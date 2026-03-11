---
name: ck:okr-kpi-myinet
description: "Automate OKR/KPI entry on my.inet.vn management portal. Read monthly meeting targets, browse issues, and fill KPI forms via browser automation."
license: MIT
version: 1.1.0
argument-hint: "[month/year] [member name] [source: meeting notes or plan report]"
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

## Data Sources

1. **Monthly OKR/KPI targets**: `<project-root>/weekly meetings/` folder OR plan reports in `<project-root>/plans/reports/`
2. **Issue details**: Retrieved from my.inet.vn issue tracker via KPI detail modal

## Authentication

Read `.env` file in `<project-root>` to get session cookies:

```env
# .env cookie names are lowercase
sid=<jwt token>
ssid=<secure session id>
```

**CRITICAL - Cookie names are lowercase `sid` and `ssid` in .env file.**

## Workflow

### Phase 1: Gather OKR/KPI Targets
1. Read source file (meeting notes from `weekly meetings/` or plan report)
2. Extract member's OKR/KPI assignments for target month
3. Present summary table to user for confirmation before proceeding
4. Ask user which entries to create (all or subset)
5. **All Vietnamese text must use diacritics (có dấu)**, except English technical terms

### Phase 2: Browser Automation (agent-browser)

**IMPORTANT: Use `agent-browser` (npm package). Install if needed: `npm install -g agent-browser && agent-browser install`**

#### Step 1: Set cookies and navigate
```bash
# Open any page first (will redirect to login - that's OK)
agent-browser open "https://my.inet.vn" --headed

# Set cookies using --url parameter (NOT --domain)
agent-browser cookies set sid "<jwt_token>" --url "https://my.inet.vn"
agent-browser cookies set ssid "<ssid_value>" --url "https://my.inet.vn"

# Navigate to member KPI page
agent-browser open "https://my.inet.vn/account/kpi/detail/{email}"
```

#### Step 2: Verify page loaded
```bash
agent-browser snapshot -i
# Verify month/year dropdowns show correct values (03 selected, 2026 selected)
# Find "Thêm KPI" button ref
```

#### Step 3: Open KPI modal
```bash
# Click "Thêm KPI" button (find ref from snapshot)
agent-browser click @e60  # ref varies - use snapshot to find
```

#### Step 4: Fill KPI form (CRITICAL - exact method)

The KPI modal has these fields:
- **Chi tiết KPI**: Rich text editor (iframe-based, NOT a regular textbox)
- **Mục tiêu** (Objective): Regular textbox
- **Kết quả** (Result): Regular textbox
- **Ghi chú** (Notes): Regular textbox
- **Đề xuất thưởng**: Checkbox (usually unchecked)

**Fill the rich text editor (Chi tiết KPI) via iframe JavaScript:**
```bash
agent-browser eval "(function() { var iframe = document.querySelector('iframe'); var body = iframe.contentDocument.body; body.innerHTML = '<p><strong>Title</strong></p><p>Description</p>'; body.dispatchEvent(new Event('input', {bubbles: true})); return 'done'; })()"
```

**Fill regular textboxes using snapshot refs:**
```bash
# After snapshot -i of modal, fields are typically:
# @e35 = Mục tiêu, @e36 = Kết quả, @e37 = Ghi chú
# (verify with snapshot -s ".modal-content")
agent-browser fill @e35 "Objective text"
agent-browser fill @e36 "Result text"
agent-browser fill @e37 "Notes text"
```

#### Step 5: Save via Angular scope (CRITICAL - do NOT click save button)

**The save button click does NOT reliably work. MUST use Angular scope directly:**

```bash
agent-browser eval "(function() { var el = document.querySelector('.modal-content'); var scope = angular.element(el).scope(); while (scope && !scope.save) { scope = scope.$parent; } scope.kpi.description = '<p><strong>Title</strong></p><p>Description</p>'; scope.save(); scope.$apply(); return 'saved'; })()"
```

**CRITICAL:** The `scope.kpi.description` MUST be set in the Angular model before calling `save()`. The iframe innerHTML alone does NOT sync to Angular model. Always set `description` explicitly in the save script.

#### Step 6: Verify save
```bash
agent-browser screenshot
# Check: Tổng KPI count increased, new row visible in KPI table
# Status should show "Chờ duyệt"
```

#### Step 7: Repeat for next KPI entry
After successful save, modal auto-closes. For next entry:
1. Re-snapshot to get fresh refs
2. Click "Thêm KPI" again
3. Repeat Steps 4-6

### Phase 3: Verification & Cleanup
1. Take final screenshot showing all KPI entries
2. Report completion: total entries created, all statuses
3. Close browser: `agent-browser close`

## User Confirmation Rules

**CRITICAL:** Always confirm with user (via `AskUserQuestion`):

1. **Before starting**: Show planned KPI entries table, ask which to create
2. **Before first save**: Show filled form screenshot, ask to approve or edit
3. **Content language**: All Vietnamese text must use diacritics (có dấu)
4. **Ambiguous matching**: When multiple issues match, list candidates for user to pick

## Error Handling

- **Cookie auth fails** (redirect to login): Notify user to update `.env` with fresh sid/ssid
- **Save button doesn't work**: Use Angular scope method (Step 5 above)
- **Iframe content not syncing**: Always set `scope.kpi.description` in save script
- **Refs expired after page change**: Re-run `snapshot -i` to get fresh refs
- **Modal doesn't appear**: Wait 2s, retry click once, then report to user

## Known Gotchas

1. `agent-browser cookies set` requires `--url` NOT `--domain` parameter
2. Rich text editor is inside an `<iframe>`, not a contenteditable div
3. Angular model does NOT auto-sync from iframe - must set `scope.kpi.description` manually
4. Click on "Lưu lại" button is unreliable - always use `scope.save()` + `scope.$apply()`
5. Element refs expire after page navigation - always re-snapshot after any page change
6. `agent-browser wait --idle` doesn't work reliably - skip it, just take screenshot to verify

## Dependencies

- `agent-browser` (npm global package) for browser automation
- `.env` file with `sid` and `ssid` values (lowercase) for cookie-based auth
