# Optional Flags — Audit & Verify

## `--audit` — So sánh OKR/KPI vs Meeting Notes

Kiểm tra OKR/KPI trên my.inet.vn có khớp với kế hoạch trong meeting notes.

**Quy trình:**
1. Đọc meeting notes tháng target từ `weekly meetings/` → trích xuất expected OKR/KPI
2. Đọc actual OKR/KPI từ my.inet.vn (agent-browser, extract text từ bảng KPI)
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
