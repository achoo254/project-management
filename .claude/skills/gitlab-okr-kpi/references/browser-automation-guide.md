# Browser Automation Guide — agent-browser (LEGACY fallback)

> **LEGACY** — KPI create/update (gồm field bắt buộc `difficulty`) hiện dùng **direct API** (`references/api-direct-guide.md`, curl `/accountkpi/create`|`/update`). Chỉ dùng browser khi direct API không khả dụng. Field `difficulty` **KHÔNG** set qua browser scope — luôn qua API payload.

Install if needed: `npm install -g agent-browser && agent-browser install`

## Step 1: Set cookies and navigate

```bash
# Open page first (may redirect to login - OK)
agent-browser open "https://my.inet.vn" --headed

# Set cookies using --url (NOT --domain)
# sid/ssid: load-env.sh lấy từ access-tokens.json (entry inet.vn)
source scripts/load-env.sh
agent-browser cookies set sid "$sid" --url "https://my.inet.vn"
agent-browser cookies set ssid "$ssid" --url "https://my.inet.vn"

# Navigate to member KPI page
agent-browser open "https://my.inet.vn/account/kpi/detail/{email}"
```

## Step 2: Verify page loaded

```bash
agent-browser snapshot -i
# Verify month/year dropdowns correct
# Find "Thêm KPI" button ref
```

## Step 3: Open KPI modal

```bash
# Click "Thêm KPI" (ref from snapshot)
agent-browser click @e60  # ref varies
```

## Step 4: Fill KPI form

Fields:
- **Chi tiết KPI**: Rich text editor (iframe-based, NOT regular textbox)
- **Mục tiêu** (Objective): Regular textbox
- **Kết quả** (Result): Regular textbox
- **Ghi chú** (Notes): Regular textbox
- **Độ khó/phức tạp** (Difficulty): field **BẮT BUỘC** (`S`/`M`/`L`/`XL` — S: Đơn giản · M: Trung bình · L: Phức tạp · XL: Rất phức tạp). Set qua **direct API payload** field `difficulty`, KHÔNG qua browser scope (xem `api-direct-guide.md`). Ước lượng khách quan từ code footprint, KHÔNG tự khai.
- **Đề xuất thưởng**: Checkbox (usually unchecked)

### Fill rich text editor via iframe:

```bash
agent-browser eval "(function() { var iframe = document.querySelector('iframe'); var body = iframe.contentDocument.body; body.innerHTML = '<p><strong>Title</strong></p><p>Description</p>'; body.dispatchEvent(new Event('input', {bubbles: true})); return 'done'; })()"
```

### Fill regular textboxes:

```bash
# Refs from snapshot -s ".modal-content"
agent-browser fill @e35 "Objective text"
agent-browser fill @e36 "Result text"
agent-browser fill @e37 "Notes text"
```

## Step 5: Save via Angular scope (CRITICAL)

**Do NOT click save button — unreliable. Use Angular scope:**

```bash
agent-browser eval "(function() { var el = document.querySelector('.modal-content'); var scope = angular.element(el).scope(); while (scope && !scope.save) { scope = scope.$parent; } scope.kpi.description = '<p><strong>Title</strong></p><p>Description</p>'; scope.save(); scope.$apply(); return 'saved'; })()"
```

**CRITICAL:** `scope.kpi.description` MUST be set before `save()` (iframe innerHTML does NOT sync to Angular model). **Field `difficulty` (bắt buộc) set qua direct API payload — KHÔNG qua browser scope** (xem `api-direct-guide.md`); browser save không phải path xử lý độ khó.

## Step 6: Verify save

```bash
agent-browser screenshot
# Check: KPI count increased, new row visible, status "Chờ duyệt"
```

## Step 7: Next entry

Modal auto-closes after save. For next:
1. Re-snapshot for fresh refs
2. Click "Thêm KPI" again
3. Repeat Steps 4-6

## Known Gotchas

1. `cookies set` requires `--url` NOT `--domain`
2. Rich text editor inside `<iframe>`, not contenteditable div
3. Angular model does NOT auto-sync from iframe
4. Click "Lưu lại" button unreliable → always `scope.save()` + `scope.$apply()`
5. Element refs expire after navigation → always re-snapshot
6. `agent-browser wait --idle` unreliable → use screenshot to verify
7. **Độ khó/phức tạp bắt buộc** — field mới (verified 2026-07-09), set qua **direct API payload** `difficulty` (S/M/L/XL), KHÔNG qua browser scope. Update độ khó = gọi API `/accountkpi/update`.
