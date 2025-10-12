# 📘 Báo cáo phạm vi và trách nhiệm của FE Team trong dự án DNS Proxy + WAF

## 🧭 1. Mục tiêu

FE Team chịu trách nhiệm **xây dựng giao diện cấu hình và giám sát hệ thống DNS Proxy & WAF** cho khách hàng,  
giúp người dùng có thể thao tác trên trình duyệt để quản lý domain, bản ghi DNS, WAF rules, SSL và thống kê traffic.  
Mọi xử lý kỹ thuật (DNS, SSL, WAF engine, proxy routing) được đảm nhiệm bởi BE hoặc Infra.

---

## 🧩 2. Phạm vi trách nhiệm của FE Team

### 🎨 2.1 Giao diện & Trải nghiệm người dùng (UI/UX)

- Thiết kế và phát triển UI theo template.
- Triển khai các trang quản lý domain, record, SSL, WAF, cache, thống kê...
- Cung cấp UX trực quan cho người dùng thao tác và theo dõi trạng thái cấu hình.
- Xử lý các trạng thái hiển thị: loading, success, error, warning, validate.

### 🔌 2.2 Giao tiếp với API BE

- Kết nối và gọi API qua Axios theo chuẩn JSON.
- Quản lý token đăng nhập, xác thực phiên người dùng.
- Hiển thị dữ liệu trả về từ BE (đã qua xử lý logic).
- Không xử lý nghiệp vụ xác thực domain, DNS proxy hoặc WAF engine.

### 🧠 2.3 Quản lý trạng thái ứng dụng

- Sử dụng Pinia để quản lý dữ liệu domain, record, rules, logs.
- Đồng bộ dữ liệu khi thao tác nhiều tab hoặc module.
- Không lưu trữ dữ liệu thực tế của hệ thống (state chỉ mang tính tạm thời).

### 📈 2.4 Giám sát & hiển thị dữ liệu thống kê

- Hiển thị biểu đồ traffic, log, request hit rule.
- Cung cấp bộ lọc và biểu đồ trực quan theo dữ liệu BE cung cấp.
- Không thu thập log hoặc xử lý thống kê thực tế.

---

## 🚫 3. Phạm vi **không thuộc trách nhiệm của FE Team**

| Hạng mục                            | Chịu trách nhiệm | Ghi chú                                                             |
|-------------------------------------|------------------|---------------------------------------------------------------------|
| **Xác minh domain (DNS ownership)** | Backend          | FE chỉ hiển thị trạng thái                                          |
| **Đồng bộ DNS xuống Data Plane**    | Backend / Infra  | Liên quan hệ thống DNS                                              |
| **Xử lý logic WAF & Rate limit**    | Backend          | FE không kiểm tra request thật                                      |
| **Sinh và quản lý SSL**             | Backend / Infra  | FE chỉ hiển thị kết quả                                             |
| **ModSecurity & Managed Rules**     | Backend / Infra  | FE không tham gia cấu hình rule engine                              |
| **Quản lý Upstream & WebSocket**    | Backend / Infra  | FE chỉ cấu hình hiển thị                                            |
| **Log và lưu trữ request thật**     | Backend / Data   | FE chỉ visualize (hiển thị lại dữ liệu đã được BE phân tích, xử lý) |
| **Proxy Routing**                   | Backend / Infra  | FE không xử lý network-level                                        |
| **IP filtering**                    | Backend / Infra  | Ngoài phạm vi L7 của FE, chỉ cấu hình rule filter qua API           |

---

## 📦 4. Deliverables (Đầu ra của FE Team)

