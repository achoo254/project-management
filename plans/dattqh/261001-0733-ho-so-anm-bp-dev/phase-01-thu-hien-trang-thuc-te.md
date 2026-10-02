---
phase: 1
title: "Thu hiện trạng thực tế"
status: in-progress
priority: P1
effort: "M"
dependencies: []
---

# Phase 1: Thu hiện trạng thực tế (01–02/10)

## Goal
Có bằng chứng chỉ-đọc, có ngày chốt, về **cách BP-DEV đang làm thật** trên mọi sản phẩm. BP-DEV tự mô tả, không gửi yêu cầu
ra ngoài bộ phận; việc BP-DEV không tự xác minh được thì ghi CHƯA XÁC MINH kèm hạn.

## Đầu ra (lưu ở iCloud `BP-DEV-ho-so-2026-10/04-bang-chung/`, không vào git)
- `EVD-BM01-20261001-danh-sach-project-gitlab.csv`: toàn bộ project trên gitlabs.inet.vn (namespace, visibility, ngày hoạt động cuối, người tạo).
- `EVD-BM01-20261001-nguoi-dong-gop-chinh.csv`: 3 người commit nhiều nhất trong 6 tháng của mỗi repo. Dùng để đề xuất người phụ trách sản phẩm.
- `EVD-BM06-20261001-quyen-cao-gitlab.csv`: tài khoản Admin/Owner/Maintainer, trạng thái 2FA, đăng nhập cuối. Không có token.
- `EVD-QT03-20261001-ci-va-nhanh-bao-ve.csv`: mỗi repo có file CI hay không, tên các job, có quét không, nhánh bảo vệ, quy tắc duyệt MR.
- `EVD-BM02-20261001-thanh-phan-phan-mem.csv`: runtime, framework, base image theo repo, kèm cột EOL.
- `EVD-BM03-20261001-file-nhay-cam-trong-repo.csv`: **chỉ đường dẫn và số lượng**, cả trong lịch sử Git. Không mở file.
- `EVD-BM09-20261001-dich-vu-ben-thu-ba.csv`: nhà cung cấp, sản phẩm sử dụng, loại dữ liệu nghi gửi đi.
- `00-nguon/phieu-hien-trang/EVD-QT01-20261001-phieu-hien-trang-san-pham.docx`: một phiếu cho mọi sản phẩm, người phụ trách BP-DEV trả lời (mẫu ở bước 4).

## Tasks & Steps
- [x] Bước 1: **Kiểm quyền token chỉ-đọc:** `source scripts/load-env.sh` (không in giá trị), gọi `GET /api/v4/user` và `GET /api/v4/projects?per_page=1` để xác nhận token đọc được và có/không quyền admin. Không có quyền admin thì cột 2FA và đăng nhập cuối ghi "cần Admin GitLab cung cấp" và đưa vào yêu cầu ở bước 5.
- [x] Bước 2: **Kết xuất GitLab** (script Python chỉ đọc, lưu ở scratchpad, không vào repo): projects (phân trang), members theo access_level ≥ 40, protected_branches, approval rules, file `.gitlab-ci.yml` của nhánh mặc định, pipelines 90 ngày gần nhất (đếm job theo stage), users với `two_factor_enabled` nếu có quyền.
- [x] Bước 3: **Quét repo cục bộ** để lấy thành phần phần mềm, CI, file nhạy cảm và dịch vụ bên thứ ba. Dùng lại phương pháp đã chạy ngày 01/10, mở rộng ra mọi repo trong danh sách GitLab: clone nông (`--depth 1`, chỉ-đọc) vào scratchpad những repo chưa có.
- [ ] Bước 4 (phiếu đã điền sẵn 01/10; chờ người phụ trách BP-DEV trả lời trước 17:00 05/10): **Phiếu hiện trạng cho mỗi sản phẩm** (trọng tâm "mô tả công việc hiện tại"). Người phụ trách BP-DEV trả lời cho mọi sản phẩm trước 17:00 05/10. Mỗi câu trả lời thực tế, cụ thể, có ví dụ:
   - Phát triển: nhận yêu cầu ở đâu; có issue không; ai review; ai merge; môi trường dev/staging.
   - Phát hành: ai bấm deploy; deploy bằng gì; có duyệt không; rollback thế nào; lần rollback gần nhất.
   - Vận hành: theo dõi lỗi ở đâu; log để đâu và giữ bao lâu; ai trực; healthcheck.
   - Sự cố: sự cố gần nhất là gì; ai phát hiện; xử lý ra sao; có ghi lại không.
   - Bảo mật: đăng nhập sản phẩm (mật khẩu, 2FA, khóa phiên); quyền quản trị; bí mật cấu hình để đâu; dịch vụ bên ngoài nhận dữ liệu gì.
   - Sao lưu: dữ liệu gì; ai sao lưu; đã thử khôi phục chưa.
