# P2+ Evaluation Automation — my.inet.vn

Đánh giá P2+ hằng tháng cho thành viên. Agent điền mức đánh giá **P2-Core** + **P2-Delivery** rồi **lưu nháp (`draft`)** để quản lý review. Agent **KHÔNG bao giờ** "Trình duyệt" (submit) hay "Khoá kết quả" — chỉ draft.

- Base API: `https://my.inet.vn/api/client/v1` — **tất cả endpoint là POST, JSON, RPC-style** (có field `api` trong body). KHÔNG có GET.
- Page: `https://my.inet.vn/account/p2/evaluation?account={SSO}&period={YYYY-MM}`
- Auth: Cookie `sid` + `ssid` — nạp qua `source scripts/load-env.sh` (helper đọc từ `access-tokens.json` (sổ token chung trên iCloud Drive, entry `service: "inet.vn"`, `type: "session-cookie"`); tên biến lowercase).
- `{SSO}` = email (vd `chuongdt@inet.vn`); `{period}` = `YYYY-MM` (vd `2026-05`).

## Cấu trúc đánh giá

### Vai trò (roles) — gửi CHÍNH XÁC text, kể cả dấu cách
Mỗi người có vai trò khác nhau. Giá trị `role` hợp lệ (đúng như dropdown trên page):
| role (gửi nguyên văn) | Ghi chú |
|-----------------------|---------|
| `"Design System"` | **có dấu cách** — KHÔNG đổi thành `DesignSystem`/`design_system` |
| `"Backend"` | |
| `"Frontend"` | |
| `"Fullstack"` | |

- Chuỗi `role` dùng **đồng thời** ở 2 nơi, phải **trùng khớp tuyệt đối** (case + dấu cách):
  1. Trong `roles[]`: `{"role": "Design System", "weight": 1}`
  2. Làm **key** trong `scores.core`: `"scores":{"core":{"Design System":{"A":...}}}`
- `weight` ∈ [0–1]. Một người có thể nhiều vai trò ("Thêm vai trò"); **tổng trọng số vai trò = 1**.
- **Luôn lấy `roles` + tên role + weight từ baseline `/get`** (hoặc dropdown trên page) — KHÔNG tự gõ lại, tránh sai dấu cách/hoa thường.

### P2-Core — Năng lực nền tảng (theo TỪNG role)
| Key | Hạng mục | Giá trị hợp lệ |
|-----|----------|----------------|
| A | Năng lực kỹ thuật | `"Đạt"` / `"Chưa đạt"` |
| B | Ownership & trách nhiệm | `"Đạt"` / `"Chưa đạt"` |
| C | DevOps & vận hành | `"Đạt"` / `"Chưa đạt"` |
| D | AI Agent & cải tiến | `"Đạt"` / `"Chưa đạt"` |

- Chỉ **2 mức**: `Đạt` / `Chưa đạt` (đ thường). `Đạt` = full điểm hạng mục, `Chưa đạt` = 0.
- ⚠️ **Trọng số A/B/C/D KHÁC theo role** — KHÔNG hardcode. VD Fullstack = 30/30/15/25; Frontend = 30/25/10/35. Điểm do server tính (xem `computed`).
- `scores.core` keyed theo **TÊN ROLE** và **chứa TẤT CẢ role** hệ thống biết; role không active để rỗng `{"A":"","B":"","C":"","D":""}`. **Bảo toàn nguyên** structure, chỉ điền role active.

### P2-Delivery — Kết quả công việc (CHUNG, không theo role)
| Key | Tiêu chí | Giá trị (hệ số) |
|-----|----------|-----------------|
| okr | Mức độ hoàn thành OKR | `"Chưa đạt"` (×0.8) / `"Đạt"` (×1) / `"Tốt"` (×1.2) |
| quality | Chất lượng kết quả | `"Chưa đạt"` / `"Đạt"` / `"Tốt"` |
| commitment | Cam kết & tiến độ | `"Chưa đạt"` / `"Đạt"` / `"Tốt"` |

- Gửi **label KHÔNG kèm hệ số**: `"Tốt"`, KHÔNG phải `"Tốt (1.2)"`.
- `scores.delivery` phẳng: `{"okr":..., "quality":..., "commitment":...}`.

> ⚠️ Chuỗi giá trị phải khớp CHÍNH XÁC (dấu + hoa/thường). Nếu lỗi, đọc `<select>` option trên page.

