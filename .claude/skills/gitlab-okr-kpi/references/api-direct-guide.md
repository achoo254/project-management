# my.inet.vn KPI API — Direct Guide

> Phương pháp chính: gọi API trực tiếp qua curl/fetch. KHÔNG dùng browser automation — đã loại bỏ vì chậm, fragile, phụ thuộc Angular DOM.
> Captured + verified ngày 2026-05-04 trong session tạo OKR cho dattqh tháng 05/2026.

## Endpoint summary

| Method | Path | Mục đích |
|---|---|---|
| `POST` | `/api/client/v1/accountkpi/create` | Tạo KPI entry mới |
| `POST` | `/api/client/v1/accountkpi/update` | Cập nhật entry (cần `_id`) |
| `POST` | `/api/client/v1/accountkpi/delete` | Xoá entry (cần `_id`) — verified 2026-05-29 |
| `POST` | `/api/client/v1/accountkpi/search` | List entries theo tháng |
| `POST` | `/api/client/v1/account/getsession` | Verify cookie alive |

Base URL: `https://my.inet.vn`. Tất cả là `POST` với JSON body, KHÔNG dùng query string.

## Auth

Cookie pair (cùng domain `.inet.vn`):
- `sid` — JWT, **TTL ~1 ngày** (`exp = iat + 86400`). Hết hạn → cần re-login SSO
- `ssid` — server session id, format `<random>_<accountId>`

Read qua `source scripts/load-env.sh` — helper lấy `sid`/`ssid` từ `access-tokens.json` (sổ token chung trên iCloud Drive, entry `service: "inet.vn"`, `type: "session-cookie"`), fallback file env trên iCloud Drive (variables lowercase: `sid=`, `ssid=`). Repo KHÔNG chứa file secret nào.

### Pre-flight check

```bash
source scripts/load-env.sh   # nạp $sid $ssid từ iCloud Drive
HTTP=$(curl -s -o /dev/null -w "%{http_code}" \
  -H "Cookie: sid=$sid; ssid=$ssid" \
  "https://my.inet.vn/account/kpi")
[ "$HTTP" = "200" ] || { echo "Cookie expired (HTTP $HTTP). Re-login SSO + cập nhật entry inet.vn trong access-tokens.json."; exit 1; }
```

`200` = OK. `302` / `401` = expired → user phải login lại trên browser, copy cookie mới vào entry `inet.vn` của `access-tokens.json`.

## Payload schemas

### CREATE

```json
POST /api/client/v1/accountkpi/create
{
  "description": "<p><strong>Tên KR</strong></p><p>Mô tả ngắn HTML</p>",
  "target": "Mục tiêu plain text",
  "result": "Kết quả mong đợi (có thể dài, multi-line)",
  "note": "Ghi chú",
  "difficulty": "L",
  "api": "/accountkpi/create",
  "monthStr": "052026",
  "account": "dattqh@inet.vn"
}
```

| Field | Required | Note |
|---|---|---|
| `description` | YES | Rich text HTML — render cột "Chi tiết KPI" (UI dùng `ng-bind-html`). Hỗ trợ `<p>`, `<strong>`, `<em>`, `<ul>`, `<ol>` |
| `target` | YES | Mục tiêu — **plain text only**. UI render qua Angular `ng-binding` → HTML bị escape thành raw text (verified 2026-05-29) |
| `result` | YES | Kết quả — plain text (multi-line OK qua `white-space: pre-line`). Cũng `ng-binding` → KHÔNG dùng được HTML |
| `note` | optional | Ghi chú — plain text |
| `difficulty` | YES (UI) | **Độ khó/phức tạp** — enum `"S" \| "M" \| "L" \| "XL"` (**S**: Đơn giản · **M**: Trung bình · **L**: Phức tạp · **XL**: Rất phức tạp). API accept thiếu field này (create không lỗi), nhưng UI form có nút chọn **bắt buộc** khi lưu ("Vui lòng chọn Độ khó/phức tạp của KPI") → **luôn set khi tạo VÀ khi sửa qua API**. Ước lượng khách quan từ code footprint (files/LOC/commits), KHÔNG tự khai. Verified 2026-07-03; nhãn UI S/M/L/XL verified 2026-07-09 |
| `api` | YES | Phải = `"/accountkpi/create"` (Angular SDK convention auto-set) |
| `monthStr` | YES | Format `MMYYYY` (pad 2 chữ số tháng). VD: `052026` = tháng 05/2026 |
| `account` | YES | Email người sở hữu KPI |
| `bonusMoney` | optional | Số tiền đề xuất thưởng (number). ⚠️ UI form: nếu set `bonusMoney` → form tự ghi đè `result = "Hoàn thành"` (verified từ main.js 2026-07-03). Mặc định bỏ qua |

