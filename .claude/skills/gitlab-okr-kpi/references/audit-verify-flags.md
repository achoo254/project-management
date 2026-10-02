# Optional Flags — Audit & Verify

## `--audit` — Đối chiếu OKR/KPI đã khai vs kỳ vọng

Kiểm tra OKR/KPI trên my.inet.vn có khớp với những gì đã cam kết cho tháng đó.

⚠️ **Không có nguồn "meeting notes" trong repo.** Folder `weekly meetings/` đã bị xoá; nội dung cũ đã stale. Baseline lấy theo thứ tự ưu tiên:

1. **User chỉ định trực tiếp** danh sách OKR kỳ vọng cho tháng (hỏi qua `AskUserQuestion` nếu chưa có).
2. **Plan trong repo** — `plans/<user>/<slug>/` nếu công việc tháng đó có plan.
3. **GitLab** — issue/milestone gán cho thành viên trong tháng (xem `--verify-gitlab`).

Nếu cần audit đầy đủ (đối chiếu OKR + P2 với bằng chứng git/GitLab/production), dùng skill **`p2-monthly-okr-audit`** thay vì flag này — flag này chỉ so entry vs danh sách kỳ vọng.

**Quy trình:**
1. Xác định baseline kỳ vọng theo thứ tự ưu tiên ở trên
2. Đọc actual OKR/KPI từ my.inet.vn qua `accountkpi/search` (xem mục dưới)
3. So sánh:
   - ✅ **Khớp**: entry match kỳ vọng
   - ⚠️ **Thiếu**: có trong kỳ vọng, chưa khai trên my.inet.vn
   - ❓ **Thừa**: có trên my.inet.vn, không có trong kỳ vọng
   - ⚡ **Sai lệch**: nội dung khác biệt (fuzzy match < 70%)
4. Không chắc chắn → `AskUserQuestion` hỏi user
5. Xuất report HTML vào `<project-root>/okr-kpi/MM-YYYY/` (kỳ được review, xem `okr-kpi/README.md`)

**Report format:**
```markdown
# Báo cáo kiểm tra OKR/KPI — Tháng MM/YYYY
| Thành viên | Kỳ vọng (nguồn) | Thực tế (my.inet.vn) | Trạng thái |
|------------|-----------------|----------------------|------------|
| Tên | Nội dung expected + nguồn | Nội dung actual | ✅/⚠️/❓/⚡ |
```

## Đọc OKR/KPI qua API

OKR/KPI hiệu suất nằm ở endpoint **`accountkpi/search`** (POST, JSON, Spring pageable). ⚠️ KHÁC `kpi/search` — `kpi/search` là KPI **sales** (revenueinet / hosting-renew / vps-renew / domain / email-renew); team Công Nghệ có **0 record** ở đó.

- URL: `POST https://my.inet.vn/api/client/v1/accountkpi/search` · Auth: cookie `sid`+`ssid`
- Body: `{"api":"/accountkpi/search","account":"<email>","monthStr":"MMYYYY"}`
- `monthStr` = `MMYYYY` (vd tháng 6/2026 = `"062026"`, tháng 5/2026 = `"052026"`)

⛔ **Bẫy phân trang — sai ở đây là kết luận sai cả report.** Endpoint phân trang **cứng ở 30 entry/trang và BỎ QUA tham số `size`/`pageSize`**. Luôn gửi kèm `monthStr` để backend lọc theo tháng; **KHÔNG** lấy một trang rồi lọc client-side theo `monthStr` — người có nhiều entry lịch sử (vd dattqh `totalElements=58`) sẽ mất sạch entry của tháng cần xem và bị kết luận sai là "không khai OKR". Luôn đối chiếu `totalElements` trả về với số dòng thực nhận trước khi tin kết quả; nếu lệch, phân trang tiếp qua `page`.

**Field mỗi entry:** `target` (mục tiêu, plain text) · `result` (kết quả — **tự báo**, plain text) · `description` (rich text HTML, chứa anchor GitLab issue) · `difficulty` (`S`/`M`/`L`/`XL`) · `note` (theo convention hiện tại **để trống** — entry cũ có thể còn link GitLab ở đây) · `createdAccount` · `createdDate` · `status` (`waiting` = chờ quản lý duyệt, **không phải** chưa làm).

