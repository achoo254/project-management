# project-management

## Quản Lý Dự Án & Đánh Giá Hiệu Suất - iNET Tech Department

Hệ thống quản lý nội bộ theo dõi **OKR/KPI hàng tháng**, **đánh giá hiệu suất (P2+)**, **biên bản họp** và **đào tạo nội bộ** cho bộ phận Công Nghệ.

### Cấu Trúc Chính

- **`members/{năm}/T{tháng}/`** - Biểu mẫu đánh giá P2 theo từng thành viên, chia theo kỳ (vd `members/2026/T5/`)
- **`docs/`** - Tài liệu hướng dẫn, quy chuẩn, lộ trình; ADR trong `docs/decisions/`
- **`okr-kpi/MM-YYYY/`** - Báo cáo audit OKR + P2 theo từng kỳ (xem [`okr-kpi/README.md`](./okr-kpi/README.md))
- **`plans/<user>/`** - Kế hoạch theo từng người; **`plans/reports/`** - báo cáo khác + audit kỳ T5–T7/2026
- **`hop-cxo/DD-MM-YYYY/`** - Biên bản họp CXO kèm transcript
- **`dao-tao/DD-MM-YYYY/`** - Tài liệu đào tạo nội bộ (slide HTML, transcript)
- **`scripts/`** - Script Python đọc/dump mẫu công thức P2 (`dump_p2_*.py`, chỉ đọc)
- **`P2_Form_BP_Cong_Nghe.xlsx`** - **Chỉ là mẫu công thức tính P2** (ở root, không sửa trực tiếp) — không chứa mức đánh giá
- **`members/`** - Workbook P2 lịch sử (đến T5/2026). ⛔ Không dùng làm nguồn dữ liệu
- **`.env`** - Cookie my.inet.vn (`sid`/`ssid`) + token GitLab (bí mật, không commit)

Dữ liệu OKR/KPI **và mức đánh giá P2** đều nằm trên **my.inet.vn**, không lưu trong repo. Repo này chỉ chứa tài liệu, mẫu công thức P2 và báo cáo đối chiếu.

### Quy Trình Chính

1. **Khai OKR đầu tháng** → nhập trên my.inet.vn theo [Quy tắc viết nội dung OKR](./docs/quy-tac-viet-noi-dung-okr.html)
2. **Tự động hóa OKR/KPI** → skill `/gitlab-okr-kpi` gọi API my.inet.vn trực tiếp (curl)
3. **Đánh giá P2+ cuối tháng** → điền mức trực tiếp trên my.inet.vn (P2-Core + P2-Delivery); agent chỉ lưu `draft`, quản lý khoá điểm cuối
4. **Review đầu tháng sau** → đối chiếu tự đánh giá với bằng chứng thật, xuất báo cáo HTML vào `okr-kpi/MM-YYYY/`

### Tài Liệu Tham Khảo

- **[Quy tắc viết nội dung OKR](./docs/quy-tac-viet-noi-dung-okr.html)** - Điền trường nào, định dạng gì, cách chấm và lỗi thường gặp
- **[Review OKR + P2 hằng tháng](./docs/monthly-okr-p2-review-guide.md)** - Runbook đối chiếu tự đánh giá vs thực tế + xuất báo cáo HTML
- **[Tổng Quan Dự Án](./docs/project-overview-pdr.md)** - Mục tiêu, quy trình, KPI thành công
- **[Tóm Tắt Codebase](./docs/codebase-summary.md)** - Cấu trúc repo, mô tả file
- **[Quy Chuẩn Code](./docs/code-standards.md)** - Quy ước đặt tên, định dạng tài liệu
- **[Lộ Trình Dự Án](./docs/project-roadmap.md)** - Trạng thái hiện tại, cải tiến sắp tới
- **[Cấu Hình Môi Trường](./docs/env-configuration-guide.md)** - Biến môi trường của các dự án liên quan

### Thành Viên Nhóm

| Tên | Username | Vai Trò | KPI Link |
|-----|----------|---------|----------|
| Trịnh Quốc Hoàn Đạt | dattqh | Trưởng phòng Công Nghệ | [KPI](https://my.inet.vn/account/kpi/detail/dattqh@inet.vn) |
| Nguyễn Đăng Đức | ducnd | Frontend | [KPI](https://my.inet.vn/account/kpi/detail/ducnd@inet.vn) |
| Bùi Văn Hổ | hobv | Design System | [KPI](https://my.inet.vn/account/kpi/detail/hobv@inet.vn) |
| Đinh Tiến Chương | chuongdt | Frontend | [KPI](https://my.inet.vn/account/kpi/detail/chuongdt@inet.vn) |
| Trần Công Tuấn Anh | anhtct | AI Research | [KPI](https://my.inet.vn/account/kpi/detail/anhtct@inet.vn) |

Phạm vi đánh giá P2 của dattqh: **dattqh, hobv, ducnd, chuongdt**. Không bao gồm `anhtct` (quản lý khác phụ trách).

### Bắt Đầu Nhanh

**Thêm OKR cho tháng này:**
1. Đọc [quy tắc viết nội dung OKR](./docs/quy-tac-viet-noi-dung-okr.html) - đặc biệt phần định dạng trường và cách chọn độ khó
2. Cập nhật cookie `sid`/`ssid` trong `.env` nếu đã hết hạn (sống khoảng một ngày)
3. Chạy skill: `/gitlab-okr-kpi 08/2026`
4. Xác nhận entry trên my.inet.vn

**Cập nhật đánh giá P2:**
1. Mở form trên my.inet.vn: `/account/p2/evaluation?account={email}&period=YYYY-MM`
2. Điền mức P2-Core (A/B/C/D) và P2-Delivery (OKR / Chất lượng / Cam kết)
3. Đối chiếu `total`/`grade` server tính với công thức trong runbook
4. Lưu **nháp**; điểm cuối do quản lý khoá. ⛔ Không điền vào file Excel — Excel chỉ còn giữ mẫu công thức

**Review OKR + P2 tháng trước:**
1. Theo runbook [monthly-okr-p2-review-guide.md](./docs/monthly-okr-p2-review-guide.md)
2. Chạy `/p2-monthly-okr-audit` (chỉ đọc, không sửa/khóa điểm)
3. Báo cáo HTML xuất vào `okr-kpi/MM-YYYY/` theo kỳ được review - dữ liệu nhân sự, để local, không publish

---

*Lần cập nhật: 05/08/2026 | Trưởng phòng: Đạt*