**Convention GitLab link trong `description`:** kết thúc description bằng anchor có tiêu đề issue (KHÔNG để plain `#N`):
```html
<p><strong>GitLab:</strong> <a href="https://gitlabs.inet.vn/server-tools/cloud-panel-application/-/issues/189">#189 — Quản lý Service Linux qua Agent (systemd)</a></p>
```
Cột "Ghi chú" (`note`) để trống — metadata (plan path, effort, link) KHÔNG nhét vào note; GitLab link nằm trong description, effort nằm ở field `difficulty`.

Response: `200 OK` + JSON entry vừa tạo (chứa `_id` Mongo ObjectId 24 chars).

### UPDATE

```json
POST /api/client/v1/accountkpi/update
{
  "api": "/accountkpi/update",
  "_id": "69f84f945beb57229796ee05",
  "description": "...",
  "target": "...",
  "result": "...",
  "note": "...",
  "monthStr": "052026",
  "account": "dattqh@inet.vn"
}
```

Giống CREATE + thêm `_id` (nhớ giữ cả `difficulty` khi merge — cùng luật full-replace).

⚠️ **FULL REPLACE behavior** (verified 2026-05-29): API KHÔNG merge partial — field nào không truyền trong payload sẽ bị **set null/empty**, không giữ giá trị cũ. Luôn:
1. Gọi `/accountkpi/search` để lấy entry hiện tại trước
2. Merge field mới với field cũ trong payload
3. Mới gửi UPDATE

Anti-pattern: chỉ truyền `_id` + 1-2 field muốn đổi → các field còn lại bị wipe.

### DELETE

```json
POST /api/client/v1/accountkpi/delete
{
  "api": "/accountkpi/delete",
  "_id": "69f82792b5a99a34741ab7b4",
  "monthStr": "052026",
  "account": "ducnd@inet.vn"
}
```

| Field | Required | Note |
|---|---|---|
| `api` | YES | Phải = `"/accountkpi/delete"` |
| `_id` | YES | Mongo ObjectId của entry cần xoá |
| `monthStr` | YES | Phải khớp tháng của entry (BE check) |
| `account` | YES | Email chủ entry — phải khớp `account` của entry |

Response success: `{"status":"success","message":"Xóa thành công"}`. Hard delete, KHÔNG có undo.

> Lưu ý: path `/accountkpi/remove` KHÔNG tồn tại (timeout/no-response). Luôn dùng `/delete`.

### SEARCH

```json
POST /api/client/v1/accountkpi/search
{
  "api": "/accountkpi/search",
  "account": "dattqh@inet.vn",
  "monthStr": "052026",
  "pageSize": 1000
}
```

Response shape (Spring Data Page):
```json
{
  "first": true, "last": true,
  "number": 0, "numberOfElements": 3,
  "size": 1000, "totalElements": 3, "totalPages": 0,
  "content": [
    {
      "_id": "69f84f945beb57229796ee05",
      "description": "<p>...</p>",
      "target": "...", "result": "...", "note": "...",
      "monthStr": "052026", "account": "dattqh@inet.vn",
      "createdAccount": "...", "month": "...",
      "createdDate": "...", "status": "Chờ duyệt"
    }
  ]
}
```

Entries ở `content[]`. Field bổ sung tự sinh: `_id`, `createdAccount`, `month`, `createdDate`, `status`.

## curl recipes

### Tạo 1 KPI entry