```bash
source scripts/load-env.sh   # nạp $sid $ssid từ iCloud Drive

curl -s --max-time 25 -X POST "https://my.inet.vn/api/client/v1/accountkpi/search" \
  -H "Cookie: sid=$sid; ssid=$ssid" -H "Content-Type: application/json" \
  --data-binary '{"api":"/accountkpi/search","account":"hobv@inet.vn","monthStr":"062026"}' \
  | jq '{totalElements, received: (.content|length), entries: [.content[] | {id:._id, target, difficulty, status}]}'
# → so totalElements vs received; strip HTML ở description khi hiển thị
```

**Endpoint liên quan** trang KPI detail (`/account/kpi/detail/{email}`) cũng gọi — dùng để đối chiếu GitLab ngay trên portal:
`esgitlabcommit/search`, `esgitlabissue/search`, `gitlabproject/search` (portal đã index commit/issue/project theo account) · `p2evaluation/history` · `account/detailchild`.

> Tìm endpoint khi trang là Angular SPA: mở page qua CDP browser, chạy `performance.getEntriesByType('resource')` lọc `/api/` → thấy đúng endpoint thay vì đoán mò.

## `--verify-gitlab` — Kiểm tra liên kết GitLab

Kiểm tra OKR/KPI có liên quan đến issues/projects trên gitlabs.inet.vn.

**Yêu cầu:** GitLab token trong file env trên iCloud (`GITLABS_ACCESS_TOKEN`), nạp qua `source scripts/load-env.sh`.

**Bản đồ repo ↔ thành viên:** đọc từ `docs/monthly-okr-p2-review-guide.md` mục 4 (không phải `README.md` — README chỉ có bảng thành viên + link KPI, không có mapping repo). GitLab user IDs: dattqh=5, ducnd=27, chuongdt=26, hobv=17.

**Quy trình:**
1. Đọc bản đồ repo ↔ thành viên từ runbook
2. Lấy OKR/KPI entries từ my.inet.vn (mục trên)
3. Với mỗi entry, ưu tiên đọc anchor GitLab có sẵn trong `description`; nếu không có thì tìm:
   - `GET /api/v4/projects/:id/issues?search=<keyword>`
   - `GET /api/v4/users/:id/events` (⚠️ **phân trang** — không tin trang đầu)
4. Đánh giá:
   - ✅ **Có liên kết**: tìm thấy issue/MR liên quan, đã closed/merged trong tháng
   - ⚠️ **Không rõ**: không tìm thấy trực tiếp, có thể thuộc task chung
   - ❌ **Không có liên kết**: OKR/KPI không liên quan project nào
5. Không chắc chắn → `AskUserQuestion`
6. Xuất report HTML vào `<project-root>/okr-kpi/MM-YYYY/` (kỳ được review, xem `okr-kpi/README.md`)

**Deadline khi đánh giá:** OKR tháng N phải landed (merge main / issue close) **≤ ngày cuối tháng N**. Landed sang tháng sau = trễ. "Đã build lên production" không phải bằng chứng — cần tag release, `last-modified` của bundle prod, hoặc pipeline `deploy` thành công.

**Report format:**
```markdown
# Báo cáo kiểm tra GitLab — Tháng MM/YYYY
| Thành viên | OKR/KPI | GitLab Project | Issue/MR | Landed | Trạng thái |
|------------|---------|----------------|----------|--------|------------|
| Tên | Nội dung | project-name | #123 | DD/MM | ✅/⚠️/❌ |
```

## Dependencies

- `sid`, `ssid` (cookie my.inet.vn — TTL ≈ 1 ngày) từ `access-tokens.json` (sổ token chung trên iCloud Drive, entry `service: "inet.vn"`, `type: "session-cookie"`) và `GITLABS_ACCESS_TOKEN` từ file env trên iCloud Drive, nạp qua `source scripts/load-env.sh`
- `curl` + `jq` — cả hai flag chạy bằng HTTP thuần, **không cần browser**
- `docs/monthly-okr-p2-review-guide.md` — bản đồ repo ↔ thành viên + ngưỡng đánh giá (cho `--verify-gitlab`)
