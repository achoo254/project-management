# Đối chiếu TCVN 14423:2026 mục 5 (HTTT cấp độ 3) với bộ mock DEV-QT/DEV-BM

- Ngày lập: 01/10/2026 (Asia/Saigon)
- Nguồn yêu cầu: `tcvn14423-cap3.txt` (trích mục 5), so sánh cấp độ 2 trong `tcvn14423.txt` mục 4
- Tài liệu được đối chiếu: `plans/dattqh/reports/mock-261001-1121-quy-trinh-bieu-mau-anm-bp-dev.html` (TPL, QT-01…QT-10, BM-01…BM-12)

**Cách đọc**

- Mức phủ chỉ đánh giá **nội dung có trong mock** (kể cả khi mới là dàn ý), không đánh giá hiện trạng áp dụng thật.
- Với dòng Chủ trì = "Phối hợp", mức phủ tính theo **phần việc của BP-DEV** (ứng dụng, runtime, thư viện, CI/CD, GitLab, tài khoản và dữ liệu trong sản phẩm). Đơn vị chủ trì phần còn lại ghi trong ngoặc.
- Ký hiệu **†**: điều khoản có yêu cầu "đánh giá, cập nhật định kỳ" do mẫu chung xử lý, xem mục B1. Phần này không làm hạ mức phủ của từng dòng.
- "(?)" = chưa chắc, cần xác nhận.

---

## A. Bảng đối chiếu từng điều khoản

### 5.1 Quản lý rủi ro an ninh mạng

| Điều khoản | Tóm tắt yêu cầu | Chủ trì | Tài liệu mock đang phủ | Mức phủ | Cần bổ sung gì cụ thể |
|---|---|---|---|---|---|
| 5.1.2.1 | Có quy định, quy trình QLRR gồm xác định, phân tích, đánh giá, xử lý; cập nhật tối thiểu 01 lần/năm hoặc khi có thay đổi † | Phối hợp (Ban ATANM chủ trì) | BM-10 | Một phần | BM-10 thêm phần hướng dẫn 4 bước thực hiện ở BP-DEV, dẫn chiếu quy trình rủi ro công ty (Sổ 7 RSK) |
| 5.1.2.2 | Xác định rủi ro (từ tài sản, lỗ hổng, tài khoản…), gồm rủi ro từ bên thứ ba, nhà cung cấp; tối thiểu 01 lần/năm hoặc khi hệ thống thay đổi | Phối hợp (Ban ATANM chủ trì) | BM-10, BM-09 | Một phần | BM-10 thêm cột "Nguồn rủi ro" (nội bộ/bên thứ ba); ghi chu kỳ năm và các sự kiện kích hoạt: phát hành lớn, lỗ hổng mới, sự cố |
| 5.1.2.3 | Phân tích, đánh giá mức ảnh hưởng, quyết định chấp nhận hay giảm thiểu; đánh giá ngay sau khi xác định và đánh giá lại khi có thay đổi | Phối hợp (Ban ATANM chủ trì) | BM-10 (Khả năng × Tác động) | Một phần | Thêm cột "Quyết định xử lý" (chấp nhận/giảm thiểu/chuyển giao/né tránh) và người phê duyệt quyết định |
| 5.1.2.4 | Thực hiện biện pháp xử lý; có phương án ứng phó khi rủi ro còn lại xảy ra; tối thiểu 01 lần/năm đánh giá hiệu quả biện pháp kiểm soát | Phối hợp (Ban ATANM chủ trì) | BM-10 (biện pháp bổ sung) | Một phần | Thêm cột "Rủi ro còn lại" và "Phương án ứng phó"; thêm phần biên bản đánh giá hiệu quả kiểm soát hằng năm |
| 5.1.2.5 | Giám sát, cập nhật thay đổi: khả năng xảy ra, mức ảnh hưởng, mức rủi ro, tài sản bị ảnh hưởng, biện pháp đã áp dụng | Phối hợp (Ban ATANM chủ trì) | BM-10 | Đã thể hiện | Đủ các trường. Nên thêm "Ngày cập nhật gần nhất" để chứng minh có theo dõi |
| 5.1.2.6 | Thông báo kịp thời cho các bên liên quan về thay đổi quan trọng liên quan đến rủi ro | Phối hợp (Ban ATANM chủ trì) | — | Chưa thể hiện | Quy định: rủi ro mới hoặc tăng điểm vượt ngưỡng thì báo Ban ATANM và chủ sở hữu sản phẩm; thêm cột "Đã thông báo cho / ngày" |

### 5.2 Quản lý tài sản phần cứng

| Điều khoản | Tóm tắt yêu cầu | Chủ trì | Tài liệu mock đang phủ | Mức phủ | Cần bổ sung gì cụ thể |
|---|---|---|---|---|---|
| 5.2.2.1 | Danh sách mọi tài sản phần cứng (cả ảo hóa, đám mây) với IP, MAC/serial, EOL, vị trí, mục đích, người chịu trách nhiệm; đăng ký thiết bị di động | Hạ tầng | — | Ngoài phạm vi BP-DEV | Tùy chọn: BM-01 thêm cột "Máy chủ/môi trường chạy" trỏ tới mã tài sản của Hạ tầng (?) |
| 5.2.2.2 | Quy trình phát hiện, xử lý tài sản phần cứng kết nối trái phép, tối thiểu 01 lần/06 tháng | Hạ tầng | — | Ngoài phạm vi BP-DEV | — |
| 5.2.2.3 | Phương án xóa sạch dữ liệu trên phần cứng khi chuyển giao hoặc đổi mục đích sử dụng | Hạ tầng | (QT-01 giai đoạn 7 chỉ xóa dữ liệu ứng dụng) | Ngoài phạm vi BP-DEV | — |
| 5.2.2.4 | Bật ghi nhật ký DHCP; rà soát nhật ký để cập nhật danh sách tài sản tối thiểu 01 lần/06 tháng | Hạ tầng | — | Ngoài phạm vi BP-DEV | — |

### 5.3 Quản lý tài sản phần mềm

| Điều khoản | Tóm tắt yêu cầu | Chủ trì | Tài liệu mock đang phủ | Mức phủ | Cần bổ sung gì cụ thể |
|---|---|---|---|---|---|
| 5.3.2.1 | Danh sách phần mềm đang cài: tên, mục đích, EOL, phạm vi, chủ thể quản lý, bản quyền, phiên bản, HTTT thành phần; gắn người chịu trách nhiệm | Phối hợp (Hạ tầng: phần mềm trên máy chủ/máy trạm) | BM-01, BM-02 | Một phần | BM-01 thêm cột phiên bản production, giấy phép/bản quyền, HTTT thành phần; BM-02 ghi mọi runtime/framework chứ không chỉ thành phần EOL |
| 5.3.2.2 | Danh sách phần mềm được phép (kể cả của nhà cung cấp, môi trường thực thi); kiểm soát cài đặt, đặc quyền tối thiểu, chặn thư viện/mã trái phép; rà soát tối thiểu 01 lần/năm † | Phối hợp (Hạ tầng chủ trì cho máy chủ/máy trạm) | QT-02 (nguồn thư viện tin cậy, lockfile) | Một phần | Lập danh sách runtime, base image, framework, kho gói được phép; CI chặn nguồn gói ngoài danh sách (?); đặt chu kỳ rà soát năm |
| 5.3.2.3 | Phát hiện, xử lý phần mềm trái phép tối thiểu 01 lần/năm; danh sách ngoại lệ kèm biện pháp kiểm soát; kế hoạch gỡ bỏ phần còn lại | Phối hợp (Hạ tầng chủ trì) | BM-01 Phần B (shadow IT) | Một phần | Ghi chu kỳ năm cho Phần B; thêm danh sách ngoại lệ (thành phần chưa được phép nhưng cần dùng) kèm biện pháp kiểm soát và hạn gỡ bỏ |