```bash
source scripts/load-env.sh   # nạp $sid $ssid từ iCloud Drive

curl -X POST "https://my.inet.vn/api/client/v1/accountkpi/create" \
  -H "Content-Type: application/json" \
  -H "Cookie: sid=$sid; ssid=$ssid" \
  -d '{
    "description": "<p><strong>KR1: Tên</strong></p><p>Mô tả</p>",
    "target": "Mục tiêu",
    "result": "Kết quả",
    "note": "Ghi chú",
    "api": "/accountkpi/create",
    "monthStr": "052026",
    "account": "dattqh@inet.vn"
  }'
```

### List + extract IDs theo tháng

```bash
curl -s -X POST "https://my.inet.vn/api/client/v1/accountkpi/search" \
  -H "Content-Type: application/json" \
  -H "Cookie: sid=$sid; ssid=$ssid" \
  -d '{"api":"/accountkpi/search","account":"dattqh@inet.vn","monthStr":"052026","pageSize":1000}' \
  | jq '.content[] | {id: ._id, target: .target}'
```

### Update entry theo ID (read-modify-write pattern)

⚠️ API là **FULL REPLACE** — phải fetch entry hiện tại + merge trước khi update.

```bash
# 1. Fetch entry hiện tại
CURRENT=$(curl -s -X POST "https://my.inet.vn/api/client/v1/accountkpi/search" \
  -H "Content-Type: application/json" \
  -H "Cookie: sid=$sid; ssid=$ssid" \
  -d '{"api":"/accountkpi/search","account":"dattqh@inet.vn","monthStr":"052026","pageSize":1000}' \
  | jq '.content[] | select(._id == "69f84f945beb57229796ee05")')

# 2. Merge field mới + giữ field cũ
PAYLOAD=$(echo "$CURRENT" | jq '. + {
  api: "/accountkpi/update",
  target: "Mục tiêu mới"
}')

# 3. Gửi UPDATE với payload đầy đủ
curl -X POST "https://my.inet.vn/api/client/v1/accountkpi/update" \
  -H "Content-Type: application/json" \
  -H "Cookie: sid=$sid; ssid=$ssid" \
  -d "$PAYLOAD"
```

❌ ANTI-PATTERN — chỉ truyền `_id` + field muốn đổi → các field khác bị wipe null:
```bash
# KHÔNG LÀM
curl ... -d '{"api":"/accountkpi/update","_id":"...","target":"Mới"}'
```

### Delete entry theo ID

```bash
curl -X POST "https://my.inet.vn/api/client/v1/accountkpi/delete" \
  -H "Content-Type: application/json" \
  -H "Cookie: sid=$sid; ssid=$ssid" \
  -d '{
    "api": "/accountkpi/delete",
    "_id": "69f82792b5a99a34741ab7b4",
    "monthStr": "052026",
    "account": "dattqh@inet.vn"
  }'
```

⚠️ Hard delete — verify `_id` qua `/accountkpi/search` trước khi gọi. Luôn confirm với user trước khi fire.

## Bulk-create script template

`create-kpi.sh`:

```bash
#!/usr/bin/env bash
# Usage: ./create-kpi.sh <email> <monthStr> <entries.json>
# entries.json schema: array of {description, target, result, note}
set -euo pipefail

EMAIL="$1"           # dattqh@inet.vn
MONTHSTR="$2"        # 052026
ENTRIES_FILE="$3"

source scripts/load-env.sh   # nạp $sid $ssid từ iCloud Drive

# Pre-flight
HTTP=$(curl -s -o /dev/null -w "%{http_code}" -H "Cookie: sid=$sid; ssid=$ssid" "https://my.inet.vn/account/kpi")
[ "$HTTP" = "200" ] || { echo "Cookie expired (HTTP $HTTP). Re-login + cập nhật entry inet.vn trong access-tokens.json."; exit 1; }

jq -c '.[]' "$ENTRIES_FILE" | while read -r entry; do
  payload=$(jq -n \
    --arg desc "$(echo "$entry" | jq -r .description)" \
    --arg tgt  "$(echo "$entry" | jq -r .target)" \
    --arg res  "$(echo "$entry" | jq -r .result)" \
    --arg note "$(echo "$entry" | jq -r .note)" \
    --arg diff "$(echo "$entry" | jq -r .difficulty)" \
    --arg acc  "$EMAIL" \
    --arg ms   "$MONTHSTR" \
    '{description:$desc,target:$tgt,result:$res,note:$note,difficulty:$diff,api:"/accountkpi/create",monthStr:$ms,account:$acc}')
  curl -s -X POST "https://my.inet.vn/api/client/v1/accountkpi/create" \
    -H "Content-Type: application/json" \
    -H "Cookie: sid=$sid; ssid=$ssid" \
    -d "$payload" | jq -r '._id // .error // "ok"'
done
```

