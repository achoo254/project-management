# 🧭 Phân tích & Tổng hợp Đề xuất Triển khai Mô hình DNS + Proxy

---

## 1. Tổng quan

Dự án DNS Proxy + WAF hướng đến việc:

- Tăng khả năng bảo vệ hạ tầng mạng và dịch vụ khách hàng ở tầng ứng dụng (Layer 7)
- Đảm bảo High Availability (HA) và Load Balancing giữa các khu vực triển khai
- Cho phép mở rộng quy mô linh hoạt (theo khu vực hoặc theo nhóm khách hàng)

Hai phương án hạ tầng hiện được đưa ra:

- **Đề xuất 1**: 3 cặp Proxy Servers, mỗi cặp triển khai ở 2 khu vực (6 server tổng)
- **Đề xuất 2**: 3 cặp Proxy Servers, mỗi cặp triển khai ở 3 khu vực (9 server tổng)

---

## 2. So sánh hai đề xuất triển khai

| Tiêu chí                                       | Đề xuất 1 (2 khu vực) | Đề xuất 2 (3 khu vực)    |
|------------------------------------------------|-----------------------|--------------------------|
| **Số lượng server tổng**                       | 6                     | 9                        |
| **Số khu vực triển khai**                      | 2                     | 3                        |
| **HA (High Availability)**                     | Có, 2 vùng dự phòng   | Tốt hơn, 3 vùng dự phòng |
| **Khả năng điều hướng gần nhất (geo-routing)** | Giới hạn              | Tối ưu hơn               |
| **Chi phí đầu tư ban đầu**                     | Thấp hơn              | Cao hơn                  |
| **Yêu cầu IP /24 riêng biệt**                  | 6 dải IP              | 9 dải IP                 |
| **Rủi ro vùng đơn lẻ**                         | Còn tồn tại           | Giảm đáng kể             |
| **Khả năng mở rộng (scalability)**             | Vừa phải              | Linh hoạt, tốt hơn       |

---

## 3. Phân tích lợi ích & hạn chế

### ✅ Lợi ích chung của cả hai đề xuất

- Mỗi khách hàng được gán vào 1 cặp Proxy Server → đảm bảo cân bằng tải & khả năng phục hồi khi 1 server lỗi
- Khi bị tấn công ở 1 dải IP, có thể chuyển người dùng sang dải khác để tránh ảnh hưởng lan rộng
- Phân chia rõ ràng giữa Control Plane (quản lý trung tâm) và Data Plane (xử lý request thực tế)

### ⚠️ Hạn chế

- Thiếu thông tin về tải thực tế, lượng khách hàng DNS đang hoạt động, nên chưa đánh giá được tính cần thiết của 3 khu
  vực
- Chưa làm rõ cơ chế chuyển đổi khi khu vực gặp sự cố (manual hay automatic failover)
- Chưa có thông tin về cache, backup và khả năng phục hồi DNS data nếu proxy layer tạm dừng

---

## 4. Các câu hỏi & đề xuất gửi team Infra/BE

Dưới đây là các câu hỏi cần được làm rõ để hoàn thiện mô hình triển khai.  
*(Mỗi mục là một đầu việc cần phản hồi chính thức từ Infra/BE)*

### ❓ 1. Cơ sở nào để xác định cần cấu hình như đề xuất (2 hay 3 khu vực)?

- Có thống kê cụ thể về số lượng khách hàng đang dùng DNS iNET không?
- Hiện tại DNS có tỷ lệ tải / query per second (QPS) trung bình bao nhiêu?
- Có log hoặc metric nào chứng minh 2 khu vực hiện tại chưa đủ đáp ứng HA?

>> Trả lời: Hệ thống được thiết kế với ít nhất 2 khu vực để đảm bảo HA, và mở rộng theo chiều ngang. Nhưng để đảm bảo HA ở mức tối đa thì cần 3 khu vực

### ❓ 2. Cơ chế khi hệ thống bị tấn công hoặc DNS bị nghẽn

- Khi một khu vực hoặc dải IP bị tấn công (ví dụ DDoS), hệ thống có tự động chuyển vùng (auto
  failover) cho user không?
- Nếu có, thời gian chuyển vùng trung bình là bao lâu?
- Có cảnh báo (alert) cho khách hàng về tình trạng "DNS degradation" không?

>> Trả lời: Không, cái này ở trang admin. Tương tự như CloudFlare.

### ❓ 3. Cơ chế phản ứng khi Proxy Layer hoặc DNS Resolver gặp sự cố

