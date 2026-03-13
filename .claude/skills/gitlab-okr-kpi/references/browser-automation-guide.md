# Browser Automation Guide — agent-browser

Install if needed: `npm install -g agent-browser && agent-browser install`

## Step 1: Set cookies and navigate

```bash
# Open page first (may redirect to login - OK)
agent-browser open "https://my.inet.vn" --headed

# Set cookies using --url (NOT --domain)
agent-browser cookies set sid "<jwt_token>" --url "https://my.inet.vn"
agent-browser cookies set ssid "<ssid_value>" --url "https://my.inet.vn"

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

**CRITICAL:** `scope.kpi.description` MUST be set before `save()`. Iframe innerHTML does NOT sync to Angular model.

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
