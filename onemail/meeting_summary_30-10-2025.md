## 👥 Người tham dự

- trihd@inet.vn
- hobv@inet.vn
- dattqh@inet.vn

---

## 🧩 Chủ đề

**Tổng hợp và đánh giá các đề xuất cải tiến hệ thống OneMail**  
nhằm tối ưu trải nghiệm người dùng, cải thiện giao diện, tính năng bảo mật và khả năng tích hợp hệ thống.

---

## 🧾 Nội dung thống nhất

1. ✅ **Đổi chữ “New” nhấp nháy thành “Drive” trên Menu Bar**
    - ⚙️ Giải pháp: thay đổi label hiển thị trên frontend.
    - ⏱️ Áp dụng ngay.
    - 👤 Phụ trách: Dev Frontend.
    - 🔗 [#187](https://my.inet.vn/gitlab/project/61/issue/detail/187)

2. ✅ **Sửa lỗi label “số lượng” không giảm khi xóa danh sách email**
    - ⚙️ Giải pháp: đồng bộ lại giá trị count khi thực hiện thao tác xóa.
    - 👤 Phụ trách: Dev FE.
    - 🔗 [#188](https://my.inet.vn/gitlab/project/61/issue/detail/188)

3. ⚖️ **Gắn cờ email → Giữ nguyên, không đổi thành “gắn sao”**
    - ⚙️ Giải pháp: giữ theo chuẩn Outlook để đảm bảo đồng bộ UI.

4. ✅ **Sửa lỗi hiển thị email trên Mobile (bị lệch khung)**
    - ⚙️ Giải pháp: responsive lại layout UI, test đa thiết bị.
    - 👤 Phụ trách: Dev FE.
    - 🔗 [#189](https://my.inet.vn/gitlab/project/61/issue/detail/189)

5. ✅ **Bổ sung xác thực hai lớp qua Google Authentication**
    - ⚙️ Giải pháp: tích hợp OAuth Google Authenticator.
    - 👤 Phụ trách: Dev BE + FE.
    - 🔗 [#176](https://my.inet.vn/gitlab/project/61/issue/detail/176)

6. 🧩 **Hiển thị danh sách file đính kèm trong cuộc hội thoại**
    - ⚙️ Giải pháp đề xuất: tổng hợp list file ở đầu conversation view.
    - 👤 Phụ trách: Dev xử lý, phản hồi sau.

7. 🧩 **Hiển thị file đính kèm trực tiếp trong email**
    - ⚙️ Giải pháp: preview file trong conversation.
    - 👤 Phụ trách: Dev xử lý, phản hồi sau.

8. ✅ **Highlight kết quả tìm kiếm theo tiêu đề & nội dung**
    - ⚙️ Giải pháp: implement text-highlighting bằng regex.
    - 👤 Phụ trách: FE Dev.
    - 🔗 [#80](https://my.inet.vn/gitlab/project/61/issue/detail/80)

9. ✅ **Preview nội dung email như Outlook (3 cột)**
    - ⚙️ Giải pháp: thêm vùng xem trước (split view).
    - 👤 Phụ trách: FE Dev.
    - 🔗 [#83](https://my.inet.vn/gitlab/project/61/issue/detail/83)

10. ✅ **Cho phép chọn hàng loạt email để xóa sau khi tìm kiếm**
    - ⚙️ Giải pháp: enable multi-select mode trong search result view.
    - 🔗 [#80](https://my.inet.vn/gitlab/project/61/issue/detail/80)

11. ✅ **Gợi ý tìm kiếm theo email hoặc tiêu đề khi nhập từ khóa**
    - ⚙️ Giải pháp: autocomplete search suggestion.
    - 🔗 [#80](https://my.inet.vn/gitlab/project/61/issue/detail/80)

12. ✅ **Auto viết hoa ký tự đầu câu khi soạn email**
    - ⚙️ Giải pháp: xử lý bằng regex hoặc input event.
    - 🔗 [#190](https://my.inet.vn/gitlab/project/61/issue/detail/190)

13. ✅ **Bổ sung thêm ngôn ngữ (Trung, Hàn)**
    - ⚙️ Giải pháp: mở rộng i18n config.
    - 🔗 [#191](https://my.inet.vn/gitlab/project/61/issue/detail/191)

14. ✅ **Thêm chức năng quản lý phiên đăng nhập cá nhân (Admin/User)**
    - ⚙️ Giải pháp: thêm module quản lý thiết bị đăng nhập (session token).
    - 🔗 [#175](https://my.inet.vn/gitlab/project/61/issue/detail/175)

15. 🚫 **Tích hợp với phần mềm khác (Zapier/n8n)**
    - ⚙️ Lý do reject: chưa rõ ràng tập khách hàng.

16. 🧩 **Tạo avatar riêng cho mỗi tài khoản**
    - ⚙️ Giải pháp cần khảo sát thêm.
    - 👤 Chờ PM chốt.

17. 🧩 **Email thông báo lỗi gửi đi (bằng tiếng Việt, theo template)**
    - ⚙️ Giải pháp chờ PM chốt.

18. 🧩 **Ngôn ngữ bằng giọng nói (Speech-to-text)**
    - ⚙️ Giải pháp: tích hợp module STT (Google Speech API).
    - 👤 Chờ PM xử lý.

19. ⚠️ **Xem lại dung lượng lưu trữ thực tế (case sv.mkt@saovietco.vn)**
    - ⚙️ Giải pháp: audit usage + kiểm tra hệ thống Ceph.
    - 👤 Chờ PM xử lý.

20. ⚠️ **Nhiều email bị vào spam**
    - ⚙️ Giải pháp: kiểm tra cấu hình SPF, DKIM, DMARC.
    - 👤 Chờ PM xử lý.

21. ⚠️ **Hiện tượng gửi/nhận email chậm, bị block bởi Microsoft Mail**
    - ⚙️ Giải pháp: kiểm tra IP reputation + mail queue.
    - 👤 Chờ PM xử lý.

22. 🧩 **Notify tới người dùng Outlook khi có thay đổi**
    - ⚙️ Giải pháp: chưa có cơ chế push tới Outlook client.
    - 👤 Chờ PM xử lý.

23. 🧩 **Cập nhật lại phần hướng dẫn sử dụng email / nhóm email**
    - ⚙️ Giải pháp: rà soát lại nội dung cũ `/mya`, cập nhật UI mới.

24. 🚫 **Phát triển app mail riêng trên điện thoại (thay vì dùng web/outlook)**
    - ⚙️ Lý do reject: chi phí cao, chưa đủ user base.