### 5.4 Quản lý tài sản thông tin

| Điều khoản | Tóm tắt yêu cầu | Chủ trì | Tài liệu mock đang phủ | Mức phủ | Cần bổ sung gì cụ thể |
|---|---|---|---|---|---|
| 5.4.2.1 | Quy định tài sản thông tin: mức nhạy cảm (4 mức), chủ sở hữu, xử lý, lưu trữ, tiêu hủy; quy trình yêu cầu truy cập/sửa/xóa dữ liệu; kiểm tra phân quyền dữ liệu 01 lần/06 tháng † | Phối hợp (Ban ATANM chủ trì, CMP-08) | QT-10 (thời hạn lưu, xóa mọi bản sao), BM-01 (loại dữ liệu) | Một phần | Áp thang 4 mức nhạy cảm vào BM-01/BM-09; quy trình xin truy cập dữ liệu production (truy vấn, xuất dữ liệu); rà phân quyền dữ liệu 01 lần/06 tháng |
| 5.4.2.2 | Lập danh sách tài sản thông tin theo quy trình; đánh giá, cập nhật tối thiểu 01 lần/năm hoặc khi có thay đổi | Phối hợp (Ban ATANM chủ trì) | BM-01 (cột loại dữ liệu), BM-09 | Một phần | Thêm danh sách tài sản thông tin theo sản phẩm: CSDL/bảng chính, kho tệp, log, bản sao lưu; kèm mức nhạy cảm, chủ sở hữu, nơi lưu, thời hạn lưu |
| 5.4.2.3 | Danh sách quyền truy cập của từng tài khoản, người dùng đối với từng loại tài sản thông tin | BP-DEV | BM-06 (GitLab, token API quản trị) | Một phần | Thêm ma trận vai trò × tài sản thông tin cho từng sản phẩm, gồm tài khoản kỹ thuật kết nối CSDL |
| 5.4.2.4 | Mã hóa thông tin xác thực và dữ liệu nhạy cảm khi lưu trữ và khi truyền; bảo vệ, quản lý vòng đời mã khóa | Phối hợp (Hạ tầng: mã hóa ổ đĩa, lưu trữ) | QT-05, BM-03 (vòng đời khóa, chứng thư TLS) | Một phần | Điểm c đã có. Bổ sung điểm a, b: băm mật khẩu, mã hóa trường nhạy cảm (eKYC, thanh toán), TLS cho mọi kết nối kể cả nội bộ |
| 5.4.2.5 | Lưu trữ dữ liệu quan trọng kèm mã kiểm tra tính nguyên vẹn | BP-DEV | — | Chưa thể hiện | Quy định checksum/hash cho bản sao lưu, tệp xuất, bản phát hành; kiểm tra mã khi khôi phục (BM-08) |
| 5.4.2.6 | Tài liệu mô tả luồng dữ liệu quan trọng; quy định quản lý phiên bản tài liệu; cập nhật tối thiểu 01 lần/năm † | BP-DEV | BM-09 (luồng ra bên thứ ba), QT-01 (docs/ trong repo), quy ước lần ban hành ở trang bìa | Một phần | Bắt buộc sơ đồ luồng dữ liệu nội bộ và ra ngoài cho từng sản phẩm, lưu trong docs/, liên kết từ BM-01; điểm b đã có quy ước phiên bản |
| 5.4.2.7 | Quy định xử lý dữ liệu quan trọng; tách biệt (logic/vật lý) môi trường xử lý, lưu trữ dữ liệu nhạy cảm cao với dữ liệu nhạy cảm thấp | Phối hợp (Hạ tầng: phân vùng máy chủ) | QT-10 (không dùng dữ liệu thật để kiểm thử), QT-03 (tách dev/staging/production) | Một phần | Quy định dữ liệu nhạy cảm cao nằm ở CSDL/schema/bucket riêng, quyền riêng; cấm đưa dữ liệu đó vào dev/staging |
| 5.4.2.8 | Sử dụng chữ ký số khi trao đổi dữ liệu nhạy cảm cao, dữ liệu quan trọng | Phối hợp (Ban ATANM ban hành quy định) | — | Chưa thể hiện | Xác định các luồng trao đổi dữ liệu quan trọng giữa hệ thống/với đối tác; áp dụng ký số cho API, webhook, tệp xuất (?) |

### 5.5 Cấu hình an toàn cho phần cứng và phần mềm

| Điều khoản | Tóm tắt yêu cầu | Chủ trì | Tài liệu mock đang phủ | Mức phủ | Cần bổ sung gì cụ thể |
|---|---|---|---|---|---|
| 5.5.2.1 | Quy định và tài liệu cấu hình chuẩn, cấu hình tăng cường; giao thức an toàn; tắt giao thức/dịch vụ thừa; tăng cường trước vận hành; cập nhật tối thiểu 01 lần/năm † | Phối hợp (Hạ tầng chủ trì OS, mạng) | (BM-11 chỉ nêu "tài liệu cấu hình") | Chưa thể hiện | Phần BP-DEV: cấu hình chuẩn cho ứng dụng, container, reverse proxy, CI: tắt debug, endpoint thừa, header bảo mật, TLS; checklist trước go-live |
| 5.5.2.2 | Tự khóa phiên: phần mềm nghiệp vụ dữ liệu quan trọng ≤15 phút, phiên quản trị ≤05 phút; khóa sau ≤05 lần đăng nhập sai; có mở khóa khẩn cấp cho quản trị | Phối hợp (Hạ tầng: máy tính, thiết bị) | QT-02 (chỉ nêu "phiên đăng nhập") | Một phần | Ghi giá trị cụ thể vào QT-02 (TCVN ghi "có thể"); thời gian mở khóa sau khi bị khóa tối thiểu 12 giờ, tối đa 30 ngày (?) |

### 5.6 Quản lý tài khoản và quyền truy cập

