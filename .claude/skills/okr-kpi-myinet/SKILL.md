---
name: ck:okr-kpi-myinet
description: "Automate OKR/KPI entry on my.inet.vn management portal. Read monthly meeting targets, browse issues, and fill KPI forms via browser automation."
license: MIT
version: 1.3.0
argument-hint: "[month/year] [member] [--audit] [--verify-gitlab]"
---

# OKR/KPI Automation - my.inet.vn

Automate reading and writing OKR/KPI on https://my.inet.vn for iNET Tech Department members.

## Team Members & KPI Links

| Name | Role | KPI URL |
|------|------|---------|
| Trinh Quoc Hoan Dat (dattqh) | Truong phong Cong Nghe | https://my.inet.vn/account/kpi/detail/dattqh@inet.vn |
| Bui Van Ho (hobv) | Design System | https://my.inet.vn/account/kpi/detail/hobv@inet.vn |
| Nguyen Huy Hoang (hoangnh) | Backend | https://my.inet.vn/account/kpi/detail/hoangnh@inet.vn |
| Dinh Tien Chuong (chuongdt) | Frontend | https://my.inet.vn/account/kpi/detail/chuongdt@inet.vn |
| Nguyen Dang Duc (ducnd) | Frontend | https://my.inet.vn/account/kpi/detail/ducnd@inet.vn |
| Tran Cong Tuan Anh (anhtct) | AI Research | https://my.inet.vn/account/kpi/detail/anhtct@inet.vn |

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

### Phase 0: Pre-flight Validation

**CRITICAL:** Chạy tất cả checks bên dưới TRƯỚC khi bắt đầu Phase 1. Nếu thiếu bất kỳ thông tin nào, dùng `AskUserQuestion` để hỏi user bổ sung. Thông tin bổ sung chỉ dùng tạm trong session hiện tại, KHÔNG ghi vào file.

#### Check 1: Cookie my.inet.vn
1. Đọc `.env` tại `<project-root>`
2. Kiểm tra có cả `sid` và `ssid` hay không
3. Nếu thiếu → `AskUserQuestion`:
   - Header: "Cookie my.inet.vn"
   - Question: "Thiếu cookie xác thực my.inet.vn. Bạn lấy từ Browser DevTools → Application → Cookies → my.inet.vn"
   - Options: (a) "Nhập sid và ssid" — user nhập qua text, (b) "Bỏ qua" — dừng skill
4. Nếu có cookie → validate bằng: `curl -s -o /dev/null -w "%{http_code}" -H "Cookie: sid=<sid>; ssid=<ssid>" https://my.inet.vn/account/kpi`
   - HTTP 200 = OK, tiếp tục
   - HTTP 302/401 = cookie hết hạn → hỏi user nhập lại như bước 3

#### Check 2: GitLab Authentication (gitlabs.inet.vn)
1. Kiểm tra GitLab access: `curl -s -H "PRIVATE-TOKEN: <token>" https://gitlabs.inet.vn/api/v4/user`
2. Token lấy từ `.env` key `GITLAB_PRIVATE_TOKEN` (nếu có)
3. Nếu không có token hoặc auth fail → `AskUserQuestion`:
   - Header: "GitLab Auth"
   - Question: "Cần Private Token để truy cập issues trên gitlabs.inet.vn. Tạo tại: Settings → Access Tokens → scope: read_api"
   - Options: (a) "Nhập Private Token" — user nhập token, (b) "Bỏ qua GitLab" — không link issues, chỉ điền KPI text
4. Nếu user chọn bỏ qua → tiếp tục nhưng bỏ qua bước link issues từ GitLab

#### Check 3: Xác nhận thành viên
1. Parse tên thành viên từ arguments hoặc meeting notes
2. So khớp với bảng Team Members ở trên (khớp theo tên, username, hoặc email)
3. Nếu không khớp → `AskUserQuestion`:
   - Header: "Thành viên"
   - Question: "Không tìm thấy thành viên '{tên}'. Chọn đúng người:"
   - Options: liệt kê tất cả thành viên trong bảng (tối đa 4, nếu >4 thì gộp nhóm)
4. Nếu argument không chỉ định thành viên → `AskUserQuestion` hỏi chọn thành viên nào cần điền KPI