- [x] Bước 5: **Không gửi yêu cầu ra ngoài BP-DEV** (quyết định 01/10). Các mục cần thông tin của đơn vị khác (sao lưu CSDL, log tập trung, EOL hạ tầng, 2FA toàn GitLab, tài liệu gốc GOV/CMP/OPS, trạng thái production ngoài quyền của BP-DEV) ghi CHƯA XÁC MINH kèm hạn ở Phase 4.
- [x] Bước 6: **Ghi nhật ký bằng chứng:** mỗi file EVD ghi người chạy, lệnh hoặc nguồn, thời điểm chốt (UTC+7).

## Verification
- [x] Đủ các loại file EVD ở trên (nay 18 tệp trong `04-bang-chung/`). Mỗi file có dòng tiêu đề, người chạy, phương pháp và thời điểm chốt 01/10/2026.
- [x] `grep -E -i "(glpat-|sk-[A-Za-z0-9]{10}|BEGIN (RSA|OPENSSH|EC) PRIVATE|password\s*[:=]\s*\S{6,})" 04-bang-chung/*` không trả dòng nào.
- [x] Phiếu hiện trạng phủ đủ 17 sản phẩm trong DEV-BM-01 (1 phiếu, người phụ trách BP-DEV trả lời toàn bộ).

## Rủi ro
- Token không có quyền admin GitLab: chỉ lấy được phần project-level. Phần còn lại chuyển thành yêu cầu, không đoán.
- Repo không có trên máy: clone nông chỉ-đọc vào scratchpad; xóa sau khi xong Phase 6.

## Kết quả thực hiện (01/10/2026, chốt 14:39 +0700)
- [x] Token GitLab: tài khoản dattqh, có 2FA, **không phải Admin**. Nhìn thấy 78 project, trong đó 50 đang hoạt động. Chỉ dùng GET.
- [x] Bằng chứng ở `04-bang-chung/`: 8 file EVD và danh mục `EVD-00-…`. Quét chuỗi giống bí mật: 0 kết quả.
- [x] 1 phiếu hiện trạng (.docx) cho 17 sản phẩm: `00-nguon/phieu-hien-trang/EVD-QT01-20261001-phieu-hien-trang-san-pham.docx`, điền sẵn dữ kiện GitLab. **Người phụ trách BP-DEV trả lời toàn bộ** (quyết định 01/10); không phát phiếu cho thành viên khác. Hạn 17:00 05/10.
- [x] 19 repo chưa thuộc sản phẩm nào: `EVD-BM01-20261001-repo-can-phan-loai.csv`, người phụ trách BP-DEV phân loại.
- [x] Quyết định 01/10: **không gửi yêu cầu ra ngoài BP-DEV**. Bản nháp 3 yêu cầu đã hủy.
- [x] Phiếu được điền sẵn tự động từ bằng chứng (01/10); người phụ trách BP-DEV chỉ sửa câu sai và trả lời 10 nhóm câu hỏi còn lại.

Số liệu chính (phạm vi 50 project đang hoạt động):
- Chế độ hiển thị: 41 private, 7 internal, **2 public**.
- CI: 22/50 có. Trong đó SAST 1, quét thư viện 2, quét bí mật 1, bước duyệt thủ công 3. Không project nào cấu hình số người duyệt MR bắt buộc (cần xác minh phiên bản GitLab có hỗ trợ không).
- 3 project đang hoạt động không có nhánh bảo vệ.
- 20 tài khoản có quyền Maintainer/Owner; 13 tài khoản có quyền Owner ở ít nhất một project.
- 29 repo có tổng 121 file có tên giống file nhạy cảm (theo tên, cần lọc tay).
- Gói thư viện bên thứ ba trong package.json: firebase/firebase-admin (12 repo), S3 SDK (5 repo), nodemailer (2 repo).

Thay đổi so với kế hoạch: Phase 1 chạy sớm một ngày (01/10). Clone nông repo vắng mặt **không cần**, vì thành phần phần mềm và tên file lấy qua API. Lịch sử Git chỉ có cho 20 repo đã clone sẵn.

Cập nhật 01/10 (sau khi chụp bằng chứng):
- Repo: xóa `dattqh/one-monit`, `dattqh/crawl-data-linkedin` (đã sao lưu bundle); lưu trữ `dattqh/domain-nodejs`; chuyển `dattqh/cloud-labs-dev`, `dattqh/one-scribe` sang GitHub private (lịch sử đã làm sạch), bản GitLab lưu trữ. Nhật ký: `EVD-BM01-20261001-thay-doi-kho-gitlab.txt`.
- Cơ cấu: Phòng Nền tảng gồm Bộ phận Kỹ thuật và BP-DEV. Trưởng phòng Nền tảng chịu trách nhiệm cao nhất về quản trị GitLab. CEO chịu trách nhiệm quy trình triển khai production.