| Điều khoản | Tóm tắt yêu cầu | Chủ trì | Tài liệu mock đang phủ | Mức phủ | Cần bổ sung gì cụ thể |
|---|---|---|---|---|---|
| 5.6.2.1 | Danh sách mọi tài khoản (quản trị, tác nghiệp, kỹ thuật) với loại, tên, trạng thái, hệ thống, người quản lý, phòng ban, ngày kích hoạt/vô hiệu hóa; rà soát tối thiểu 01 lần/06 tháng | Phối hợp (Hạ tầng: tài khoản OS, thiết bị) | QT-04, BM-06 Phần A, B (rà hằng quý) | Một phần | Mở rộng BM-06 ra tài khoản quản trị trong sản phẩm, tài khoản CSDL, service account, CI; thêm cột loại, trạng thái, phòng ban, ngày kích hoạt/vô hiệu hóa |
| 5.6.2.2 | Đổi mật khẩu mặc định; quy tắc độ dài; có MFA ≥08 ký tự, không MFA ≥14 ký tự đủ 4 loại; quản trị: MFA, đổi 01 lần/02 tháng, không trùng 10 mật khẩu trước | Phối hợp (Ban ATANM ban hành chính sách chung (?)) | (QT-04 chỉ nêu 2FA GitLab; BM-12 2FA quản trị) | Chưa thể hiện | Thêm mục chính sách mật khẩu: QT-04 cho tài khoản nhân sự BP-DEV dùng, QT-02 cho chức năng đăng nhập của sản phẩm (đổi mật khẩu lần đầu, mật khẩu duy nhất hoặc SSO) |
| 5.6.2.3 | Quản lý tài khoản tập trung; đổi/vô hiệu hóa tài khoản mặc định; tách loại tài khoản; mỗi tài khoản một người, tài khoản chung phải được duyệt; vô hiệu hóa sau 45 ngày † | Phối hợp | QT-04 (cấp, thu hồi khi vào/chuyển/nghỉ; SSO khi có) | Một phần | Thêm: vô hiệu hóa tài khoản không hoạt động sau 45 ngày; xử lý root/admin mặc định; phê duyệt tài khoản dùng chung; tách tài khoản quản trị với tài khoản hằng ngày |
| 5.6.2.4 | Quyền tối thiểu, phân tách nhiệm vụ; tài liệu quyền theo chức danh/bộ phận; MFA cho truy cập từ ngoài, từ bên thứ ba, từ Internet và tài khoản quản trị † | Phối hợp | QT-04 (quyền tối thiểu, 2FA GitLab), QT-03 (người review không phải tác giả) | Một phần | Ma trận quyền theo chức danh; MFA bắt buộc cho trang quản trị sản phẩm, truy cập từ Internet, tài khoản đối tác |

### 5.7 Quản lý lỗ hổng bảo mật

| Điều khoản | Tóm tắt yêu cầu | Chủ trì | Tài liệu mock đang phủ | Mức phủ | Cần bổ sung gì cụ thể |
|---|---|---|---|---|---|
| 5.7.2.1 | Quy trình: rà quét, đánh giá mức nghiêm trọng, chia sẻ/tiếp nhận báo cáo, khắc phục theo ưu tiên, đánh giá lại; rà soát quy trình và rà quét tối thiểu 01 lần/06 tháng | Phối hợp (Hạ tầng: quét hạ tầng) | QT-06, BM-05, QT-02 (SECURITY.md) | Một phần | Thêm bước kiểm tra lại sau khắc phục (cột trong BM-05); quét toàn bộ sản phẩm tối thiểu 01 lần/06 tháng kể cả khi không thay đổi; chu kỳ rà soát QT-06 là 06 tháng, không phải năm |
| 5.7.2.2 | Quản lý bản vá: máy chủ vá tập trung; đánh giá tác động, kiểm thử, phương án phục hồi trước khi vá hệ thống dữ liệu quan trọng; vá máy người dùng tối thiểu 01 lần/tháng | Phối hợp (Hạ tầng chủ trì vá tập trung, máy trạm) | QT-03 (thay đổi tiêu chuẩn, staging, rollback), QT-06 | Một phần | Phần BP-DEV: luồng vá thư viện, runtime theo QT-03, bắt buộc đánh giá tác động và cách hoàn tác khi sản phẩm xử lý dữ liệu quan trọng |

### 5.8 Quản lý nhật ký an ninh mạng

| Điều khoản | Tóm tắt yêu cầu | Chủ trì | Tài liệu mock đang phủ | Mức phủ | Cần bổ sung gì cụ thể |
|---|---|---|---|---|---|
| 5.8.2.1 | Quy định log: truy cập, tiến trình, ứng dụng, cảnh báo, có trường tối thiểu; đồng bộ thời gian; SIEM; lưu tập trung tối thiểu 03 tháng; rà soát 01 lần/06 tháng † | Phối hợp (Hạ tầng/Ban ATANM chủ trì SIEM, NTP) | QT-07 (log ứng dụng, log kiểm toán), QT-04 (log API quản trị 12 tháng), QT-08 (giờ UTC+7) | Một phần | Quy định trường log truy cập (IP nguồn/đích, tài khoản, thời điểm, hành vi); lưu ≥03 tháng; đẩy về kho log tập trung/SIEM; biên bản rà soát 06 tháng |

### 5.9 Bảo vệ trình duyệt web, thư điện tử

| Điều khoản | Tóm tắt yêu cầu | Chủ trì | Tài liệu mock đang phủ | Mức phủ | Cần bổ sung gì cụ thể |
|---|---|---|---|---|---|
| 5.9.2.1 | Danh sách trình duyệt, dịch vụ thư được phép, còn hỗ trợ; giải pháp an ninh cho thư; cập nhật bản vá thường xuyên | Hạ tầng | — | Ngoài phạm vi BP-DEV | — |
| 5.9.2.2 | Triển khai dịch vụ lọc tên miền chặn tên miền giả mạo, độc hại | Hạ tầng | — | Ngoài phạm vi BP-DEV | — |

### 5.10 Phòng chống phần mềm độc hại

| Điều khoản | Tóm tắt yêu cầu | Chủ trì | Tài liệu mock đang phủ | Mức phủ | Cần bổ sung gì cụ thể |
|---|---|---|---|---|---|
| 5.10.2.1 | Giải pháp phòng chống mã độc trên máy chủ, máy người dùng; bảo vệ thời gian thực, tự cập nhật mẫu | Hạ tầng | — | Ngoài phạm vi BP-DEV | — |
| 5.10.2.2 | Quét mã độc, tắt autorun/autoplay với thiết bị lưu trữ di động | Hạ tầng | — | Ngoài phạm vi BP-DEV | — |
| 5.10.2.3 | Bật tính năng phòng chống khai thác lỗ hổng trên phần cứng, phần mềm (nếu có) | Hạ tầng | — | Ngoài phạm vi BP-DEV | Tùy chọn: tùy chọn bảo mật của container/runtime trong cấu hình chuẩn (?) |
| 5.10.2.4 | EDR hoặc tương đương phát hiện theo hành vi; kết nối SIEM giám sát thời gian thực | Hạ tầng | — | Ngoài phạm vi BP-DEV | — |

### 5.11 Sao lưu và khôi phục dữ liệu