## Nguồn mức đánh giá

⛔ **KHÔNG có nguồn Excel.** File `.xlsx` trong repo (kể cả `members/{năm}/T{tháng}/`) chỉ giữ **mẫu công thức tính P2** — không chứa mức đánh giá nào. Không đọc, không suy diễn từ đó.

Thứ tự nguồn:

1. **User cung cấp trực tiếp** (nguồn CHÍNH) → dùng đúng giá trị user gửi.
2. **`selfScores` đã có trên portal** — khi việc cần làm là chấm official theo đúng self, hoặc để hiển thị đối chiếu. Lấy từ `p2evaluation/get`; role lấy từ `roles[]` cùng response, KHÔNG tự gõ lại.
3. **User không cung cấp** → `AskUserQuestion` hỏi từng hạng mục (A/B/C/D + okr/quality/commitment), **KHÔNG tự suy diễn**.
4. **Phân tích GitLab (chỉ khi user yêu cầu RÕ)**: dùng Mode 1 lấy commits/MRs/issues/pipelines trong `period`, đối chiếu tiêu chí lấy từ `p2config/list` → đề xuất mức + bằng chứng → **luôn cho user xác nhận trước khi save**.

⛔ **KHÔNG làm P2 cho `anhtct`** (Trần Công Tuấn Anh) — do quản lý khác phụ trách. Phạm vi P2 của dattqh: dattqh, hobv, ducnd, chuongdt.

**Giá trị hợp lệ gửi API** (khớp chính xác dấu + hoa/thường): Core `"Đạt"` / `"Chưa đạt"` · Delivery `"Chưa đạt"` / `"Đạt"` / `"Tốt"` — gửi label KHÔNG kèm hệ số.

## API contract (đã verify thực tế)

### 1. `/p2evaluation/get` — load baseline + check quyền
Body: `{"account": "<email>", "period": "<YYYY-MM>"}`

- **Chưa có record** → `{"__permission": "self" | "manager"}` (chỉ quyền, chưa có roles/scores).
- **Đã có record** → object đầy đủ:
```json
{"_id":"...","account":"chuongdt@inet.vn","period":"2026-05","department":"technology",
 "roles":[{"role":"Frontend","weight":1}],
 "scores":{"core":{"Fullstack":{"A":"","B":"","C":"","D":""},
                   "Frontend":{"A":"Đạt","B":"Đạt","C":"Đạt","D":"Đạt"}},
           "delivery":{"okr":"Đạt","quality":"Đạt","commitment":"Tốt"}},
 "evidence":{},"notes":"","status":"draft","evaluator":"dattqh@inet.vn",
 "computed":{"core":{"subScores":{...},"total":1},"delivery":{...},"total":1.025,"grade":"Tốt",
             "coreWeight":0.5,"deliveryWeight":0.5,"primaryRole":"Frontend"},
 "__permission":"manager"}
```

**`__permission` quyết định luồng save:**
- `"manager"` (quản lý đánh giá cấp dưới) → dùng `/save` (`scores` + `status`).
- `"self"` (tự đánh giá) → dùng `/saveself` (`selfScores` + `selfStatus`).

> Nếu record CHƯA tồn tại (get chỉ trả `__permission`) → roles chưa biết. Lấy role từ: badge role hiển thị trên page P2-Core ("Frontend trọng số 1"), hoặc hỏi user. `department` mặc định `"technology"` (phòng Công Nghệ).

### 2. `/p2evaluation/compute` — tính điểm (validate, nên làm trước khi save)
Body (ghi ra file UTF-8, gửi `--data-binary @file`):
```json
{"api":"/p2evaluation/compute",
 "roles":[{"role":"Frontend","weight":1}],
 "scores":{"core":{"Frontend":{"A":"Đạt","B":"Đạt","C":"Đạt","D":"Đạt"}},
           "delivery":{"okr":"Đạt","quality":"Đạt","commitment":"Tốt"}}}
```
Response:
```json
{"core":{"subScores":{"A":0.3,"B":0.25,"C":0.1,"D":0.35},"total":1},
 "delivery":{"subScores":{"okr":0.4,"quality":0.35,"commitment":0.3},"total":1.05},
 "total":1.025,"grade":"Tốt","coreWeight":0.5,"deliveryWeight":0.5,"primaryRole":"Frontend"}
```
- Thiếu `roles` → lỗi `{"status":"error","message":"Trường roles không được để trống"}`.
- **Hiển thị `total` + `grade` cho user xác nhận trước khi save.**