| Hạng mục                     | Mô tả                                                                             |
|------------------------------|-----------------------------------------------------------------------------------|
| **Dashboard tổng quan**      | Trang hiển thị danh sách domain, zone, trạng thái xác minh, SSL, thống kê traffic |
| **Module Record Manager**    | Cho phép thêm/sửa/xoá bản ghi DNS, bật/tắt proxy                                  |
| **Module WAF & Rate Limit**  | Giao diện cấu hình rule, sắp xếp thứ tự, hành động (Allow, Block, Log)            |
| **Trang giám sát**           | Hiển thị logs, biểu đồ traffic, WAF rule hits                                     |
| **Module cấu hình nâng cao** | Cache, WebSocket, Upstream                                                        |
| **Bộ thông báo & xử lý lỗi** | Chuẩn hóa response từ API, hiển thị thân thiện                                    |
| **Responsive UI**            | Đảm bảo hoạt động tốt trên PC, tablet, mobile                                     |

---

## 📊 5. Mục tiêu gốc của FE hiểu ở mức hợp lý (không vượt ranh giới trách nhiệm)

| Mức độ hiểu biết                           | Lợi ích                                                                                    |
|--------------------------------------------|--------------------------------------------------------------------------------------------|
| **Hiểu rõ cấu trúc dữ liệu API**           | FE map dữ liệu chính xác, tránh lỗi hiển thị hoặc sai trạng thái.                          |
| **Hiểu luồng xử lý tổng thể (high-level)** | FE biết thời điểm hiển thị “Pending / Applying / Error”, tránh confuse UX.                 |
| **Hiểu giới hạn BE**                       | Không thiết kế tính năng FE vượt ngoài khả năng BE (ví dụ: auto rollback khi chưa có API). |
| **Hiểu các trạng thái đồng bộ**            | Hiển thị UI phù hợp (disable nút Apply khi đang Pending chẳng hạn).                        |

👉 Như vậy, FE nên hiểu BE làm gì (hiểu mục đích, đầu vào và đầu ra của từng API hoặc luồng xử lý), chứ không phải hiểu
cách BE làm. (Đây là vấn đề triển khai nội bộ, có thể thay đổi bất kỳ lúc nào. Nếu FE biết và phụ thuộc vào cách BE làm,
thì khi BE đổi cách triển khai (để tối ưu, refactor, scale…) FE sẽ bị ảnh hưởng theo. FE sẽ dần “gắn chặt” với BE → mất
tính độc lập phát triển)

---

## ⚠️ 6. Lưu ý nên tránh khi FE hiểu quá sâu (deep backend logic)

| Nguy cơ                        | Mô tả                                                           | Hậu quả                                   |
|--------------------------------|-----------------------------------------------------------------|-------------------------------------------|
| **Mất ranh giới trách nhiệm**  | FE cố "mô phỏng" logic BE hoặc đưa logic BE lên UI.             | Dễ sinh lỗi không đồng nhất giữa UI & BE. |
| **Phải phụ thuộc chặt với BE** | FE thay đổi theo từng chi tiết BE (schema, workflow).           | Mỗi lần BE đổi, FE phải cập nhật theo.    |
| **Sai hướng thiết kế**         | FE cố xử lý phần “business logic” thay vì chỉ hiển thị dữ liệu. | BE mất kiểm soát quy trình nghiệp vụ.     |
| **Giảm bảo mật**               | FE "biết" quá nhiều endpoint hoặc cơ chế nội bộ.                | Tăng rủi ro lộ logic / tấn công API.      |

### 💡 Cách quản lý ranh giới hiệu quả:

- FE hiểu ở mức business flow, không can thiệp implementation detail.
  (Hiểu các bước validate → apply → confirm, nhưng không cần biết cụ thể hệ thống sẽ làm gì.)

- BE xuất tài liệu API đầy đủ → FE dựa vào đó làm việc.

- FE & BE có API contract rõ ràng: input/output/schema/status code.

- Tổ chức họp hàng tuần - sync nhẹ giữa FE–BE để thống nhất các thay đổi luồng dữ liệu, tránh hiểu sai.

- Không cho FE truy cập trực tiếp logs, backend code, mà chỉ thông qua API response.