| Điều khoản | Tóm tắt yêu cầu | Chủ trì | Tài liệu mock đang phủ | Mức phủ | Cần bổ sung gì cụ thể |
|---|---|---|---|---|---|
| 5.11.2.1 | Quy định: loại dữ liệu (cấu hình, OS, CSDL, nghiệp vụ), tần suất, phương pháp, quản lý vùng lưu, khôi phục thử định kỳ; lưu trữ tập trung; cập nhật 01 lần/năm † | Phối hợp (Hạ tầng: bản dự phòng OS, lưu trữ tập trung) | QT-09, BM-08 (khôi phục thử 6 tháng/lần) | Một phần | Thêm cột phương pháp (full/incremental/snapshot), dữ liệu cấu hình ứng dụng; chốt bộ phận sao lưu CSDL (đang CẦN XÁC MINH) |
| 5.11.2.2 | Danh sách dữ liệu cần sao lưu, tần suất ngày/tuần/tháng/năm; sao lưu tự động | Phối hợp | QT-09 (bảng sao lưu theo sản phẩm) | Một phần | Bắt buộc sao lưu tự động (job định kỳ), lưu bằng chứng lần chạy thành công gần nhất |
| 5.11.2.3 | Quy tắc 3-2-1 hoặc tương đương; mã hóa bản sao lưu dữ liệu quan trọng | Phối hợp (Hạ tầng chủ trì) | QT-09 (cột mã hóa) | Một phần | Ghi rõ áp dụng 3-2-1: số bản, số loại phương tiện, bản ngoài nơi vận hành |
| 5.11.2.4 | Bản sao lưu được định danh, quản lý phiên bản, lưu ở hạ tầng tách biệt môi trường vận hành | Phối hợp (Hạ tầng chủ trì) | QT-09 (cột nơi lưu) | Một phần | Thêm cột mã định danh, phiên bản bản sao lưu, "tách biệt production: Có/Không" |

### 5.12 Quản lý hạ tầng mạng

| Điều khoản | Tóm tắt yêu cầu | Chủ trì | Tài liệu mock đang phủ | Mức phủ | Cần bổ sung gì cụ thể |
|---|---|---|---|---|---|
| 5.12.2.1 | Sơ đồ kiến trúc mạng (tổng quan, chi tiết, phương án an ninh); phân vùng, đặc quyền ít nhất, sẵn sàng; cập nhật 01 lần/năm | Hạ tầng | — | Ngoài phạm vi BP-DEV | BP-DEV cung cấp tài liệu kiến trúc ứng dụng (QT-01, docs/) làm đầu vào |
| 5.12.2.2 | Quản lý an toàn hạ tầng: dự phòng, chống thất thoát dữ liệu, IPS, DBF, NAC, WAF, chống DDoS, quản lý thay đổi, kiểm tra hiệu năng; 7 vùng mạng | Phối hợp (Hạ tầng chủ trì) | QT-03 (quản lý thay đổi ứng dụng), QT-07 (giám sát hiệu năng ứng dụng) | Một phần | Phần BP-DEV: điều kiện go-live sản phẩm có Internet phải đặt sau WAF; CSDL trong vùng CSDL; tham chiếu quy trình thay đổi hạ tầng |
| 5.12.2.3 | Kế hoạch, quy trình thử nghiệm và nghiệm thu; kiểm thử trước vận hành; bộ phận chịu trách nhiệm; bên độc lập giám sát; báo cáo nghiệm thu được chủ quản duyệt | BP-DEV | QT-01 (6 cổng), QT-03 (staging, B6), BM-11, BM-12 | Một phần | Điểm d, e chưa có cho luồng L1: cần bộ phận độc lập (Ban ATANM (?)) giám sát và biên bản nghiệm thu do chủ quản HTTT phê duyệt trước go-live |
| 5.12.2.4 | Kết nối an toàn; xác thực khi quản trị; timeout phiên; kiểm soát truy cập vào/ra theo dịch vụ; giới hạn kết nối đồng thời theo nguồn và theo dịch vụ | Phối hợp (Hạ tầng: tường lửa, thiết bị) | QT-02 (xác thực, phiên), QT-04 | Một phần | Phần ứng dụng: timeout phiên, giới hạn tần suất và kết nối đồng thời theo IP/dịch vụ, ứng dụng chỉ gọi ra các đích được phép |
| 5.12.2.5 | Truy cập từ xa qua VPN có xác thực, xác thực bổ sung; giới hạn dải địa chỉ/thiết bị được quản trị từ xa | Phối hợp (Hạ tầng chủ trì VPN) | (QT-01 A.3 chỉ dùng làm tiêu chí rủi ro) | Chưa thể hiện | QT-04: truy cập production, trang quản trị, API quản trị chỉ qua VPN + MFA, giới hạn IP được phép |

### 5.13 Giám sát và phòng thủ an ninh mạng

| Điều khoản | Tóm tắt yêu cầu | Chủ trì | Tài liệu mock đang phủ | Mức phủ | Cần bổ sung gì cụ thể |
|---|---|---|---|---|---|
| 5.13.2.1 | Giám sát an ninh thiết bị, máy chủ, ứng dụng, dịch vụ; triển khai SIEM liên kết, phân tích sự kiện | Phối hợp (Ban ATANM/Hạ tầng chủ trì SIEM) | QT-07, QT-08 | Một phần | Danh sách sản phẩm đã đưa vào giám sát; nguồn log kiểm toán của ứng dụng được gửi về SIEM |
| 5.13.2.2 | Bật tường lửa, cảnh báo, ngăn chặn xâm nhập của hệ điều hành và hệ thống (nếu có) | Hạ tầng | — | Ngoài phạm vi BP-DEV | — |
| 5.13.2.3 | Kiểm soát cổng kết nối trên thiết bị mạng; tách cổng quản trị ứng dụng khỏi cổng cung cấp dịch vụ | Phối hợp (điểm a thuộc Hạ tầng) | — | Chưa thể hiện | Điểm b thuộc BP-DEV: trang/API quản trị chạy trên cổng hoặc tên miền riêng, không mở ra Internet; đưa vào checklist cấu hình chuẩn |
| 5.13.2.4 | Thu thập log luồng dữ liệu mạng, lưu lượng từ thiết bị mạng để rà soát, cảnh báo | Hạ tầng | — | Ngoài phạm vi BP-DEV | — |
| 5.13.2.5 | Điều chỉnh ngưỡng cảnh báo sự kiện an ninh mạng tối thiểu 01 lần/06 tháng | Phối hợp (Ban ATANM chủ trì SIEM) | QT-07 (ngưỡng, luật phát hiện đề xuất) | Một phần | Thêm lịch rà ngưỡng 06 tháng/lần và biên bản ghi ngưỡng cũ, ngưỡng mới, lý do |

### 5.14 Nhân sự vận hành, quản trị, bảo vệ an ninh mạng

