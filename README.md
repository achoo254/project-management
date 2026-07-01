# project-management

## Quản Lý Dự Án & Đánh Giá Hiệu Suất - iNET Tech Department

Hệ thống quản lý nội bộ theo dõi **OKR/KPI hàng tháng**, **đánh giá hiệu suất (P2)**, và **phối hợp nhóm** cho bộ phận Công Nghệ.

### Cấu Trúc Chính

- **`weekly meetings/`** - Ghi chép các cuộc họp hàng tuần với phân công OKR/KPI
- **`members/`** - Các biểu mẫu đánh giá P2 theo từng thành viên
- **`docs/`** - Tài liệu hướng dẫn, quy chuẩn và lộ trình dự án
- **`P2_Form_BP_Cong_Nghe.xlsx`** - Mẫu đánh giá P2 chính
- **`.env`** - Cookie xác thực my.inet.vn (bí mật, không commit)

### Quy Trình Chính

1. **Họp hàng tháng** → Ghi chép trong `weekly meetings/DD-MM-YYYY.md`
2. **Tự động hóa OKR/KPI** → Skill `okr-kpi-myinet` điền vào my.inet.vn
3. **Đánh giá P2** → Cập nhật file Excel theo từng thành viên
4. **Theo dõi tiến độ** → Dashboard hiệu suất (sắp tới)

### Tài Liệu Tham Khảo

- **[Tổng Quan Dự Án](./docs/project-overview-pdr.md)** - Mục tiêu, quy trình, KPI thành công
- **[Tóm Tắt Codebase](./docs/codebase-summary.md)** - Cấu trúc repo, mô tả file
- **[Quy Chuẩn Code](./docs/code-standards.md)** - Quy ước đặt tên, định dạng ghi chép
- **[Lộ Trình Dự Án](./docs/project-roadmap.md)** - Trạng thái hiện tại, cải tiến sắp tới
- **[Review OKR + P2 hằng tháng](./docs/monthly-okr-p2-review-guide.md)** - Runbook đối chiếu tự đánh giá vs thực tế + xuất báo cáo HTML

### Thành Viên Nhóm

| Tên | Vai Trò | KPI Link |
|-----|---------|----------|
| Trịnh Quốc Hoàn Đạt (dattqh) | Trưởng phòng Công Nghệ | [KPI](https://my.inet.vn/account/kpi/detail/dattqh@inet.vn) |
| Nguyễn Đăng Đức | Frontend | [KPI](https://my.inet.vn/account/kpi/detail/duc@inet.vn) |
| Bùi Văn Hổ | Design System | [KPI](https://my.inet.vn/account/kpi/detail/ho@inet.vn) |
| Đinh Tiến Chương | Frontend | [KPI](https://my.inet.vn/account/kpi/detail/chuong@inet.vn) |
| Tuấn Anh | AI Research | — |

### Bắt Đầu Nhanh

**Thêm KPI cho tháng này:**
1. Cập nhật file ghi chép trong `weekly meetings/`
2. Chạy skill automation: `/okr-kpi-myinet 03/2026`
3. Xác nhận các entry trên my.inet.vn

**Cập nhật đánh giá P2:**
1. Mở file thành viên trong `members/`
2. Điền điểm và kết quả đánh giá
3. Kiểm tra công thức tính tổng hợp

---

*Lần cập nhật: Tháng 03/2026 | Trưởng phòng: Đạt | Quản lý: Team Lead*
