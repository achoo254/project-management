# P2+ Evaluation Automation — my.inet.vn

Đánh giá P2+ hằng tháng cho thành viên. Agent điền mức đánh giá **P2-Core** + **P2-Delivery** rồi **lưu nháp (`status="draft"`)** để quản lý review. Agent **KHÔNG bao giờ** submit/duyệt — chỉ draft.

- Base API: `https://my.inet.vn/api/client/v1`
- Page: `https://my.inet.vn/account/p2/evaluation?account={SSO}&period={YYYY-MM}`
- Auth: Cookie `sid` + `ssid` (đọc `.env`, tên lowercase).
- `{SSO}` = email tài khoản (vd `dattqh@inet.vn`); `{period}` = `YYYY-MM` (vd `2026-05`).

## Cấu trúc đánh giá

### P2-Core — Năng lực nền tảng (theo TỪNG role)
| Key | Hạng mục | Trọng số | Giá trị hợp lệ |
|-----|----------|----------|----------------|
| A | Năng lực kỹ thuật | 30% | `"Đạt"` / `"Chưa đạt"` |
| B | Ownership & trách nhiệm | 30% | `"Đạt"` / `"Chưa đạt"` |
| C | DevOps & vận hành | 15% | `"Đạt"` / `"Chưa đạt"` |
| D | AI Agent & cải tiến | 25% | `"Đạt"` / `"Chưa đạt"` |

- Chỉ **2 mức**: `Đạt` hoặc `Chưa đạt`.
- `scores.core` được keyed theo **TÊN ROLE**: `{"Fullstack": {"A": ..., "B": ..., "C": ..., "D": ...}}`. Nhiều role → nhiều key (mỗi role 1 bộ A/B/C/D).

### P2-Delivery — Kết quả công việc (CHUNG, không theo role)
| Key | Tiêu chí | Trọng số | Giá trị (hệ số) |
|-----|----------|----------|-----------------|
| okr | Mức độ hoàn thành OKR | 40% | `"Chưa đạt"` (0.8) / `"Đạt"` (1) / `"Tốt"` (1.2) |
| quality | Chất lượng kết quả | 35% | `"Chưa đạt"` (0.8) / `"Đạt"` (1) / `"Tốt"` (1.2) |
| commitment | Cam kết & tiến độ | 25% | `"Chưa đạt"` (0.8) / `"Đạt"` (1) / `"Tốt"` (1.2) |

- Gửi **label KHÔNG kèm hệ số**: `"Tốt"`, KHÔNG phải `"Tốt (1.2)"`.
- `scores.delivery` là object phẳng: `{"okr": ..., "quality": ..., "commitment": ...}`.

> ⚠️ **Chuỗi giá trị phải khớp CHÍNH XÁC** option trên form (dấu + hoa/thường). Cả Core và Delivery dùng `"Chưa đạt"` (đ thường). Nếu `save` báo lỗi giá trị, đọc lại `<select>` option trên page để lấy đúng chuỗi rồi gửi lại.

## Nguồn mức đánh giá

**Mặc định: chỉ điền khi có sẵn dữ liệu.**
1. **User cung cấp** → dùng đúng giá trị user gửi (ưu tiên tuyệt đối).
2. **User không cung cấp** → dùng `AskUserQuestion` hỏi từng hạng mục. **KHÔNG tự suy diễn.**
3. **Phân tích GitLab (chỉ khi user yêu cầu RÕ)** — vd "phân tích GitLab để đánh giá P2 cho X": dùng Mode 1 (GitLab API) lấy commits/MRs/issues/pipelines/reviews trong `period`, đối chiếu rubric (link "Xem" trên page) → đề xuất mức + bằng chứng → **luôn cho user xác nhận trước khi save**.

## Quy trình (API-first, dùng `curl`)

### Bước 1 — Load baseline (GET)
Mỗi người có roles khác nhau → **PHẢI** lấy trước.

```bash
# Lấy sid/ssid từ .env (tôn trọng privacy hook)
curl -s "https://my.inet.vn/api/client/v1/p2evaluation/compute?account=${ACCOUNT}&period=${PERIOD}" \
  -H "Cookie: sid=${SID}; ssid=${SSID}" \
  -H "Accept: application/json"
```

Trả về: `roles` (kèm `weight`), `department`, `scores` hiện tại, và metadata khác.
**Giữ nguyên TOÀN BỘ field; chỉ sửa `scores`.** Nếu GET thiếu `department`/`period`, lấy từ tham số URL đã dùng / page.