| Điều khoản | Tóm tắt yêu cầu | Chủ trì | Tài liệu mock đang phủ | Mức phủ | Cần bổ sung gì cụ thể |
|---|---|---|---|---|---|
| 5.14.2.1 | Bộ phận riêng vận hành, quản trị, bảo vệ ANM, độc lập chuyên môn; nhân sự có trình độ, cam kết bảo mật cả sau nghỉ việc | Nhân sự / Ban ATANM | — | Ngoài phạm vi BP-DEV | Ghi chú: BP-DEV vừa phát triển vừa vận hành nên vai trò kiểm tra độc lập thuộc Ban ATANM (?) |
| 5.14.2.2 | Chương trình nâng cao nhận thức cho toàn bộ nhân viên, tối thiểu 01 lần/năm; thu hồi tài sản, vô hiệu hóa mọi quyền khi thôi việc, chuyển việc | Phối hợp (Ban ATANM + Nhân sự chủ trì) | QT-04 (thu hồi quyền GitLab), QT-05 (xoay khóa khi người giữ nghỉ), BM-11 (thu hồi quyền bên giao) | Một phần | Checklist offboarding BP-DEV: GitLab, tài khoản quản trị sản phẩm, token, khóa, VPN, có biên bản; đào tạo lập trình an toàn hằng năm cho nhân sự BP-DEV (5.14.1 b) |

### 5.15 Quản lý nhà cung cấp sản phẩm, dịch vụ (không có điều khoản con)

| Điều khoản | Tóm tắt yêu cầu | Chủ trì | Tài liệu mock đang phủ | Mức phủ | Cần bổ sung gì cụ thể |
|---|---|---|---|---|---|
| 5.15 (5.15.2) | (1) Danh sách, trạng thái nhà cung cấp; (2) phân loại nhà cung cấp; (3) văn bản phạm vi trách nhiệm hai bên; (4) xem xét, cập nhật tối thiểu 01 lần/năm † | Phối hợp (Ban ATANM/Mua hàng chủ trì cấp công ty (?)) | BM-09, QT-10 | Một phần | BM-09 thêm cột phân loại (mức quan trọng), trạng thái, văn bản phạm vi trách nhiệm, ngày rà soát; gồm cả bên phát triển thuê khoán; đánh giá nhà cung cấp trước khi tích hợp (5.15.1) |

### 5.16 Quản trị ứng phó sự cố

| Điều khoản | Tóm tắt yêu cầu | Chủ trì | Tài liệu mock đang phủ | Mức phủ | Cần bổ sung gì cụ thể |
|---|---|---|---|---|---|
| 5.16.2.1 | Một người chủ chốt và ít nhất 01 người dự phòng; đầu mối với cơ quan chức năng; xác minh liên hệ hằng năm; phân vai; trách nhiệm phối hợp các phòng ban | Phối hợp (Ban ATANM chủ trì, OPS-12) | QT-08 mục 5 | Một phần | Ghi người chính và người dự phòng của BP-DEV (hiện chỉ "Người phụ trách BP-DEV là đầu mối mặc định"); xác minh danh bạ liên hệ BP-DEV hằng năm |
| 5.16.2.2 | Quy trình nội bộ báo cáo sự cố; phân nhóm sự cố; cập nhật tối thiểu 01 lần/năm † | Phối hợp | QT-08 (P1–P4, B1–B3), BM-07 | Đã thể hiện | — (chu kỳ rà soát xử lý tại B1) |
| 5.16.2.3 | Quy trình ứng phó, phối hợp với cơ quan chức năng, chuyên gia, bên cung cấp dịch vụ; cập nhật 01 lần/năm †; diễn tập định kỳ (5.16.1) | Phối hợp (Ban ATANM chủ trì) | QT-08 (B4–B7, CSIRT), hiện trạng diễn tập "CHƯA CÓ" | Một phần | Thêm bước liên hệ nhà cung cấp trong BM-09, bên thuê khoán; lịch diễn tập (TCVN chỉ ghi "định kỳ"; đề xuất 01 lần/năm (?)); hồ sơ diễn tập |

### 5.17 Phát triển ứng dụng an toàn

| Điều khoản | Tóm tắt yêu cầu | Chủ trì | Tài liệu mock đang phủ | Mức phủ | Cần bổ sung gì cụ thể |
|---|---|---|---|---|---|
| 5.17.2.1 | Quy trình phát triển an toàn; cập nhật 01 lần/năm †; thuê khoán: hợp đồng, cam kết bảo mật, mã nguồn hoặc chứng chỉ độc lập/kiểm thử xâm nhập và cam kết pháp lý | BP-DEV | QT-01, QT-02, QT-03 | Một phần | Điểm a đã có. Điểm c chưa có: thêm luồng "thuê khoán bên ngoài" vào QT-01 Phụ lục A và tiêu chí tương ứng vào BM-12 |
| 5.17.2.2 | Quy trình tiếp nhận, xử lý báo cáo lỗ hổng phần mềm, có kênh cho cá nhân, tổ chức bên ngoài báo cáo; cập nhật 01 lần/năm † | BP-DEV | QT-02 (SECURITY.md), QT-06 (người dùng báo), BM-05 | Một phần | SECURITY.md trong repo nội bộ thì người ngoài không xem được; cần kênh công khai (thư bảo mật, security.txt trên tên miền), các bước xác nhận, phản hồi, thời hạn |
| 5.17.2.3 | Kiến trúc có: kiểm tra đầu vào, kiểm tra đầu ra, chống tấn công phổ biến, kiểm soát thông báo lỗi, không lưu thông tin xác thực trong mã nguồn | BP-DEV | QT-02, QT-03 Phụ lục 9.1, QT-05 | Đã thể hiện | Viết rõ "kiểm tra tính hợp lệ dữ liệu đầu ra" (hiện mới ghi "mã hóa đầu ra") |
| 5.17.2.4 | Kiểm tra, khắc phục lỗ hổng của ứng dụng, mã nguồn, thư viện và thành phần bên thứ ba trước khi đưa vào vận hành chính thức | BP-DEV | QT-03 B4 (quét secret, thư viện), QT-01 giai đoạn 4, QT-06, BM-12 (L3b) | Một phần | Quy định bộ kiểm tra tối thiểu trước go-live: SAST, quét thư viện, kiểm tra động/OWASP cho bản đầu và bản lớn; lưu kết quả vào biên bản nghiệm thu |

### 5.18 Quản lý kiểm tra an ninh mạng

| Điều khoản | Tóm tắt yêu cầu | Chủ trì | Tài liệu mock đang phủ | Mức phủ | Cần bổ sung gì cụ thể |
|---|---|---|---|---|---|
| 5.18.2.1 | Chương trình kiểm thử xâm nhập: phê duyệt phạm vi, thời gian, phương pháp, đầu mối; không gián đoạn dịch vụ; tần suất quý/nửa năm/năm/đột xuất; hành vi cấm; cách phản ứng | Phối hợp (Ban ATANM chủ trì chương trình (?)) | (QT-06 chỉ nêu pentest là một nguồn lỗ hổng) | Chưa thể hiện | Phần BP-DEV: phạm vi sản phẩm, môi trường kiểm thử, tần suất chọn theo cấp độ; phiếu phê duyệt phạm vi kiểm thử (xem C, BM-13) |
| 5.18.2.2 | Khắc phục tồn tại phát hiện qua kiểm thử xâm nhập theo chính sách về phạm vi và mức ưu tiên | BP-DEV | QT-06 (nguồn pentest, thời hạn theo CVSS), BM-05 | Đã thể hiện | BM-05 nên ghi mã đợt kiểm thử ở cột Nguồn |
| 5.18.2.3 | Kiểm tra, đánh giá hiệu quả biện pháp bảo mật sau mỗi lần kiểm thử xâm nhập | Phối hợp (Ban ATANM chủ trì) | — | Chưa thể hiện | Thêm phần "đánh giá sau kiểm thử" vào BM-13, kết quả đưa vào BM-10 (đánh giá hiệu quả kiểm soát, 5.1.2.4) |