`entries.json` example:
```json
[
  {
    "description": "<p><strong>Tên KR</strong></p><p>Mô tả</p><p><strong>GitLab:</strong> <a href=\"https://gitlabs.inet.vn/.../issues/N\">#N — Tiêu đề issue</a></p>",
    "target": "Mục tiêu",
    "result": "Kết quả",
    "note": "",
    "difficulty": "L"
  }
]
```

## Workflow integration

Khi skill thực thi tạo OKR/KPI:

1. **Pre-flight** — `source scripts/load-env.sh`, validate cookie qua `curl HEAD /account/kpi` (200 = OK)
2. **Confirm** — show user table 3-N entries dự kiến + xin approval qua `AskUserQuestion`
3. **Execute** — loop `curl POST /accountkpi/create` cho từng entry. Capture `_id` response để verify
4. **Verify** — gọi `/accountkpi/search` đếm `totalElements` confirm số entry tăng đúng
5. **Report** — list IDs đã tạo + status

KHÔNG cần: spawn browser, set cookies, click button, inspect Angular scope, screenshot. Mọi thao tác = HTTP request thuần.

## Cookie expired recovery

Nếu pre-flight `HTTP != 200`:

1. Báo user: "Cookie my.inet.vn hết hạn (HTTP <code>). Cần re-login."
2. User mở browser → login `https://my.inet.vn` → mở DevTools (F12) → Application/Storage → Cookies → copy `sid` + `ssid` value
3. User update vào entry `service: "inet.vn"`, `type: "session-cookie"` của `access-tokens.json` (iCloud Drive):
   ```json
   "token": { "sid": "<new_jwt>", "ssid": "<new_session_id>" }
   ```
4. User báo skill tiếp tục → re-run pre-flight

KHÔNG có cách auto-refresh từ skill (SSO không expose token endpoint cho client tự refresh — phải qua browser login flow).

## Field discovery technique (khi form UI có field mới chưa document)

Form KPI là AngularJS, toàn bộ controller nằm trong 1 bundle **`https://my.inet.vn/public/dist/js/main.js`** (~1.6MB, KHÔNG minify tên field). Cách tìm tên field payload từ label UI:

```bash
curl -s -H "Cookie: sid=$sid; ssid=$ssid" "https://my.inet.vn/public/dist/js/main.js" -o /tmp/main.js
grep -oE '.{1500}<label-text-trên-UI>' /tmp/main.js   # đọc code quanh validation/binding
```

VD field `difficulty` tìm được qua grep `"Vui lòng chọn Độ khó"` → thấy `l.difficultyLevels=["S","M","L","XL"]` + `a.kpi.difficulty`. Cách này đã dùng verify 2026-07-03.

## Semantics ghi nhận

- **`status` values**: search trả `"waiting"` (UI hiển thị badge "Chờ duyệt"). `waiting` = chờ quản lý duyệt, KHÔNG phải chưa làm — công việc đã hoàn thành.
- **Effort-weighted OKR**: điểm OKR chấm theo effort-weighted completion. `difficulty` ước lượng **khách quan từ code footprint** (đếm files/LOC/commits của module liên quan), không tin effort tự khai. Ngưỡng "Tốt" = hoàn thành cao VÀ ≥1 deliverable stretch (L–XL).
- **`bonusMoney`** (resolved 2026-07-03): number field; UI form logic `kpi.bonusMoney && (kpi.result = "Hoàn thành")` — set bonusMoney qua form sẽ ghi đè result. Qua API thuần thì không bị (logic nằm ở client), nhưng tránh set để khỏi lệch hành vi UI.

## Unresolved

1. **Permission check** — tạo/sửa/xoá cho email khác chính mình chưa test. Có thể yêu cầu role admin/manager.
2. **Approve workflow** — `status: "waiting"` có endpoint approve riêng nhưng chưa capture (manager-only feature).