#### Check 4: Tìm Meeting Notes
1. Parse tháng/năm từ arguments (vd: `03/2026`)
2. Tìm file meeting notes: `weekly meetings/DD-MM-YYYY.md` matching tháng target
3. Nếu không tìm thấy → `AskUserQuestion`:
   - Header: "Meeting Notes"
   - Question: "Không tìm thấy ghi chép cho tháng {MM/YYYY}. Chọn nguồn dữ liệu:"
   - Options: (a) "Chỉ đường dẫn file" — user nhập path, (b) "Dùng plan report" — tìm trong `plans/reports/`, (c) "Nhập thủ công" — user tự ghi OKR/KPI entries

#### Kết quả Pre-flight
Sau khi tất cả checks pass, hiển thị bảng tóm tắt:
```
✓ Cookie my.inet.vn: hợp lệ
✓ GitLab: đã xác thực (hoặc: bỏ qua)
✓ Thành viên: Đức, Hoàng (2 người)
✓ Meeting notes: weekly meetings/02-03-2026.md
```
Tiếp tục Phase 1.

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

## Optional Steps (Flags)

### `--audit` — So sánh OKR/KPI vs Meeting Notes

Kiểm tra nội dung OKR/KPI trên my.inet.vn có khớp với kế hoạch trong meeting notes không.

**Quy trình:**
1. Đọc meeting notes tháng target từ `weekly meetings/` → trích xuất expected OKR/KPI mỗi thành viên
2. Đọc actual OKR/KPI từ my.inet.vn (dùng agent-browser, extract text từ bảng KPI)
3. So sánh từng entry:
   - ✅ **Khớp**: entry trên my.inet.vn match với kế hoạch
   - ⚠️ **Thiếu**: có trong meeting notes nhưng chưa điền trên my.inet.vn
   - ❓ **Thừa**: có trên my.inet.vn nhưng không có trong meeting notes
   - ⚡ **Sai lệch**: nội dung khác biệt đáng kể (fuzzy match < 70%)
4. Khi không chắc chắn → dùng `AskUserQuestion` hỏi user xác nhận
5. Xuất report markdown vào `<project-root>/plans/reports/`

**Report format:**
```markdown
# Báo cáo kiểm tra OKR/KPI — Tháng MM/YYYY
| Thành viên | Kế hoạch (meeting notes) | Thực tế (my.inet.vn) | Trạng thái |
|------------|--------------------------|----------------------|------------|
| Tên | Nội dung expected | Nội dung actual | ✅/⚠️/❓/⚡ |
```

### `--verify-gitlab` — Kiểm tra liên kết GitLab

Kiểm tra OKR/KPI có liên quan đến issues/projects trên gitlabs.inet.vn không.

**Yêu cầu:** GitLab Private Token (Check 2 trong Pre-flight). Thông tin thành viên và GitLab projects đọc từ `<project-root>/README.md` (bảng Thành Viên Nhóm).

**Quy trình:**
1. Đọc `README.md` → lấy danh sách projects mỗi thành viên tham gia
2. Với mỗi thành viên, lấy OKR/KPI entries từ my.inet.vn
3. Với mỗi entry, kiểm tra trên GitLab:
   - Tìm issues liên quan trong projects của thành viên: `GET /api/v4/projects/:id/issues?search=<keyword>`
   - Kiểm tra có issue/MR nào match với nội dung OKR/KPI không
4. Đánh giá:
   - ✅ **Có liên kết**: tìm thấy issue/MR liên quan trên GitLab
   - ⚠️ **Không rõ**: không tìm thấy issue trực tiếp, có thể thuộc task chung
   - ❌ **Không có liên kết**: OKR/KPI không liên quan đến bất kỳ project nào
5. Khi không chắc chắn → dùng `AskUserQuestion` hỏi user xác nhận
6. Xuất report markdown vào `<project-root>/plans/reports/`

**Report format:**
```markdown
# Báo cáo kiểm tra GitLab — Tháng MM/YYYY
| Thành viên | OKR/KPI | GitLab Project | Issue/MR | Trạng thái |
|------------|---------|----------------|----------|------------|
| Tên | Nội dung | project-name | #123 | ✅/⚠️/❌ |
```

## Dependencies

- `agent-browser` (npm global package) for browser automation
- `.env` file with `sid` and `ssid` values (lowercase) for cookie-based auth
- `README.md` chứa bảng thành viên với vai trò và GitLab projects (cho `--verify-gitlab`)