Tổng: 63 dòng (62 điều khoản x.y.z.w và 5.15), mỗi điều khoản xuất hiện một lần.

---

## B. Yêu cầu dùng chung cho nhiều điều khoản và cách mẫu chung (TPL) xử lý

**B1. Rà soát, cập nhật từng tài liệu theo chu kỳ (†)**
- "Đánh giá và cập nhật tối thiểu 01 lần/năm hoặc khi có thay đổi" có ở 5.1.2.1b, 5.3.2.2d, 5.4.2.1e, 5.4.2.2b, 5.4.2.6c, 5.5.2.1e, 5.6.2.3, 5.6.2.4, 5.8.2.1b, 5.11.2.1c, 5.12.2.1e, 5.15, 5.16.2.2c, 5.16.2.3b, 5.17.2.1b, 5.17.2.2b.
- Ngoại lệ: **quy trình quản lý lỗ hổng phải rà soát, cập nhật tối thiểu 01 lần/06 tháng** (5.7.2.1b), áp cho DEV-QT-06.
- Cách xử lý trong TPL: thêm vào khối tiêu đề hai trường "Chu kỳ rà soát: tối thiểu 01 lần/năm hoặc khi có thay đổi (QT-06: 06 tháng)" và "Rà soát gần nhất / kế tiếp". Trong "Lịch sử thay đổi" cho phép ghi dòng "Rà soát định kỳ, không thay đổi nội dung" để có bằng chứng ngay cả khi không sửa.

**B2. Tần suất vận hành bắt buộc (nên có bảng "Lịch định kỳ" ở mục 6 hoặc 7 của TPL và một bảng tổng ở trang tổng quan)**

| Tần suất tối thiểu | Hoạt động | Điều khoản | Tài liệu nhận |
|---|---|---|---|
| 01 lần/02 tháng | Đổi mật khẩu tài khoản quản trị | 5.6.2.2 | QT-04 |
| 45 ngày không hoạt động | Xóa/vô hiệu hóa tài khoản | 5.6.2.3 | QT-04, BM-06 |
| 01 lần/06 tháng | Rà danh sách tài khoản | 5.6.2.1d | BM-06 (hiện hằng quý, đã đạt) |
| 01 lần/06 tháng | Kiểm tra cấp độ phân quyền dữ liệu | 5.4.2.1d | QT-04/QT-10, BM-06 |
| 01 lần/06 tháng | Rà quét lỗ hổng; rà soát quy trình lỗ hổng | 5.7.2.1b | QT-06, BM-05 |
| 01 lần/06 tháng | Rà soát nhật ký an ninh mạng | 5.8.2.1 | QT-07 |
| 01 lần/06 tháng | Điều chỉnh ngưỡng cảnh báo | 5.13.2.5 | QT-07 |
| 01 lần/năm | Xác định rủi ro; đánh giá hiệu quả biện pháp kiểm soát | 5.1.2.2c, 5.1.2.4b | BM-10 |
| 01 lần/năm | Kiểm kê phần mềm; danh sách phần mềm được phép; phát hiện phần mềm trái phép | 5.3.1b, 5.3.2.2d, 5.3.2.3a | BM-01, BM-02 |
| 01 lần/năm | Cập nhật danh sách tài sản thông tin; tài liệu luồng dữ liệu | 5.4.2.2b, 5.4.2.6c | BM-01, docs/ |
| 01 lần/năm | Cập nhật danh sách nhà cung cấp | 5.15 | BM-09 |
| 01 lần/năm | Xác minh thông tin liên hệ ứng phó sự cố | 5.16.2.1c | QT-08 |
| 01 lần/năm | Đào tạo nhận thức an ninh mạng | 5.14.2.2d | Ban ATANM/Nhân sự |
| Lưu tối thiểu 03 tháng | Nhật ký an ninh mạng | 5.8.2.1 | QT-07 |
| Quý / nửa năm / năm / đột xuất (tổ chức tự chọn) | Kiểm thử xâm nhập | 5.18.2.1 | BM-13 (mới) |
| "Định kỳ" (TCVN không ghi số) | Khôi phục thử bản sao lưu; diễn tập ứng phó sự cố | 5.11.2.1a, 5.16.1 | QT-09/BM-08 (mock: 06 tháng); QT-08 |
| Mỗi lần thay đổi | Đánh giá lại rủi ro, thiết kế; cập nhật danh sách | 5.1.2.3b, 5.12.2.1d… | BM-10, QT-03 |

Ghi chú: các mốc 01 lần/06 tháng cho phần cứng và DHCP (5.2.2.2, 5.2.2.4) và vá máy người dùng 01 lần/tháng (5.7.2.2) thuộc Hạ tầng.

**B3. Hồ sơ, bằng chứng**
- Mỗi yêu cầu định kỳ cần hồ sơ chứng minh: danh sách/sổ có ngày chốt và biên bản rà soát (ai rà, số mục, kết luận).
- TPL mục 7 nên thêm cột "Điều khoản TCVN". Các sổ BM-01, 02, 05, 09, 10 dùng chung khối "Biên bản rà soát" giống BM-06 Phần C.
- Quy ước tên bằng chứng EVD-… đã có, giữ nguyên.

**B4. Căn cứ phải ghi đến điều khoản**
- QT-03 đang ghi "TCVN 14423:2026, nhóm yêu cầu quản lý vận hành", QT-02 ghi chung "TCVN 14423:2026"; như vậy không truy được điều khoản.
- TPL mục 3 nên có dòng "TCVN 14423:2026 cấp độ 3: 5.x.2.y…". Bảng mục 8 "Hiện trạng" nên có cột điều khoản để khớp với bảng A.

**B5. "Hoặc phương án tương đương" và "dựa trên kết quả đánh giá rủi ro"**
- Nhiều điều khoản cho phép dùng biện pháp tương đương hoặc chọn giá trị theo đánh giá rủi ro: 5.4.2.4, 5.4.2.7, 5.5.2.2, 5.6.2.2b, 5.11.2.3, 5.12.2.4e.
- Phần "ngoại lệ" cuối mục 6 của TPL nên ghi: biện pháp thay thế, lý do, mã rủi ro trong BM-10, người duyệt.

**B6. Gắn trách nhiệm.** Tài sản, tài khoản, phần mềm phải có cá nhân hoặc bộ phận chịu trách nhiệm (5.2.2.1b, 5.3.2.1b, 5.6.2.1c). Mọi sổ cần cột "Người/bộ phận phụ trách". Phần lớn sổ đã có cột này; BM-06 Phần A còn thiếu cột "Phòng ban".