- Phía khách hàng có thể tự chuyển thủ công sang server khác (qua UI/Portal) hay phải do hệ thống xử lý?
- Nếu DNS Proxy service bị down, dữ liệu hiển thị trong giao diện quản lý:
    - Có được cache từ bản ghi gần nhất (read-only)?
    - Có backup hoặc phương án "disable proxy" để khách hàng vẫn thao tác được?

>> Trả lời: Có thể xảy ra nếu toàn bộ khu vực bị down cùng 1 lúc

### ❓ 4. Các dịch vụ liên quan

- Các dịch vụ như Redis, MongoDB, Control Plane được triển khai theo cơ chế nào:
    - Replication hay Sharding? 
      - Replication: sao chép toàn bộ dữ liệu giữa nhiều node (bản sao). Mục tiêu: sẵn sàng cao (high availability) và đọc phân tán.
      - Sharding: chia dữ liệu theo key sang nhiều node (mỗi shard giữ phân đoạn dữ liệu). Mục tiêu: mở rộng dung lượng / throughput khi dữ liệu lớn hoặc write-heavy.
    - Có giám sát failover và khôi phục tự động không?
      - Health checks & heartbeat: mỗi node phải báo sống/chết.
      - Automatic failover: nếu primary chết → replicate một secondary thành primary tự động. (Ví dụ: Mongo ReplicaSet election, Redis Sentinel election).
      - Monitoring + alerting: metrics quan trọng: replication lag, query latency, error rate, node CPU/memory, network packet loss. Cảnh báo qua Slack/Email/Pager khi vượt ngưỡng.
      - Recovery (self-heal): node chết được tái khởi động/replicated lại và tự sync dữ liệu.
      - Chaos testing / runbooks: có đường dẫn thao tác tay khi auto-failover không thành công.
    - Có cần Redis Sentinel / Mongo ReplicaSet giữa các khu vực không?
      - Redis Sentinel: quản lý election (chọn master khi master chết) và cảnh báo. Nếu triển khai Sentinel/replica trải qua nhiều khu vực (region) thì:
        * Lợi: nếu toàn bộ 1 region sập, region khác có replica và Sentinel sẽ promote → hệ thống sống tiếp.
        * Hại: độ trễ mạng giữa region lớn gây ra heartbeat chậm, tăng nguy cơ election sai (split-brain) hoặc false failover; replication asyncronous có thể dẫn tới dữ liệu mất mát (writes chưa replicate).
 
      - ReplicaSet across regions: hoàn toàn khả thi — MongoDB hỗ trợ replica nodes đặt ở nhiều region. Nhưng:
        * Lợi: primary nằm ở region chính → nếu region chính down, election có thể promote node ở region khác → HA global.
        * Hại: Nếu máy chính (primary) ở một khu vực, mà các bản sao (secondary) ở xa nhau, khi mạng giữa các khu vực chập chờn → việc “chọn máy chính mới” sẽ rắc rối, có thể khiến hệ thống tạm ngưng ghi dữ liệu.

>> Trả lời: Các service này đều được cấu hình cluster để đảm bảo HA

---

## 5. Góc nhìn từ phía FE Team

### FE team không can thiệp tầng mạng (L3–L4), tuy nhiên có các yêu cầu phối hợp:
- FE cần API thống nhất để hiển thị trạng thái domain, proxy, rule, và quá trình apply
- Đề nghị có môi trường LAB nội bộ để mô phỏng:
    - Kịch bản khách hàng bị chặn/tấn công
    - Trạng thái chuyển vùng hoặc proxy down
- FE sẽ visualize dữ liệu log thực từ backend (không xử lý network-level)

📌 **FE đề xuất được thử nghiệm nội bộ (sandbox)** để kiểm tra giao diện & phản ứng của hệ thống khi có sự cố hoặc
failover giả lập.

---

## 6. Kết luận & hướng phối hợp

- Cần Infra/BE cung cấp bản thống kê sử dụng DNS và mô hình failover (cách phát hiện lỗi, cách chọn máy chủ dự phòng, cách khôi phục khi máy chủ chính hoạt động trở lại) hiện có
- Hai đề xuất (2 khu vực và 3 khu vực) đều khả thi, nhưng cần chứng minh về tải thực tế và HA để chọn phương án
  tối ưu
- FE team sẽ chuẩn hóa UI & API visualization
- Đề nghị có buổi thử nghiệm LAB nội bộ, mô phỏng các tình huống tấn công hoặc nghẽn DNS để đánh giá mô hình

---

## 📎 Tài liệu tham chiếu

[Đề xuất triển khai mô hình DNS Proxy - OneShield v2](https://kb.inet.vn/books/oneshield-v2/page/de-xuat-trien-khai-mo-hinh-dns-proxy)