### 3a. `/p2evaluation/save` — MANAGER lưu nháp (`__permission="manager"`)
Body — **bảo toàn account/period/department/reason/roles + FULL scores.core (mọi role) từ baseline**, chỉ sửa role active + delivery:
```json
{"api":"/p2evaluation/save",
 "account":"chuongdt@inet.vn","period":"2026-05","department":"technology","reason":"",
 "roles":[{"role":"Frontend","weight":1}],
 "scores":{"core":{"Fullstack":{"A":"","B":"","C":"","D":""},
                   "Frontend":{"A":"Đạt","B":"Đạt","C":"Đạt","D":"Đạt"}},
           "delivery":{"okr":"Đạt","quality":"Đạt","commitment":"Tốt"}},
 "status":"draft"}
```

### 3b. `/p2evaluation/saveself` — SELF lưu nháp (`__permission="self"`)
Khác `/save`: `scores`→`selfScores`, `status`→`selfStatus`. Giữ `reason` nếu baseline có.
```json
{"api":"/p2evaluation/saveself",
 "account":"dattqh@inet.vn","period":"2026-05","department":"technology",
 "roles":[{"role":"Fullstack","weight":1}],
 "selfScores":{"core":{"Fullstack":{"A":"Đạt","B":"Đạt","C":"Đạt","D":"Đạt"}},
               "delivery":{"okr":"Tốt","quality":"Đạt","commitment":"Tốt"}},
 "selfStatus":"draft"}
```

**Quy tắc save (BẮT BUỘC):**
- `status`/`selfStatus` **LUÔN** = `"draft"`. KHÔNG bao giờ submit/khoá.
- Bảo toàn mọi field không liên quan đánh giá (`account`, `period`, `department`, `reason`, `roles`, `notes`, `evidence`...) từ baseline `/get`. Chỉ `scores`/`selfScores` là mới.
- KHÔNG cần gửi `_id`/`computed`/`history`/`evaluator` (server tự quản lý).
- Xóa file body tạm sau khi xong (chứa dữ liệu nhân sự).

## Quy trình curl (đầy đủ)
```bash
# 1. Nạp sid/ssid từ iCloud Drive
source scripts/load-env.sh   # nạp $sid $ssid từ iCloud Drive
COOKIE="sid=${sid}; ssid=${ssid}"; BASE="https://my.inet.vn/api/client/v1"

# 2. Load baseline + quyền
echo '{"account":"chuongdt@inet.vn","period":"2026-05"}' > /tmp/get.json
curl -s --max-time 25 -X POST "$BASE/p2evaluation/get" \
  -H "Cookie: $COOKIE" -H "Content-Type: application/json" --data-binary @/tmp/get.json

# 3. compute (validate) → 4. save / saveself (status=draft) — body từ file UTF-8
curl -s --max-time 25 -X POST "$BASE/p2evaluation/save" \
  -H "Cookie: $COOKIE" -H "Content-Type: application/json" --data-binary @/tmp/save.json
```

> **Lưu ý:** gửi nhiều request dồn dập gây **502 "page temporarily unavailable"** (rate-limit). Gọi tuần tự, `--max-time 25`, có khoảng nghỉ.

## Verify sau save
1. Đọc response `save`/`saveself` → xác nhận thành công.
2. Gọi lại `/get` → kiểm tra `scores` + `status="draft"` + `computed.grade` đã ghi.
3. Báo cáo: điểm tổng (`computed.total`), `grade`, trạng thái `draft`, nhắc quản lý vào my.inet.vn review.

## Error Handling
- `/get`,`/compute`,`/save` trả HTML hoặc 302/401 → cookie hết hạn → báo user cập nhật `sid`/`ssid` trong entry `inet.vn` của `access-tokens.json`.
- 502 "temporarily unavailable" → server quá tải do gọi dồn → đợi ~15s, gọi lại tuần tự.
- `{"status":"error","message":"Trường roles không được để trống"}` → thiếu `roles` trong body compute.
- Giá trị mức không hợp lệ → đọc `<select>` option trên page lấy đúng chuỗi (dấu/hoa-thường).
- Tiếng Việt lỗi dấu → body file UTF-8 (no BOM) + `--data-binary @file`.