**B7. Phạm vi cấp độ.** TPL mục 2 nên ghi rõ quy trình áp cho HTTT cấp độ nào. Nếu BM-01 xếp một sản phẩm cấp 3 (ví dụ iNET Portal), toàn bộ bảng A áp cho sản phẩm đó.

---

## C. Đề xuất bổ sung (ưu tiên mở rộng tài liệu sẵn có)

### C1. Mở rộng tài liệu sẵn có

| Tài liệu | Mục/phần bổ sung | Đáp ứng |
|---|---|---|
| TPL | Trường "Chu kỳ rà soát", "Rà soát gần nhất/kế tiếp"; bảng "Lịch định kỳ"; cột "Điều khoản TCVN" ở mục 3, 7, 8; mục ngoại lệ/biện pháp tương đương | B1–B5 |
| QT-01 | Luồng thuê khoán bên ngoài (hợp đồng, cam kết bảo mật, bàn giao mã nguồn hoặc chứng chỉ độc lập/kiểm thử xâm nhập, cam kết pháp lý); giai đoạn Thiết kế bắt buộc sơ đồ luồng dữ liệu và phân loại dữ liệu; giai đoạn Kiểm thử nêu bộ kiểm tra bảo mật tối thiểu; nghiệm thu có bên độc lập giám sát và chủ quản HTTT phê duyệt | 5.17.2.1c, 5.4.2.6, 5.4.2.1, 5.17.2.4, 5.12.2.3 |
| QT-02 | Mục "Yêu cầu bảo mật bắt buộc của sản phẩm": chính sách mật khẩu (08/14 ký tự, đổi lần đầu, quản trị 02 tháng, không trùng 10 lần trước); MFA cho quản trị; khóa phiên ≤15/≤05 phút; khóa sau ≤05 lần sai, mở khóa khẩn cấp; timeout, giới hạn kết nối; băm mật khẩu, mã hóa trường nhạy cảm, TLS; kiểm tra đầu vào và đầu ra | 5.6.2.2, 5.6.2.4, 5.5.2.2, 5.12.2.4, 5.4.2.4, 5.17.2.3 |
| QT-03 | Luồng vá thư viện/runtime: đánh giá tác động và cách hoàn tác bắt buộc với sản phẩm có dữ liệu quan trọng | 5.7.2.2 |
| QT-04 | Mở phạm vi ra mọi tài khoản BP-DEV quản lý (GitLab, CI, quản trị sản phẩm, CSDL, service account). Bổ sung: vô hiệu hóa sau 45 ngày; xử lý tài khoản mặc định; duyệt tài khoản dùng chung; tách tài khoản quản trị; chính sách mật khẩu cho nhân sự; quy trình xin truy cập dữ liệu production; rà phân quyền dữ liệu 06 tháng; truy cập từ xa qua VPN + MFA + giới hạn IP; checklist offboarding | 5.6.2.1–5.6.2.4, 5.4.2.1c-d, 5.12.2.5, 5.14.2.2b-c |
| QT-05 | Chuẩn mã hóa khi lưu và khi truyền; mã kiểm tra nguyên vẹn; các trường hợp bắt buộc ký số khi trao đổi dữ liệu quan trọng (theo quy định của Ban ATANM) | 5.4.2.4a-b, 5.4.2.5, 5.4.2.8 |
| QT-06 | Chu kỳ rà soát 06 tháng; quét toàn bộ 06 tháng/lần; bước kiểm tra lại sau khắc phục; kênh tiếp nhận báo cáo lỗ hổng từ bên ngoài (có thể chuyển nội dung SECURITY.md từ QT-02 sang); danh sách runtime/thư viện/kho gói được phép và danh sách ngoại lệ; Phụ lục "Kiểm thử xâm nhập sản phẩm" | 5.7.2.1, 5.17.2.2, 5.3.2.2, 5.3.2.3, 5.18 |
| QT-07 | Cấu hình chuẩn ứng dụng (tắt debug/endpoint thừa, header, TLS, tách cổng/tên miền quản trị); trường log tối thiểu; lưu ≥03 tháng; đẩy về kho log tập trung/SIEM; đồng bộ thời gian; rà log 06 tháng; rà ngưỡng cảnh báo 06 tháng; danh sách sản phẩm được giám sát | 5.5.2.1, 5.13.2.3b, 5.8.2.1, 5.13.2.1, 5.13.2.5 |
| QT-08 | Người chính và người dự phòng; xác minh danh bạ hằng năm; liên hệ nhà cung cấp và bên thuê khoán khi xử lý; lịch và hồ sơ diễn tập | 5.16.2.1, 5.16.2.3, 5.16.1 |
| QT-09 | Cột phương pháp sao lưu; dữ liệu cấu hình ứng dụng; sao lưu tự động; quy tắc 3-2-1; mã kiểm tra nguyên vẹn; định danh, phiên bản bản sao lưu; hạ tầng tách biệt | 5.11.2.1–5.11.2.4, 5.4.2.5 |
| QT-10 | Thang 4 mức nhạy cảm; tách môi trường cho dữ liệu nhạy cảm cao; đánh giá và phân loại nhà cung cấp trước khi tích hợp | 5.4.2.1, 5.4.2.7, 5.15 |
| BM-01 | Cột phiên bản production, giấy phép, HTTT thành phần, mức nhạy cảm (1–4), liên kết sơ đồ luồng dữ liệu; **Phần C "Tài sản thông tin theo sản phẩm"** (tài sản, mức, chủ sở hữu, nơi lưu, mã hóa, thời hạn lưu); Phần B ghi chu kỳ năm | 5.3.2.1, 5.3.2.3, 5.4.2.2, 5.4.2.6 |
| BM-02 | Đổi thành "Sổ thành phần phần mềm và EOL": ghi mọi runtime/framework/base image, thêm cột "Được phép / Ngoại lệ" và biện pháp kiểm soát cho ngoại lệ | 5.3.2.1–5.3.2.3 |
| BM-05 | Cột "Ngày kiểm tra lại, kết quả"; nguồn ghi rõ mã đợt kiểm thử xâm nhập hoặc báo cáo bên ngoài | 5.7.2.1, 5.17.2.2, 5.18.2.2 |
| BM-06 | Phần A mở ra mọi loại tài khoản với đủ trường 5.6.2.1c; **Phần D "Ma trận quyền theo chức danh × tài sản thông tin"** | 5.6.2.1, 5.6.2.4, 5.4.2.3 |
| BM-08 | Dòng kiểm tra mã nguyên vẹn bản sao lưu trước khi khôi phục | 5.4.2.5, 5.11.2.1 |
| BM-09 | Cột phân loại nhà cung cấp, trạng thái, văn bản phạm vi trách nhiệm, ngày rà soát; thêm dòng cho bên thuê khoán | 5.15, 5.17.2.1c |
| BM-10 | Cột nguồn rủi ro, quyết định xử lý, rủi ro còn lại, phương án ứng phó, ngày cập nhật, đã thông báo cho; biên bản đánh giá hiệu quả kiểm soát hằng năm | 5.1.2.2–5.1.2.6 |
| BM-12 (+BM-11) | Dùng BM-12 làm biên bản nghiệm thu chung cho mọi luồng khi go-live lần đầu hoặc thay đổi lớn (kể cả L1); thêm chữ ký bộ phận độc lập giám sát và chủ quản HTTT phê duyệt; đính kèm kết quả kiểm tra bảo mật; thêm tiêu chí cho phần mềm thuê khoán | 5.12.2.3d-e, 5.17.2.4, 5.17.2.1c |