> Nếu GET trả HTML/redirect login thay vì JSON → cookie hết hạn (xem Error Handling) hoặc endpoint chặn curl → dùng fallback browser fetch() ở cuối file.

### Bước 2 — Dựng `scores`
Theo "Nguồn mức đánh giá" ở trên. Điền đủ 4 hạng mục core (mỗi role) + 3 tiêu chí delivery.

### Bước 3 — Compute (validate điểm — NÊN làm)
Ghi body ra file UTF-8 (an toàn tiếng Việt trên Windows) rồi gửi bằng `--data-binary @file`:

```bash
# body-compute.json (UTF-8, no BOM)
{
  "api": "/p2evaluation/compute",
  "roles": [{"role": "Fullstack", "weight": 1}],
  "scores": {
    "core": {"Fullstack": {"A": "Đạt", "B": "Đạt", "C": "Đạt", "D": "Đạt"}},
    "delivery": {"okr": "Tốt", "quality": "Đạt", "commitment": "Tốt"}
  }
}
```

```bash
curl -s -X POST "https://my.inet.vn/api/client/v1/p2evaluation/compute" \
  -H "Cookie: sid=${SID}; ssid=${SSID}" \
  -H "Content-Type: application/json" \
  --data-binary @body-compute.json
```

→ Trả điểm tính toán (theo trọng số). **Hiển thị cho user xác nhận trước khi save.**

### Bước 4 — Lưu nháp (POST save, `status="draft"`)

```bash
# body-save.json (UTF-8, no BOM) — account/period/department/reason/roles lấy từ baseline Bước 1
{
  "api": "/p2evaluation/save",
  "account": "dattqh@inet.vn",
  "period": "2026-05",
  "department": "technology",
  "reason": "",
  "roles": [{"role": "Fullstack", "weight": 1}],
  "scores": {
    "core": {"Fullstack": {"A": "Đạt", "B": "Đạt", "C": "Đạt", "D": "Đạt"}},
    "delivery": {"okr": "Tốt", "quality": "Đạt", "commitment": "Tốt"}
  },
  "status": "draft"
}
```

```bash
curl -s -X POST "https://my.inet.vn/api/client/v1/p2evaluation/save" \
  -H "Cookie: sid=${SID}; ssid=${SSID}" \
  -H "Content-Type: application/json" \
  --data-binary @body-save.json
```

**Quy tắc save (BẮT BUỘC):**
- `status` **LUÔN** = `"draft"`. Không bao giờ `"submit"`/`"approved"`/giá trị khác.
- `account`, `period`, `department`, `roles`, `reason` + **mọi field khác** lấy từ baseline (Bước 1) → **GIỮ NGUYÊN**. Chỉ `scores` là phần mới.
- Xóa file body tạm sau khi xong (chứa dữ liệu nhân sự).

### Bước 5 — Verify + report
1. Đọc response `save` → xác nhận thành công.
2. (Optional) GET lại Bước 1 → kiểm tra `scores` + `status="draft"` đã ghi.
3. Báo cáo: điểm tổng (core/delivery), trạng thái `draft`, nhắc quản lý vào my.inet.vn review.

## Fallback — Browser fetch() (khi curl bị chặn CSRF/WAF)

Mở page evaluation trong session đã đăng nhập, chạy `fetch()` từ chính origin (browser tự gắn cookie):

```javascript
// Chạy qua claude-in-chrome javascript_tool hoặc agent-browser eval, trên tab my.inet.vn
await fetch('/api/client/v1/p2evaluation/save', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  credentials: 'include',
  body: JSON.stringify({ /* body-save như trên, status: "draft" */ })
}).then(r => r.json());
```

## Error Handling

- GET/POST trả HTML hoặc 302/401 → cookie hết hạn → báo user cập nhật `sid`/`ssid` trong `.env`.
- 403/CSRF → dùng fallback browser fetch().
- Giá trị mức không hợp lệ → đọc lại `<select>` option trên page lấy đúng chuỗi (dấu/hoa-thường).
- Role trong baseline khác kỳ vọng → dùng đúng role + weight từ GET, không hardcode.
- Tiếng Việt lỗi dấu trong request → đảm bảo body file là UTF-8 (no BOM) và dùng `--data-binary @file`.
