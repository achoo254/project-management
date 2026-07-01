# Optional Flags — Audit & Verify

## `--audit` — So sánh OKR/KPI vs Meeting Notes

Kiểm tra OKR/KPI trên my.inet.vn có khớp với kế hoạch trong meeting notes.

**Quy trình:**
1. Đọc meeting notes tháng target từ `weekly meetings/` → trích xuất expected OKR/KPI
2. Đọc actual OKR/KPI từ my.inet.vn qua API `accountkpi/search` (xem mục "Đọc OKR/KPI qua API" bên dưới — ưu tiên, không cần browser)
3. So sánh:
   - ✅ **Khớp**: entry match kế hoạch
   - ⚠️ **Thiếu**: có trong meeting notes, chưa điền trên my.inet.vn
   - ❓ **Thừa**: có trên my.inet.vn, không có trong meeting notes
   - ⚡ **Sai lệch**: nội dung khác biệt (fuzzy match < 70%)
4. Không chắc chắn → `AskUserQuestion` hỏi user
5. Xuất report vào `<project-root>/plans/reports/`

**Report format:**
```markdown
# Báo cáo kiểm tra OKR/KPI — Tháng MM/YYYY
| Thành viên | Kế hoạch (meeting notes) | Thực tế (my.inet.vn) | Trạng thái |
|------------|--------------------------|----------------------|------------|
| Tên | Nội dung expected | Nội dung actual | ✅/⚠️/❓/⚡ |
```

## Đọc OKR/KPI qua API (ưu tiên — không cần browser)

OKR/KPI hiệu suất nằm ở endpoint **`accountkpi/search`** (POST, JSON, Spring pageable). ⚠️ KHÁC `kpi/search` — `kpi/search` là KPI **sales** (revenueinet / hosting-renew / vps-renew / domain / email-renew); team Công Nghệ có **0 record** ở đó.

- URL: `POST {MYBASE}/accountkpi/search` · Auth: cookie `sid`+`ssid`.
- Body: `{"account":"<email>","size":200}` — lọc theo field **`account`** (email; các field lạ bị bỏ qua). `size` = page size (mặc định 30). Trả **TẤT CẢ tháng** của account → lọc tháng ở client theo `monthStr`.
- `monthStr` = `MMYYYY` (vd tháng 6/2026 = `"062026"`, tháng 5/2026 = `"052026"`).
- Field mỗi entry: `target` (mục tiêu) · `result` (kết quả — **tự báo**) · `description` (HTML) · `note` (hay kèm link GitLab issue) · `createdAccount` · `createdDate`.

```bash
curl -s --max-time 25 -X POST "$MYBASE/accountkpi/search" \
  -H "Cookie: sid=$sid; ssid=$ssid" -H "Content-Type: application/json" \
  --data-binary '{"account":"hobv@inet.vn","size":200}'
# → lọc content[].monthStr == "062026"; strip HTML ở description
```

**Endpoint liên quan** trang KPI detail (`/account/kpi/detail/{email}`) cũng gọi — dùng để đối chiếu GitLab ngay trên portal:
`esgitlabcommit/search`, `esgitlabissue/search`, `gitlabproject/search` (portal đã index commit/issue/project theo account) · `p2evaluation/history` · `account/detailchild`.

> Tìm endpoint khi trang là Angular SPA: mở page qua CDP browser, chạy `performance.getEntriesByType('resource')` lọc `/api/` → thấy đúng endpoint thay vì đoán mò.

## `--verify-gitlab` — Kiểm tra liên kết GitLab

Kiểm tra OKR/KPI có liên quan đến issues/projects trên gitlabs.inet.vn.

**Yêu cầu:** GitLab Private Token. Thông tin thành viên và projects đọc từ `<project-root>/README.md`.

**Quy trình:**
1. Đọc `README.md` → danh sách projects mỗi thành viên
2. Lấy OKR/KPI entries từ my.inet.vn
3. Với mỗi entry, tìm trên GitLab:
   - `GET /api/v4/projects/:id/issues?search=<keyword>`
   - Check issue/MR match nội dung OKR/KPI
4. Đánh giá:
   - ✅ **Có liên kết**: tìm thấy issue/MR liên quan
   - ⚠️ **Không rõ**: không tìm thấy trực tiếp, có thể thuộc task chung
   - ❌ **Không có liên kết**: OKR/KPI không liên quan project nào
5. Không chắc chắn → `AskUserQuestion`
6. Xuất report vào `<project-root>/plans/reports/`

**Report format:**
```markdown
# Báo cáo kiểm tra GitLab — Tháng MM/YYYY
| Thành viên | OKR/KPI | GitLab Project | Issue/MR | Trạng thái |
|------------|---------|----------------|----------|------------|
| Tên | Nội dung | project-name | #123 | ✅/⚠️/❌ |
```

## Dependencies

- `agent-browser` (npm global) — browser automation
- `.env` with `sid`, `ssid` (my.inet.vn cookies), `GITLAB_PRIVATE_TOKEN`
- `README.md` chứa bảng thành viên với GitLab projects (cho `--verify-gitlab`)