### C2. Tài liệu mới (giữ tối thiểu)

| Đề xuất | Lý do không gộp vào tài liệu cũ |
|---|---|
| **DEV-BM-13 "Kế hoạch, phê duyệt và đánh giá sau kiểm thử xâm nhập"** (phạm vi, thời gian, phương pháp, đầu mối, hành vi cấm, cách phản ứng, xử lý dữ liệu thu được; phần đánh giá hiệu quả biện pháp sau kiểm thử) | 5.18.2.1 yêu cầu phê duyệt từng đợt theo các trường cụ thể và 5.18.2.3 yêu cầu đánh giá sau mỗi đợt; BM-05 chỉ theo dõi lỗ hổng. Nếu Ban ATANM đã có chương trình cấp công ty thì BM-13 dẫn chiếu, QT-06 chỉ cần phụ lục |

Các nội dung sau **không cần tài liệu riêng**:
- Chính sách mật khẩu: đặt trong QT-04 (nhân sự dùng) và QT-02 (sản phẩm phải thực thi). Nếu công ty đã có chính sách chung thì dẫn chiếu (?).
- Danh sách phần mềm được phép: dùng BM-02 sau khi mở rộng.
- Danh sách tài sản thông tin: BM-01 Phần C.
- Luồng dữ liệu: sơ đồ trong docs/ của repo, liên kết từ BM-01.
- Mã hóa, chữ ký số: đưa vào QT-05.
- Quy trình quản lý rủi ro: dùng quy trình cấp công ty, BM-10 là đầu vào.

---

## D. Thống kê mức phủ

Tổng 63 dòng: 14 dòng ngoài phạm vi (13 Hạ tầng, 1 Nhân sự/Ban ATANM); 49 dòng có phần việc của BP-DEV.

| Mức phủ | BP-DEV chủ trì (9) | Phối hợp, tính phần BP-DEV (40) | Cộng (49) |
|---|---|---|---|
| Đã thể hiện | 2 (5.17.2.3, 5.18.2.2) | 2 (5.1.2.5, 5.16.2.2) | 4 |
| Một phần | 6 (5.4.2.3, 5.4.2.6, 5.12.2.3, 5.17.2.1, 5.17.2.2, 5.17.2.4) | 30 | 36 |
| Chưa thể hiện | 1 (5.4.2.5) | 8 (5.1.2.6, 5.4.2.8, 5.5.2.1, 5.6.2.2, 5.12.2.5, 5.13.2.3, 5.18.2.1, 5.18.2.3) | 9 |

Lưu ý: cả 10 quy trình hiện chưa có trường chu kỳ rà soát (B1). Nếu tính yêu cầu này vào từng dòng thì 5.16.2.2 hạ xuống "Một phần".

---

## E. Khác biệt cấp độ 3 so với cấp độ 2 có ảnh hưởng tới BP-DEV

| Nội dung | Cấp độ 2 (mục 4) | Cấp độ 3 (mục 5) |
|---|---|---|
| Phát triển ứng dụng an toàn, kiểm thử xâm nhập | Không có mục riêng; chỉ có 4.3.2.3 phần mềm thuê khoán | Mục mới 5.17 và 5.18; yêu cầu thuê khoán chuyển vào 5.17.2.1c |
| Quản lý rủi ro | Chỉ có quy trình và rà soát năm (4.1) | Thêm các bước xác định (gồm bên thứ ba), đánh giá, xử lý, giám sát, truyền thông (5.1.2.2–5.1.2.6) |
| Tài sản thông tin | Kiểm tra phân quyền dữ liệu 01 lần/năm; chỉ mã hóa khi lưu | 01 lần/06 tháng; mã hóa cả khi truyền, quản lý vòng đời khóa; mới thêm 5.4.2.5–5.4.2.8 (nguyên vẹn, luồng dữ liệu, tách môi trường, chữ ký số) |
| Danh sách phần mềm được phép | Không có | Mới 5.3.2.2, bao gồm thư viện và đoạn mã |
| Tài khoản | Rà danh sách 01 lần/năm; quản trị đổi mật khẩu 02 tháng | Rà 01 lần/06 tháng; quản trị phải MFA, không trùng 10 mật khẩu trước; quản lý tài khoản tập trung |
| Lỗ hổng | Rà quét, rà quy trình 01 lần/năm | 01 lần/06 tháng; vá qua máy chủ vá tập trung |
| Nhật ký | Lưu ≥01 tháng, rà 01 lần/năm, không bắt buộc SIEM | Lưu ≥03 tháng, rà 01 lần/06 tháng, thêm log tiến trình, bắt buộc SIEM và lưu tập trung |
| Sao lưu | Không bắt buộc tự động, 3-2-1, mã hóa | Bắt buộc tự động, 3-2-1, mã hóa dữ liệu quan trọng, lưu trữ tập trung |
| Kiểm thử, nghiệm thu | Có nhân sự chịu trách nhiệm | Có bộ phận chịu trách nhiệm; bên/bộ phận độc lập giám sát; báo cáo nghiệm thu do chủ quản HTTT phê duyệt |
| Kiểm soát truy cập | Chỉ chiều vào | Thêm chiều ra, giới hạn kết nối đồng thời, kiểm soát người dùng vào dịch vụ nội bộ |
| Giám sát | Không có mục riêng | Mục mới 5.13: tách cổng quản trị ứng dụng, chỉnh ngưỡng cảnh báo 06 tháng |
| Ứng phó sự cố | Không yêu cầu diễn tập | Thêm "định kỳ tổ chức diễn tập" (5.16.1) |

---

## F. Ghi chú khác khi đọc mock

- **Kiểm tra từ khóa cấm:** mock không nhắc tới AI. Chuỗi "ai" chỉ xuất hiện với nghĩa tiếng Việt "ai làm", "ai vận hành".
- **Tên đơn vị chưa thống nhất:** nhiều chỗ ghi "BP Công Nghệ" và "người phụ trách BP-DEV", trong khi TPL và tên bộ tài liệu dùng "BP Phát triển sản phẩm" (BP-DEV, thuộc Phòng Nền tảng). Cần thống nhất trước khi điền nội dung thật.
- **Mã tài liệu công ty chưa đối chiếu được:** mock dẫn chiếu OPS-09/10/12/13/16, CMP-07/08, GOV-03, Sổ 7 RSK nhưng các tài liệu này không có trong phạm vi đọc, nên chưa xác nhận được (?).
