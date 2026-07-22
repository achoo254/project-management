# Giáo trình bóc tách — Buổi đào tạo Docker cơ bản (18-07-2026)

> Nguồn: `inet_2026-07-18_105914.srt` (~10.146 dòng SRT, ~2h36 phút). Transcript do speech-to-text tự động, nhiều lỗi phiên âm thuật ngữ kỹ thuật. Tài liệu này đã chuẩn hóa các lệnh/thuật ngữ Docker, giữ nguyên các ví von và phong cách giảng dạy của giảng viên. Các chỗ suy luận được đánh dấu **[suy luận]**; các chỗ transcript sai kiến thức kỹ thuật được đánh dấu **[Ghi chú: cần đính chính]**.

---

## 1. Tóm tắt buổi học

Đây là buổi 1 (trong chuỗi dự kiến 2-3 buổi) đào tạo nội bộ về Docker/container cho đội kỹ thuật iNET. Giảng viên mở đầu bằng việc điểm qua các nguồn tài liệu học Docker trên mạng, sau đó dẫn dắt học viên đi từ lịch sử tiến hóa hạ tầng (vật lý → ảo hóa → cloud → container) để giải thích *vì sao* container/Docker ra đời và giá trị của nó. Phần lý thuyết tập trung vào: kiến trúc Docker (daemon, registry, CLI), khái niệm image/layer, tính bất biến của container, cơ chế namespace/cgroups của Linux đứng sau container. Phần thực hành (chiếm phần lớn thời lượng) được giảng viên demo trực tiếp trên một máy chủ Linux đã cài Docker: từ `docker run hello-world`, quản lý image, đến vòng đời container (tạo, dừng, khởi động, đổi tên, xóa), truy cập vào bên trong container, xem log/event/tài nguyên. Đối tượng là các kỹ sư/DevOps của bộ phận công nghệ, một số đã có kinh nghiệm dùng Docker cơ bản (cài đặt, mở port) nhưng chưa thực hành sâu về vòng đời, log, registry riêng. Mục tiêu buổi học: xây dựng nền tảng khái niệm + thao tác tay để chuẩn bị cho các buổi sau về Dockerfile, Docker Compose, và Kubernetes.

---

## 2. Dàn ý theo trình tự giảng dạy

### 2.1. Mở đầu — tài liệu tham khảo (~00:00 – 00:03)
- Giảng viên điểm qua các trang học Docker trực tuyến (có trang tính phí 5-50 USD/khóa, một số giảng viên nổi tiếng người Ấn Độ chuyên đào tạo lập trình/AI).
- Tài liệu công ty chuẩn bị gồm 2 phần: tài liệu cơ bản (lý thuyết) và tài liệu thực hành (PDF hướng dẫn lab). **[Ghi chú: tên tài liệu nghe không rõ — "IntroDain và Pareto", tài liệu "công ty AdSense" — nhiều khả năng là tên bị phiên âm sai, không chắc chắn.]**
- Dự kiến: 2-3 buổi để phủ Docker cơ bản.

### 2.2. Lịch sử tiến hóa hạ tầng — vì sao có container (~00:05 – 00:14)
- **Khái niệm cốt lõi:** Chuỗi tiến hóa hạ tầng CNTT: **Vật lý → Ảo hóa (VMware, KVM, Hyper-V, Citrix) → Cloud (OpenStack, CloudStack) → Container (Docker, K8s)**. Giảng viên gọi bước container là mức "IaaS 1.5" — nằm giữa hạ tầng ảo hóa/cloud và nền tảng ứng dụng (PaaS).
- **Ví von:** Giảng viên đặt câu hỏi dẫn dắt kiểu Socratic: "Trước Cloud là gì?" → "Ảo hóa" → "Trước ảo hóa là gì?" → "Vật lý". Dùng cách hỏi ngược dòng lịch sử để học viên tự suy ra trình tự tiến hóa.
- **Lợi ích cốt lõi được nhấn mạnh:** tận dụng tài nguyên phần cứng. Ví dụ so sánh: "5 anh em có 5 máy chủ vật lý" so với "5 máy chủ ảo hóa" hoặc "5 máy chủ cloud" — độ giãn nở, triển khai nhanh hơn hẳn.
  - Ngày xưa: một máy vật lý chỉ được cấp cho **một mục đích sử dụng** (one physical server = one use case), hiệu suất khai thác CPU/RAM chỉ đạt mức thấp.
  - Ảo hóa/cloud: khai thác được tới **80-90%, thậm chí 90-95%** năng lực phần cứng.
  - So sánh mật độ người dùng: "một máy vật lý cho một công dụng" → ảo hóa "cho 100 người dùng" → Docker/microservice "cho 300 người dùng" — minh họa độ co giãn tăng dần qua từng lớp công nghệ.
- **Điểm nhấn về chi phí điện năng:** giảng viên nhấn mạnh giá trị tiết kiệm năng lượng của ảo hóa/cloud là yếu tố kinh tế quan trọng, không chỉ là "công nghệ cho vui".
- **Câu hỏi khảo sát kinh nghiệm:** giảng viên hỏi học viên đã từng cài Docker chưa, dùng ở mức nào (build image, dùng Docker Hub/registry tương tự, mở port...). Học viên phản hồi: chủ yếu dùng Docker ở mức cơ bản — mở port qua UFW/firewall.

### 2.3. Bài toán dẫn tới container (~00:15 – 00:20)
- **Khái niệm cốt lõi:** Trên một máy chủ vật lý truyền thống, chỉ chạy được **một môi trường tại một thời điểm** — ví dụ cài Java lên thì khó cài PHP cùng lúc (dù có các "trick" để né việc này). Bài toán: làm sao chạy đồng thời môi trường production lẫn môi trường test/dev trên cùng hạ tầng, và di chuyển ứng dụng linh hoạt giữa các môi trường (PC dev, staging, production, cloud public, tại chỗ khách hàng) mà không phải setup lại từ đầu.
- **Ví von đặc trưng:** Container giống như "hộp đen"/"thùng" (kiện hàng) chứa ứng dụng, có thể mang đi nhiều nơi khác nhau mà không cần lo về nền tảng bên dưới.
- **Ví von container vận tải (rất đặc trưng, giảng viên nhấn mạnh nhiều):** Kể lại câu chuyện thập niên 1960 khi vận chuyển hàng hóa quốc tế — trước đó mỗi người đóng gói hàng theo kiểu riêng (thùng, vải bọc...), không có tiêu chuẩn, gây lãng phí diện tích khi vận chuyển bằng ô tô/tàu thủy/tàu hỏa. Người ta phát minh ra container hàng hải (thùng container tiêu chuẩn - conex) để đóng gói hàng hóa **thống nhất, an toàn, tối ưu diện tích** trên mọi phương tiện vận chuyển. → Container phần mềm (Docker) áp dụng đúng ý tưởng này: đóng gói ứng dụng theo chuẩn để chạy nhất quán trên mọi hạ tầng (PC, staging, production, cloud, on-premise khách hàng).

### 2.4. Container là gì? Kiến trúc so với ảo hóa (~00:20 – 00:26)
- **Khái niệm cốt lõi:** So sánh kiến trúc:
  - Ảo hóa truyền thống: Hardware → Host OS → **Hypervisor** → nhiều máy ảo, mỗi máy ảo có **hệ điều hành khách (guest OS) riêng** → ứng dụng chạy trên guest OS.
  - Container: Hardware → Host OS → **Container runtime** (thay thế vị trí Hypervisor) → các container chứa ứng dụng, **dùng chung kernel/hệ điều hành của host**, không cần cài OS riêng cho từng container.
- **Điểm nhấn quan trọng [Định nghĩa cốt lõi]:** "Khi container chạy, hệ điều hành mà ứng dụng dùng chính là hệ điều hành dùng chung với host bên dưới" → nhờ vậy container **bỏ được một lớp hệ điều hành**, làm container **nhanh, nhỏ, nhẹ** hơn máy ảo rất nhiều (khởi động chỉ 1-2 phút, thực chất là một *process* của hệ điều hành host, không phải một máy ảo đầy đủ).
- Container = kỹ thuật đóng gói ứng dụng + các thư viện/dependency cần thiết để chạy nhất quán trên mọi môi trường. Công nghệ hiện thực hóa: Docker, Podman và nhiều công cụ khác (Docker là phổ biến nhất).

### 2.5. Chuẩn mở container — đề cập OCI (~00:22 – nhiều lần rải rác)
- Giảng viên có nhắc tới việc các công cụ container (Docker, Podman) đều **tuân theo một chuẩn phát triển chung**, nên image/registry có thể tương thích qua lại (Docker Hub, quay.io, GitHub Registry, GitLab Registry đều theo cùng chuẩn). Cụm từ trong transcript nghe thành **"Quảng Tây Nư"** — theo ngữ cảnh (chuẩn chung giúp Docker và Podman + các registry khác nhau tương thích với nhau, không phụ thuộc vendor) **[suy luận, cần đính chính]: nhiều khả năng giảng viên nói đến "OCI" (Open Container Initiative)** — chuẩn mở định nghĩa format image và runtime container mà Docker/Podman/containerd đều tuân thủ.
- **Điểm nhấn:** "Container chỉ phụ thuộc vào kernel, không phụ thuộc hệ điều hành cụ thể" — khác với package Linux truyền thống (Ubuntu chỉ dùng repo Ubuntu, không dùng repo RPM của RedHat) — container "quẩy vào đâu cũng được, không bị phụ thuộc".

### 2.6. Kiến trúc & quy trình vận hành Docker (~00:26 – 00:38)
- **Các thành phần kiến trúc Docker** (giảng viên vẽ/diễn giải theo hình minh họa):
  1. **Docker Host / Docker daemon (dockerd)** — máy chạy môi trường Docker, xử lý image và chạy container.
  2. **Docker Registry** — nơi chứa image; có 2 dạng: registry public bên ngoài (Docker Hub, quay.io...) hoặc tự biến máy của mình thành registry riêng (private registry).
  3. **Docker CLI** (`docker build`, `docker pull`, `docker run`...) — công cụ tương tác với Docker daemon.
- **Cách đọc sơ đồ kiến trúc (điểm nhấn về kỹ năng đọc hình):** Giảng viên nhấn mạnh học viên phải chú ý đường nét trong sơ đồ — đường liền nét là luồng `docker pull` (kéo image có sẵn từ registry về), đường nét đứt là luồng `docker build` (build image từ Dockerfile). Nhắc nhở: "người vẽ hình có ý đồ, phải dành thời gian quan sát mới hiểu đúng ý đồ đó".
- **Quy trình khi chạy ứng dụng:** nếu đã có image → build (`docker build`) hoặc pull (`docker pull`) → sau đó `docker run`. Đa số trường hợp thực tế là **pull** (kéo image có sẵn), chỉ khi cần tùy biến (customize) mới build từ đầu.
- **Khái niệm Layer:** Mỗi lần đóng gói lại ứng dụng (thêm tính năng, sửa code) sẽ tạo ra một **layer mới**, kế thừa các layer trước đó — tương tự cách quản lý version. Layer nhỏ/gọn hay không phụ thuộc vào người viết Dockerfile.
- **Ví dụ minh họa dung lượng nhỏ:** Một image WordPress hoàn chỉnh chỉ cần khoảng 60MB để chạy được — vì container chỉ chứa đúng phần cần thiết để chạy web (ví dụ không cần SSH server) — khác hẳn triển khai truyền thống nơi 70-80% hệ điều hành cài đặt là dư thừa không dùng đến.
- **Đề cập Podman + ví dụ PDF LaTeX:** Podman (của Red Hat) là công cụ tương tự Docker. Ví dụ container chạy chương trình PDFLaTeX để build báo cáo, xuất file ra ngoài, sau khi chạy xong thì container "biến mất" — không cần duy trì. Liên hệ tới khái niệm **serverless** — dịch vụ chạy xong việc thì tự kết thúc process, không cần tồn tại liên tục (liên hệ dùng cho các tác vụ xử lý đơn lẻ như xác nhận đơn hàng).
- **Giới thiệu Dockerfile:** có các lệnh cơ bản để build image (hẹn sẽ giảng chi tiết ở buổi Dockerfile sau).

### 2.7. Tính bất biến của container & dữ liệu (~00:34 – 00:36) — *Khái niệm quan trọng nhất buổi*
- **[Định nghĩa cốt lõi — nguyên văn ý đã chuẩn hóa]:** "Container là bất biến — một khi container được tạo ra, không sửa được nội dung bên trong nó theo nghĩa lâu dài. Mỗi lần chạy container là chạy đúng phiên bản (image) đó. Muốn nâng cấp/thay đổi thì phải **thay thế (replace)** bằng container mới từ image mới, chứ không sửa tại chỗ."
- **[Định nghĩa cốt lõi]:** "Docker không lưu trữ dữ liệu (state) của container — nó chỉ là môi trường chạy (runtime). Dữ liệu phải được ghi ra ngoài host qua **Docker volume** (hay gọi là container volume), nếu không khi container bị xóa thì dữ liệu cũng mất theo."
- Giảng viên lưu ý nên phân biệt rõ từ "Docker" dùng để chỉ cả công ty/công cụ lẫn khái niệm chung (volume, container) — dễ gây nhầm lẫn.

### 2.8. Cơ chế lõi bên dưới: namespace & cgroups (~00:40 – 00:44)
- **Khái niệm cốt lõi:** Container dùng các cơ chế cấp Linux kernel:
  - **Namespace** — cô lập không gian tài nguyên (network namespace, PID namespace, mount namespace...). Trong Linux có namespace cho hệ thống (system) và cho người dùng (user), giao tiếp qua các lời gọi hệ thống (syscalls).
  - **Control Groups (cgroups)** — cơ chế giới hạn/phân chia tài nguyên (CPU, RAM...) cho từng nhóm tiến trình.
  - **Union filesystem** — cơ chế lưu trữ theo layer của image.
- **Điểm nhấn kiến thức quan trọng:** "Công nghệ container **không hề mới** — các cơ chế namespace/cgroup đã có trong thiết kế Linux từ hàng chục năm trước (giảng viên ước tính 20-30 năm). Docker chỉ là công ty **hiện thực hóa** các cơ chế này bằng giao diện/CLI dễ dùng hơn, không phải phát minh ra khái niệm cô lập tiến trình."
- **Ví von/câu chuyện lịch sử (đặc trưng):** Kể chuyện về kỹ thuật cgroup ra đời từ nhu cầu thực tế cách đây ~30 năm: một tổ chức (liên quan tới hệ thống DNS) được đầu tư máy chủ 64 core nhưng phần mềm thời đó chỉ tận dụng được 8 core (phần mềm không chạy đa lõi tốt) → gây lãng phí tài nguyên đầu tư ("dự án không khai thác hết, nó chết đỏ" — ý nói lỗ ngân sách). Để giải quyết, đội kỹ thuật nghiên cứu ra kỹ thuật **chia nhỏ CPU theo cgroup**: mỗi cgroup chạy một tiến trình riêng biệt, cho phép nhiều "máy chủ ảo nhỏ" chạy trên cùng một máy vật lý. → Đây chính là nền tảng kỹ thuật mà Docker/container ngày nay dùng lại và đóng gói dễ dùng hơn.
- Liên hệ thêm: giống như trước khi có `iptables`/firewall command hiện đại, người quản trị Linux phải thao tác rất sâu ở tầng thấp để lọc gói tin; ngày nay chỉ cần vài lệnh nhẹ nhàng để "phủ lên" một lớp trừu tượng dễ dùng — Docker/container cũng đi theo hướng tương tự: che giấu sự phức tạp của namespace/cgroup bên dưới bằng CLI đơn giản.

### 2.9. Docker Registry và các công cụ liên quan (~00:26 – 00:28, rải rác)
- **Docker Hub**: nơi lưu trữ image chính thức của Docker, có phần miễn phí (public/community) và phần trả phí.
- Registry riêng (self-hosted): công ty có thể build/host registry riêng, thậm chí tích hợp pipeline scan bảo mật — khi Dev đẩy image lên, hệ thống tự scan **[suy luận: có thể là công cụ scan lỗ hổng bảo mật kiểu Trivy/Clair, transcript nghe thành "Quatch Virus"]** kiểm tra image có chứa gói lỗi thời/lỗi bảo mật (**[suy luận: transcript "CTI" có thể là "CVE" — Common Vulnerabilities and Exposures]**) hay không, và có tuân thủ quy tắc phát triển của team hay không.
- **Các registry nổi tiếng được nhắc tên:** Harbor (registry chuyên dụng mã nguồn mở), Nexus (Sonatype Nexus), quay.io (Red Hat), GitHub Container Registry, GitLab Container Registry.
- Giảng viên hỏi học viên đã từng tự dựng (host) một Docker Registry riêng chưa — học viên trả lời chưa.

### 2.10. Docker Compose, Docker Swarm, Kubernetes (~00:45 – 00:47)
- **Docker Compose:** dùng khi ứng dụng có nhiều thành phần (ví dụ 12-13 module/container) — thay vì viết 12 lệnh `docker run` riêng lẻ hoặc 12 Dockerfile, gom tất cả vào **một file duy nhất** (`docker-compose.yml`), chạy một lệnh để khởi động toàn bộ hệ thống.
- **Docker Swarm:** mô hình điều phối nhiều container **trên nhiều máy chủ** (khác với Docker/Compose vốn chạy trên 1 máy). Giảng viên lưu ý Swarm hiện nay ít được dùng, xu hướng chuyển hẳn sang **Kubernetes (K8s)**.
- **Kubernetes (K8s):** được mô tả là "lớp trừu tượng hóa phủ lên môi trường Docker" — công cụ điều phối container ở quy mô lớn, nhiều máy chủ. Sẽ học ở buổi sau (không đi sâu buổi này).
- Nhắc thêm các container runtime khác: LXC, systemd-nspawn (systemd), Podman... — chỉ liệt kê, khuyến nghị chọn công cụ phù hợp.

### 2.11. Yêu cầu môi trường & cài đặt (~00:47 – 00:48 lý thuyết, ~00:48 trở đi thực hành)
- Docker chạy được trên Windows, Mac, Linux — nhưng khuyến nghị chạy **native trên Linux** vì hiệu năng tốt hơn (Windows cần lớp ảo hóa/WSL2 trung gian). Production thường luôn chạy trên Linux.
- Yêu cầu kernel Linux tối thiểu 3.10 trở lên (thực tế hiện nay hầu hết distro dùng kernel 5.x/6.x nên không phải lo).

### 2.12. Thực hành: Cài đặt Docker (~00:48 – 00:59)
- **Điểm nhấn về kỹ năng/thói quen làm việc (rất được nhấn mạnh):** Trước khi làm bất cứ thao tác gì trên một máy chủ, luôn phải **kiểm tra thông tin trước** — IP, hệ điều hành, timezone — để chọn đúng lệnh cài đặt phù hợp. Đây là "thói quen" giảng viên muốn truyền đạt, không chỉ là kỹ thuật Docker thuần túy.
- Giảng viên chia sẻ cách bản thân **dùng AI (GPT)** để soạn nhanh tài liệu thực hành (chỉ mất ~5-10 phút thay vì cả buổi tối như trước đây) — nhưng luôn yêu cầu AI thêm **bước xác minh (verify)** sau mỗi bước cài đặt, và tài liệu AI sinh ra sẽ theo đúng "form"/thói quen làm việc quen thuộc của người yêu cầu (prompt càng rõ, kết quả càng khớp phong cách).
- **Trình tự cài đặt Docker (theo tài liệu, 8 bước cơ bản):**
  1. Kiểm tra IP, hostname, hệ điều hành trước khi cài (dùng lệnh kiểm tra OS — **[suy luận: transcript nghe thành "rsb", nhiều khả năng là `lsb_release -a` hoặc `cat /etc/os-release`]**).
  2. Cài các gói phụ thuộc / cập nhật hệ thống (`apt update`).
  3. Tạo/khai báo repository (GPG key + repo Docker) cho hệ điều hành tương ứng.
  4. Cài đặt Docker Engine (gói `docker-ce`).
  5. Kiểm tra version sau khi cài (`docker version`, `docker compose version`).
  6. Khởi động (start) dịch vụ Docker và kiểm tra trạng thái chạy.
  7. Kích hoạt (enable) Docker khởi động cùng hệ điều hành khi reboot.
  8. Kiểm tra tiến trình (process) Docker đang chạy; nếu không dùng user root, cần thêm user vào **group docker** để có quyền thực thi lệnh Docker mà không cần `sudo`.
- Sau khi cài, kiểm tra bằng `docker info` — quan sát: network mặc định được Docker tạo ra (trước khi cài chỉ có 2 "cặp mạng" localhost + vật lý; sau khi cài Docker sinh thêm network cầu nối/bridge riêng), số lượng container đang chạy, đường dẫn thư mục gốc lưu trữ layer/image (mặc định thường là `/var/lib/docker`).
  - **Lưu ý vận hành quan trọng:** thư mục lưu image/layer này sẽ phình to dần theo thời gian sử dụng — nên tính toán đặt nó ở phân vùng có dung lượng lớn (ví dụ tách riêng `/var/lib/docker` ra một disk/mount point riêng) ngay từ đầu.

### 2.13. Thực hành: Image cơ bản (~00:59 – 01:24)
- Chạy thử `docker run --rm hello-world` để xác nhận Docker hoạt động bình thường — ví như "print Hello World" để kiểm tra môi trường mới cài đặt.
- Giải thích cơ chế: khi chạy lệnh, Docker tìm image trong local cache trước, nếu không có sẽ **pull** từ Docker Hub (hoặc `quay.io` nếu dùng Podman).
- Giải thích khái niệm **digest/mã hash của image** — dùng để đảm bảo image tải về không bị giả mạo, đảm bảo tính toàn vẹn (mỗi lần build version mới sẽ có digest mới khác nhau).
- Kiểm tra image bằng `docker image ls` — thấy image `hello-world` chỉ chiếm dung lượng chưa tới 1MB.
- Demo `docker pull python` (không chỉ định tag → mặc định tải `latest`) và `docker pull python:3.11` (chỉ định version cụ thể) — nếu cần version khác (như 3.12) phải tra trên trang chủ Docker Hub để biết tag chính xác.
- **Minh họa chia sẻ layer (layer sharing):** kéo về nhiều version Python khác nhau (một ứng dụng dùng Python 3.11, một dùng Python 3.12...) — dù tưởng chừng tổng dung lượng phải cộng dồn (ví dụ ước tính 4.5GB) nhưng thực tế chỉ chiếm khoảng 1.7GB vì các image **dùng chung (share) các layer giống nhau**.
- `docker image inspect <image>` — xem toàn bộ metadata JSON của image (OS, kiến trúc CPU, lệnh chạy mặc định, các layer/digest...).
- `docker image inspect --format '{{.Os}} {{.Architecture}}' <image>` — kỹ thuật lọc field cụ thể bằng Go template thay vì đọc toàn bộ JSON dài, hữu ích khi cần script hóa qua nhiều image cùng lúc.
- `docker image history <image>` — xem lịch sử build/thay đổi của image, tương tự lịch sử version/commit; nhấn mạnh: hữu ích với các team **tự build image**, còn nếu chỉ tải image có sẵn về dùng thì ít khi cần đến lệnh này.
- `docker image tag <ten-cu> <ten-moi>` — đặt tag/tên mới cho image (ví dụ chuẩn hóa theo naming convention nội bộ, rút gọn tag).
- `docker image rm <image>` — xóa image.

### 2.14. Thực hành: Chạy container Nginx & vòng đời container (~01:24 – 01:59)
- Demo chạy container Nginx với lệnh dạng:
  `docker run -d --name <ten> --hostname <ten> --restart always -p 8080:80 nginx`
  - `-d`: chạy nền (detached).
  - `--name`, `--hostname`: đặt tên container và hostname bên trong container.
  - `--restart always`: chính sách tự khởi động lại khi container bị dừng ngoài ý muốn.
  - `-p 8080:80`: map port 8080 của host vào port 80 bên trong container.
- **Điểm nhấn về network binding:** nếu khai báo `-p 127.0.0.1:8080:80` thì chỉ truy cập được từ chính máy host (localhost); nếu bỏ phần địa chỉ IP (chỉ để `-p 8080:80`) thì Docker sẽ public ra tất cả interface mạng (`0.0.0.0`) — cho phép truy cập từ máy khác qua IP của server. Giảng viên chủ động sửa lại tài liệu mẫu (vốn dùng 127.0.0.1) để demo truy cập từ máy ngoài.
- Kiểm tra bằng `docker container ls` / `docker ps`, `docker container port <ten>` (xem port mapping), truy cập qua trình duyệt bằng `http://<ip-server>:8080` để thấy trang chào mừng mặc định của Nginx.
- **Quản lý vòng đời container ("container nó sinh ra, nó chạy và nó mất đi"):**
  - `docker container stop <ten>` — dừng container (trạng thái chuyển thành *Exited*, kiểm tra lại bằng `docker container ls -a` hoặc `docker ps -a`).
  - `docker container start <ten>` — khởi động lại container đã dừng (không mất container, giữ nguyên container instance).
  - `docker container pause <ten>` / `unpause` — tạm dừng xử lý tiến trình bên trong (container vẫn "chạy" theo nghĩa tồn tại nhưng không phản hồi request) — giảng viên nói bản thân ít dùng lệnh này, dùng trong ngữ cảnh đặc thù khi cần "đóng băng" tạm thời tiến trình.
  - `docker container rename <ten-cu> <ten-moi>` — đổi tên container, chỉ đổi "vỏ", không ảnh hưởng hoạt động bên trong.
  - `docker container rm <ten>` — xóa hẳn container (phải `stop` trước nếu đang chạy).
- **Truy cập vào bên trong container (2 cách):**
  1. Đứng từ ngoài quan sát: `docker container top <ten>` — xem các tiến trình (process) chạy bên trong container, giống lệnh `top` của Linux. Điểm nhấn: từ host, **không** thấy các process quản trị của host (ví dụ init/systemd) khi liệt kê `top` toàn hệ thống — vì container bị cô lập namespace tiến trình.
  2. Chui hẳn vào bên trong: `docker container exec -it <ten> /bin/sh` (hoặc `hostname`, hoặc lệnh bất kỳ) — mở phiên tương tác bên trong container. Sau khi vào, dấu nhắc lệnh (prompt) thay đổi để nhận biết đang ở trong container. Bên trong container: chạy `hostname`, `ip a` để thấy IP nội bộ khác với IP của host; dùng `ls` để thấy container tối giản (chỉ có thư mục cần thiết, không đầy đủ như một hệ điều hành full).
- **Demo "sửa nóng" (hotfix tạm thời) và minh chứng tính bất biến — phần thực hành quan trọng nhất:**
  - Vào bên trong container (`exec -it`), `cd` tới thư mục chứa file HTML mặc định của Nginx (`/usr/share/nginx/html/index.html`).
  - Dùng `echo "<nội-dung>" > index.html` (ghi đè) hoặc `echo "<nội-dung>" >> index.html` (ghi thêm/append) để sửa trực tiếp nội dung trang web.
  - `exit` để thoát khỏi container, quay lại reload trang web trên trình duyệt → thấy nội dung đã đổi (chứng minh sửa nóng có tác dụng tức thời).
  - **Nhấn mạnh:** đây chỉ là "phích tạm"/sửa nóng — **không phải cách làm đúng để thay đổi ứng dụng lâu dài**. Nếu muốn thay đổi nội dung/version một cách chính thức, phải sửa từ nguồn (Dockerfile/mã nguồn) rồi build lại image mới.
  - **Minh chứng bằng thực nghiệm (rất đáng nhớ để làm lab):** `docker container stop` → `docker container rm` (xóa hẳn container đã sửa nóng) → chạy lại đúng lệnh `docker run` ban đầu (dùng lại **cùng image** cũ, chưa build lại) → container mới được tạo ra → truy cập lại web → nội dung **trở về mặc định ban đầu**, thay đổi vừa sửa nóng biến mất hoàn toàn. → Chứng minh trực quan: "**image là bất biến**", container không lưu trạng thái/state.
- `docker container exec` có thể dùng ID rút gọn (chỉ cần gõ vài ký tự đầu của container ID thay vì gõ đầy đủ tên/ID).

### 2.15. Thực hành: Inspect, log, volume path (~01:59 – 02:23)
- `docker container inspect <ten/id>` — lệnh **rất quan trọng**, giảng viên nhấn mạnh sẽ phải dùng rất nhiều trong công việc thực tế. Trả về toàn bộ metadata JSON của container: trạng thái (State/Status), network/IP nội bộ, PID, cấu hình storage/volume mount, RestartPolicy, v.v.
- `docker container inspect --format '{{...}}' <ten>` — tương tự image inspect, lọc riêng field cần xem (ví dụ trạng thái running, RestartPolicy) thay vì đọc cả khối JSON dài.
- **Đường dẫn dữ liệu trên host:** dữ liệu/log của container thực chất được lưu trong các thư mục trên host, nằm dưới `/var/lib/docker/containers/<container-id>/...` (bao gồm file log dạng JSON — ví dụ `<id>-json.log`) và các thư mục volume tương ứng. Khi container bị xóa, đường dẫn này cũng biến mất theo (trừ khi dữ liệu được mount ra một volume/thư mục ngoài được quản lý riêng).
- **Phân biệt 2 loại log (điểm nhấn quan trọng):**
  1. **Log của container** — log thu được qua cơ chế Docker (stdout/stderr của tiến trình chính trong container), xem bằng `docker container logs`.
  2. **Log của ứng dụng bên trong** — ví dụ log riêng của Nginx (access/error log ở đường dẫn nội bộ như `/var/log/nginx/`), là log do chính ứng dụng ghi ra, độc lập với cơ chế log của Docker.
  - Giảng viên khuyến nghị: dữ liệu/mã nguồn ứng dụng (code, data) nên **mount ra ngoài container** qua volume — container chỉ nên chứa phần runtime, quan điểm "nhồi hết mọi thứ vào trong container" bị đánh giá là **sai lầm** trong thiết kế. Ví dụ thực tế giảng viên áp dụng: thư mục chứa code/app luôn nằm ngoài (host), container chỉ cấp quyền truy cập vào thư mục đó.
  - Giới thiệu công cụ log tập trung thực tế: **Vector** (vector.dev) và **VictoriaLogs** — các agent này khi cài lên máy sẽ tự nhận diện cấu trúc log của Docker và đọc thẳng, không cần người dùng phải tự mount/quản lý đường dẫn log thủ công.
- `docker container logs <ten>` — xem log container.
- `docker container logs -f <ten>` — theo dõi log real-time (follow), tương tự `tail -f`.
- `docker container logs --tail 20 <ten>` — chỉ xem N dòng log cuối cùng (ví dụ 20 dòng).
- **Demo tạo tải để quan sát log (rất trực quan cho lab):** mở 2 cửa sổ terminal song song — một chạy `docker container logs -f <ten>` để theo dõi, một chạy vòng lặp gửi 50 HTTP request liên tiếp vào container (mô phỏng bằng script/curl loop, có gắn ID request để dễ đối chiếu) — quan sát log tăng lên tương ứng theo thời gian thực. Giảng viên gợi ý: ngày nay có thể nhờ AI viết nhanh script giả lập nhiều request để test.
- `RestartPolicy` — xem trong kết quả inspect, các giá trị điển hình: `no` (mặc định), `always` (luôn tự khởi động lại khi bị dừng), `on-failure`, `unless-stopped` (chỉ khởi động lại khi bị reboot, không cố gắng restart liên tục khi bị stop chủ động) — ví như tính năng máy tính tự bật lại sau khi mất điện đột ngột.

### 2.16. Thực hành: Theo dõi tài nguyên & sự kiện (~02:27 – 02:35)
- **`docker stats`** *(transcript ghi sai thành "Docker Star" — đã đính chính)* — lệnh xem tài nguyên (CPU, RAM...) mà container đang sử dụng theo thời gian thực, tương tự lệnh `top`/`htop` nhưng cho container.
  - Giảng viên lưu ý: việc giới hạn tài nguyên cụ thể cho từng container (CPU limit, memory limit) trong Docker thuần thường ít được cấu hình chi tiết; đến khi học Kubernetes (K8s) mới thấy rõ cơ chế giới hạn tài nguyên bài bản hơn (resource requests/limits).
- **`docker events`** — theo dõi sự kiện của Docker daemon/container theo thời gian thực (start, stop, restart, kill...).
  - Demo: mở 2 terminal — terminal 1 chạy `docker events` (lọc theo container, ví dụ `docker events --filter container=<id>`), terminal 2 lần lượt thực hiện `docker container restart`, `docker container stop`, `docker container start` — quan sát terminal 1 xuất hiện các sự kiện tương ứng: *container restart*, *container kill*, *container stop*, *container start*.
  - **Lưu ý vận hành:** `docker events` **không lưu trữ vĩnh viễn** — theo giảng viên chỉ giữ khoảng 1.000-3.000 dòng sự kiện gần nhất trong bộ nhớ, không có cơ chế lưu trữ lâu dài mặc định (giảng viên tự nhận "khả năng phải tìm hiểu thêm" phần này, không chắc chắn 100%). Có thể lọc theo thời gian bằng option `--since` (ví dụ theo ngày cụ thể).
  - Ý nghĩa thực tế: khi một container bị restart/stop bất thường, đây chính là dấu hiệu ứng dụng đang gặp vấn đề — cần có cơ chế giám sát (log/event) bắt được các sự kiện này, ví dụ tích hợp Vector/VictoriaLogs để bắt sự kiện Docker gửi cảnh báo (ví dụ cảnh báo qua điện thoại/chat).

### 2.17. Chia sẻ kinh nghiệm cá nhân: dùng AI để tăng năng suất (~02:23 – 02:27, xen giữa phần thực hành)
- Giảng viên chia sẻ trải nghiệm cá nhân: trước đây viết tài liệu triển khai/thực hành phải tự mò mẫm, mất nhiều thời gian (kể chuyện "8 năm trước" từng phải viết thủ công tốn nhiều công sức). Nay dùng AI (GPT) để soạn tài liệu, có thể hoàn thành trong 5-10 phút.
- **Nguyên tắc khi dùng AI mà giảng viên áp dụng và truyền đạt:** mỗi bước cài đặt trong tài liệu do AI viết ra đều phải có **bước xác minh (verify)** kèm theo trước khi chuyển bước tiếp theo — không chấp nhận tài liệu chỉ liệt kê lệnh mà không có cách kiểm chứng.
- Liên hệ thuật ngữ AI: **"Human in the Loop"** — con người luôn phải nằm trong vòng lặp của quy trình làm việc lặp đi lặp lại, không giao phó hoàn toàn cho máy.
- Ví dụ thực tế được kể: triển khai một mô hình observability (giám sát) cho 4 máy chủ — nhờ AI viết tài liệu (hơn 50 trang, gồm cả IP planning, các bước kiểm tra) chỉ trong chưa đầy 10 phút, sau đó giao lại cho các thành viên khác trong nhóm triển khai theo tài liệu mà không cần trực tiếp hướng dẫn — rút thời gian triển khai 5 hệ thống từ dự kiến nửa tháng xuống còn 2 ngày.
- **Điểm nhấn/cảnh báo:** dù AI hỗ trợ nhanh, kỹ sư vẫn phải tự trải nghiệm/thực hành thật để không trở thành người chỉ biết "copy-paste" một cách thụ động — nếu không sẽ không nâng cao được năng lực thực sự.

### 2.18. Kết thúc buổi học (~02:35)
- Giảng viên tóm tắt: buổi 1 tập trung vào "nguyên lý" (sự ra đời của container, các điểm ưu việt) và một số kỹ thuật cài đặt/khởi tạo cơ bản, cùng các thông tin hỗ trợ công việc thực tế.
- Dừng lại ở "phần 16" trong tài liệu (theo đánh số mục lục nội bộ của tài liệu thực hành), hẹn tiếp tục ở buổi sau.
- Hỏi đáp cuối buổi: không có câu hỏi thêm từ học viên.

---

## 3. Toàn bộ lệnh Docker được nhắc tới

| Lệnh (cú pháp đã chuẩn hóa) | Mục đích | Ngữ cảnh trong buổi học |
|---|---|---|
| `docker version` | Xem phiên bản Docker client/server | Kiểm tra sau khi cài đặt |
| `docker compose version` | Xem phiên bản Docker Compose | Kiểm tra cùng lúc với `docker version` |
| `docker info` | Xem thông tin tổng quan môi trường Docker (số container, network, storage driver, thư mục gốc...) | Kiểm tra ngay sau khi cài, trước khi chạy container đầu tiên |
| `docker run --rm hello-world` | Chạy container test để xác nhận Docker hoạt động; `--rm` để tự xóa container sau khi chạy xong | Thực hành đầu tiên sau khi cài đặt |
| `docker image ls` (hoặc `docker images`) | Liệt kê các image có trên máy | Kiểm tra sau khi pull `hello-world`, sau khi pull Python |
| `docker pull <image>[:tag]` (vd: `docker pull python`, `docker pull python:3.11`) | Tải image từ registry (Docker Hub mặc định) | Demo tải image Python nhiều version, minh họa layer sharing |
| `docker image inspect <image>` | Xem chi tiết metadata của image (OS, kiến trúc, lệnh, lịch sử) | Sau khi pull Python, xem chi tiết image |
| `docker image inspect --format '{{.Os}} {{.Architecture}}' <image>` | Lọc field cụ thể từ metadata bằng Go template | Minh họa cách lấy nhanh 1-2 thông tin thay vì đọc cả JSON |
| `docker image history <image>` | Xem lịch sử build/thay đổi của image theo từng layer | Giải thích dành cho team tự build image |
| `docker image tag <ten-cu> <ten-moi>` | Gán tag/tên mới cho image | Chuẩn hóa naming convention nội bộ (vd `lab.inet/nginx`) |
| `docker image rm <image>` | Xóa image | Demo dọn dẹp image không cần dùng nữa |
| `docker run -d --name <ten> --hostname <ten> --restart always -p 8080:80 nginx` | Chạy container Nginx nền, đặt tên/hostname, tự khởi động lại, map port 8080 (host) → 80 (container) | Demo container thực tế đầu tiên của buổi học |
| `docker container ls` (hoặc `docker ps`) | Liệt kê container đang chạy | Kiểm tra container Nginx vừa tạo |
| `docker container ls -a` (hoặc `docker ps -a`) | Liệt kê tất cả container kể cả đã dừng | Kiểm tra container sau khi `stop` |
| `docker container port <ten>` | Xem port mapping của container | Xác nhận port 80 nội bộ ↔ 8080 bên ngoài |
| `docker container stop <ten>` | Dừng container | Bài lab vòng đời container |
| `docker container start <ten>` | Khởi động lại container đã dừng | Bài lab vòng đời container |
| `docker container pause <ten>` / `docker container unpause <ten>` | Tạm dừng/tiếp tục xử lý tiến trình bên trong container | Giới thiệu, ít dùng theo giảng viên |
| `docker container rename <ten-cu> <ten-moi>` | Đổi tên container | Minh họa đổi tên không ảnh hưởng hoạt động |
| `docker container rm <ten>` | Xóa container (đã dừng) | Minh họa mất dữ liệu khi container bị xóa |
| `docker container top <ten>` | Xem tiến trình chạy bên trong container (đứng từ ngoài) | Minh họa cô lập tiến trình (namespace) |
| `docker container exec -it <ten> /bin/sh` (hoặc `bash`, hoặc lệnh đơn như `hostname`) | Truy cập/tương tác trực tiếp bên trong container | Vào container để kiểm tra `hostname`, `ip a`, sửa file |
| `docker container inspect <ten>` | Xem toàn bộ metadata container (network, storage, PID, RestartPolicy...) | Lệnh được nhấn mạnh là "rất quan trọng, dùng nhiều sau này" |
| `docker container inspect --format '{{...}}' <ten>` | Lọc field cụ thể (vd trạng thái, RestartPolicy) | Tránh phải đọc toàn bộ JSON dài |
| `docker container logs <ten>` | Xem log của container | Bài lab log |
| `docker container logs -f <ten>` | Theo dõi log real-time (follow) | Demo cùng lúc với tạo tải 50 request |
| `docker container logs --tail 20 <ten>` | Xem N dòng log cuối | Giới thiệu option `--tail` |
| `docker stats` | Xem tài nguyên (CPU/RAM) container đang dùng theo thời gian thực | *(transcript: "Docker Star" — đã đính chính)* |
| `docker events` | Theo dõi sự kiện container real-time (start/stop/restart/kill) | Demo 2 terminal — 1 xem event, 1 tạo sự kiện |
| `docker events --filter container=<id>` | Lọc sự kiện theo container cụ thể | Cùng demo trên |
| `docker events --since <ngày>` | Lọc sự kiện theo mốc thời gian | Giới thiệu thêm, chưa demo sâu |

**Lệnh Linux/hệ thống liên quan được nhắc tới (không phải lệnh Docker nhưng dùng trong thao tác chuẩn bị):**

| Lệnh | Mục đích | Ghi chú |
|---|---|---|
| Kiểm tra IP/hostname/OS trước khi cài | Xác định thông tin máy chủ trước khi chọn lệnh cài phù hợp | **[suy luận]** transcript nghe không rõ ("rsb"), có thể là `lsb_release -a`, `hostnamectl`, hoặc `cat /etc/os-release` |
| `apt update` / cài `docker-ce` qua repo chính thức | Cài đặt Docker Engine trên Linux | Theo quy trình 8 bước tài liệu AI soạn |

---

## 4. Các demo / thao tác thực hành đã làm live

Dưới đây mô tả chi tiết từng demo để có thể tái hiện thành LAB độc lập.

### Demo 1 — Cài đặt Docker và kiểm tra môi trường
1. Kiểm tra IP, hostname, hệ điều hành của máy chủ Linux mục tiêu.
2. Cài đặt Docker theo tài liệu 8 bước (update hệ thống → tạo repo/GPG key → cài `docker-ce` → start service → enable service khi reboot → kiểm tra process).
3. Nếu không dùng root: thêm user hiện tại vào group `docker`.
4. Kiểm tra: `docker version`, `docker compose version`, `docker info`.
5. Quan sát trong `docker info`: network mặc định Docker tạo ra, thư mục gốc lưu image/layer (mặc định `/var/lib/docker`).

### Demo 2 — Container test đầu tiên (Hello World)
1. Chạy `docker run --rm hello-world`.
2. Quan sát: Docker tự động pull image `hello-world:latest` từ Docker Hub (do chưa có trong local cache), hiển thị digest hash xác thực.
3. Đọc output thông báo "chào mừng" xác nhận Docker hoạt động đúng.
4. Kiểm tra `docker container ls -a` → không thấy container (vì dùng `--rm`, container tự xóa sau khi chạy xong).

### Demo 3 — Quản lý image (pull, inspect, tag, xóa)
1. `docker pull python` (không chỉ định tag) → tự động lấy `latest`.
2. `docker pull python:3.11` → lấy đúng version chỉ định.
3. `docker image ls` → so sánh dung lượng, quan sát các image dùng chung layer với nhau (dung lượng tổng thực tế nhỏ hơn nhiều so với cộng dồn riêng lẻ).
4. `docker image inspect python:3.11` → xem toàn bộ metadata.
5. `docker image inspect --format '{{.Os}} {{.Architecture}}' python:3.11` → lọc riêng field OS/kiến trúc.
6. `docker image history python:3.11` → xem lịch sử layer.
7. `docker image tag python:3.11 lab.inet/python:3.11` → đặt tag mới theo naming nội bộ.
8. `docker image rm <tag-cu-khong-dung>` → xóa image không cần thiết.

### Demo 4 — Chạy container Nginx và quản lý vòng đời (LAB trọng tâm nhất buổi)
1. Chạy: `docker run -d --name docker-lab --hostname docker-lab --restart always -p 8080:80 nginx`.
2. Kiểm tra: `docker container ls`, `docker container port docker-lab`.
3. Truy cập `http://<ip-server>:8080` từ trình duyệt máy khác → xác nhận thấy trang chào mừng Nginx.
4. Thực hành vòng đời: `docker container stop docker-lab` → kiểm tra bằng `docker container ls -a` (trạng thái Exited) → `docker container start docker-lab` → kiểm tra lại web truy cập được.
5. Thực hành `docker container pause` / `docker container unpause` để quan sát khác biệt (container "sống" nhưng không phản hồi request).
6. Thực hành `docker container rename docker-lab docker-lab-2`.
7. `docker container top docker-lab-2` → xem tiến trình bên trong (đối chiếu để thấy không có tiến trình của host).
8. `docker container exec -it docker-lab-2 /bin/sh` → vào container, chạy `hostname`, `ip a` để so sánh với thông tin ngoài host.

### Demo 5 — Sửa nóng và minh chứng tính bất biến của image (LAB quan trọng để hiểu cốt lõi Docker)
1. Từ bên trong container (bước 8 ở trên), `cd /usr/share/nginx/html/`.
2. `echo "<tên của bạn>" > index.html` (ghi đè nội dung) hoặc dùng `>>` để ghi thêm dòng mới, không xóa nội dung cũ.
3. `exit` khỏi container, mở lại `http://<ip-server>:8080` → xác nhận nội dung trang web đã đổi theo nội dung vừa sửa.
4. `docker container stop docker-lab-2` → `docker container rm docker-lab-2` (xóa hẳn container đã bị sửa nóng).
5. Chạy lại đúng lệnh ở bước 1 của Demo 4 (dùng lại **cùng image nginx gốc**, chưa build lại gì cả) để tạo container mới.
6. Mở lại trình duyệt → quan sát: nội dung web **trở về mặc định ban đầu**, không còn dấu vết chỉnh sửa trước đó.
7. Kết luận rút ra cho học viên: image bất biến, container không lưu state; muốn thay đổi lâu dài phải sửa từ nguồn (Dockerfile) và build lại image.

### Demo 6 — Inspect, phân biệt log container và log ứng dụng
1. `docker container inspect docker-lab-2` → quan sát toàn bộ JSON, tìm các field: `State.Status`, network/IP nội bộ, đường dẫn lưu trữ (`/var/lib/docker/containers/<id>/...`), `RestartPolicy`.
2. `docker container inspect --format '{{json .State.Status}}' <ten>` (hoặc tương đương) để lọc riêng trạng thái.
3. Tìm và mở trực tiếp file log JSON trên host tại đường dẫn `/var/lib/docker/containers/<id>/<id>-json.log` để xem log thô của container.
4. Phân biệt: log này là log của container (docker logs), khác với log ứng dụng Nginx nằm trong `/var/log/nginx/` bên trong container.
5. `docker container logs docker-lab-2` → xem log qua CLI (thay vì phải mò file trên host).
6. `docker container logs -f docker-lab-2` → theo dõi real-time.
7. `docker container logs --tail 20 docker-lab-2` → chỉ xem 20 dòng cuối.

### Demo 7 — Tạo tải để quan sát log real-time
1. Mở terminal A: chạy `docker container logs -f docker-lab-2`.
2. Mở terminal B: chạy vòng lặp gửi 50 HTTP request liên tiếp tới `http://<ip-server>:8080` (mỗi request có gắn một ID để dễ đối chiếu số lượng — ví dụ dùng script `curl` lặp 50 lần).
3. Quan sát terminal A: log tăng dần theo từng request, đếm để xác nhận đủ 50 dòng log tương ứng 50 request.

### Demo 8 — Theo dõi tài nguyên và sự kiện
1. `docker stats` → quan sát CPU%/MEM usage của container Nginx đang chạy.
2. Mở terminal A: `docker events --filter container=docker-lab-2` (hoặc theo ID container).
3. Mở terminal B: lần lượt chạy `docker container restart docker-lab-2`, `docker container stop docker-lab-2`, `docker container start docker-lab-2`.
4. Quan sát terminal A: các sự kiện `restart`, `kill`, `stop`, `start` xuất hiện tương ứng theo đúng trình tự thao tác ở terminal B.

---

## 5. Các khái niệm/định nghĩa quan trọng giảng viên nhấn mạnh

1. **"Container là bất biến (immutable)."** Một khi container được tạo, không sửa nội dung bên trong nó theo cách bền vững — mỗi lần chạy là chạy đúng phiên bản (image) tại thời điểm tạo. Muốn nâng cấp thì phải thay thế bằng container mới, không sửa tại chỗ.
2. **"Docker (container) không lưu dữ liệu — nó chỉ là môi trường chạy."** Dữ liệu phải được đưa ra ngoài qua volume, nếu không khi container bị xóa, dữ liệu mất theo.
3. **"Khi container chạy, nó dùng chung hệ điều hành (kernel) với host bên dưới"** — đây là lý do container nhẹ/nhanh hơn máy ảo, vì bỏ được một lớp hệ điều hành riêng so với mô hình ảo hóa (Hypervisor + guest OS).
4. **"Container về bản chất giống một tiến trình (process) của hệ điều hành host"**, không phải một máy ảo đầy đủ — thời gian khởi động chỉ 1-2 phút (thường vài giây) là vì bản chất chỉ là chạy một process, không phải boot một OS.
5. **"Công nghệ nền tảng của container (namespace, cgroups) không hề mới — nó đã tồn tại trong Linux kernel hàng chục năm."** Docker chỉ hiện thực hóa (đóng gói dễ dùng) các cơ chế cô lập vốn đã có sẵn ở tầng hệ điều hành, không phát minh ra khái niệm cô lập tiến trình.
6. **"Sửa nóng (hotfix) bên trong container là tạm thời, không phải cách làm đúng."** Cách làm đúng là sửa từ nguồn (Dockerfile/mã nguồn ứng dụng) rồi build lại image mới.
7. **"Có 2 loại log cần phân biệt rõ: log của container (do Docker capture qua stdout/stderr) và log của ứng dụng bên trong (do chính ứng dụng tự ghi ra file)."** Cả hai đều quan trọng nhưng phục vụ mục đích khác nhau.
8. **"Quan điểm nhồi hết mọi thứ (code, data) vào bên trong container là một sai lầm thiết kế."** Nên tách: container chỉ chứa phần runtime, còn code/data nên được mount ra ngoài (volume) để dễ quản lý, cập nhật mà không ảnh hưởng đến container.
9. **"Container chỉ phụ thuộc vào kernel bên dưới, không phụ thuộc hệ điều hành cụ thể như Ubuntu hay RedHat"** — nhờ tuân theo chuẩn phát triển chung (theo giảng viên) **[suy luận: khả năng là chuẩn OCI]**, nên image/registry của các nhà cung cấp khác nhau vẫn tương thích được với các container runtime khác nhau (Docker, Podman).
10. **"Human in the Loop"** (mượn thuật ngữ từ AI): trong bất kỳ quy trình làm việc lặp lại nào (kể cả khi dùng AI hỗ trợ soạn tài liệu/script), con người luôn phải có bước xác minh (verify) nằm trong vòng lặp, không giao phó hoàn toàn cho công cụ tự động.

---

## 6. Gợi ý bài tập / lab (dựa trên các chỗ giảng viên hứa hẹn hoặc nội dung phù hợp)

Giảng viên không đưa ra danh sách bài tập chính thức trong transcript này (buổi học thiên về demo trực tiếp có học viên làm theo), nhưng các điểm sau đây phù hợp để biên soạn thành bài tập/lab cho buổi tiếp theo hoặc bài tập về nhà — dựa trên nội dung đã giảng và các điểm giảng viên "hẹn buổi sau":

1. **Lab vòng đời container (mở rộng từ Demo 4-5):** Yêu cầu học viên tự chạy một container bất kỳ (khác Nginx, ví dụ MySQL/Redis), thực hiện đầy đủ chu trình stop → start → rename → exec vào trong → sửa nóng → xóa → tạo lại → tự viết báo cáo quan sát để minh chứng lại tính bất biến của image.
2. **Lab Dockerfile (giảng viên hẹn rõ ràng "buổi sau" sẽ học):** Viết một Dockerfile đơn giản để build image tùy chỉnh (ví dụ thêm file HTML riêng vào image Nginx thay vì sửa nóng), rồi build và chạy thử — đối chiếu với cách "sửa nóng" đã học để hiểu sự khác biệt giữa 2 cách tiếp cận.
3. **Lab thiết lập Docker Registry riêng:** Giảng viên có hỏi "đã từng tự dựng (host/view) một Docker Registry chưa" và học viên trả lời chưa — đây là khoảng trống phù hợp để ra bài tập dựng thử Harbor hoặc Nexus (hoặc đơn giản là `registry:2` chính thức của Docker) làm registry nội bộ.
4. **Lab Docker volume/persistent storage:** Giảng viên nhiều lần nhắc "sau này em sẽ mount volume ra ngoài" nhưng chưa demo cụ thể trong buổi này — phù hợp làm bài tập riêng: dùng `-v` hoặc `--mount` để lưu dữ liệu ra ngoài container, kiểm chứng dữ liệu **không** mất khi xóa container (đối lập với Demo 5 ở trên).
5. **Lab logging tập trung:** Cài thử Vector hoặc VictoriaLogs để thu thập log container tự động (giảng viên có nhắc tên công cụ nhưng chưa demo) — bài tập nối tiếp phần lý thuyết về log.
6. **Lab giới hạn tài nguyên (resource limits):** Giảng viên nói "trong K8s sẽ thấy rõ hơn" về giới hạn CPU/RAM — có thể ra bài tập nhỏ hơn ngay ở mức Docker: dùng option `--memory` và `--cpus` khi `docker run` để giới hạn tài nguyên, quan sát bằng `docker stats`.
7. **Lab test tải cơ bản:** Dựa trên Demo 7 (gửi 50 request), mở rộng thành bài tập viết script test tải đơn giản (dùng AI hỗ trợ viết) và quan sát qua `docker stats` + `docker container logs -f` cùng lúc.
8. **Lab Docker Compose (hẹn buổi sau):** Vì buổi này chỉ giới thiệu khái niệm Docker Compose (không demo), có thể ra bài tập: viết một file `docker-compose.yml` gộp 2-3 container (ví dụ web + database) thay vì chạy `docker run` riêng lẻ.
9. **Lab tìm hiểu `docker events` lưu trữ lâu dài:** Giảng viên tự nhận chưa chắc chắn về cơ chế lưu trữ của `docker events` ("khả năng phải tìm hiểu thêm") — đây là điểm mở, phù hợp giao cho học viên tự nghiên cứu và trình bày lại ở buổi sau.

---

## 7. Khoảng trống / điểm chưa rõ trong transcript

- **Tên tài liệu tham khảo mở đầu** ("IntroDain và Pareto", tài liệu "công ty AdSense") — nghe không rõ, không xác định được chính xác là công ty/sản phẩm gì.
- **Cụm "Quảng Tây Nư"** — suy luận là "OCI" (Open Container Initiative) dựa theo ngữ cảnh (chuẩn chung giúp Docker/Podman/registry khác nhau tương thích) nhưng **không có độ chắc chắn 100%** vì âm thanh phiên âm khác biệt khá xa.
- **Cụm "TGRAF"** trong lúc xem `docker info` — không xác định được chính xác đây là field/lệnh nào.
- **"Quatch Virus" / "CTI"** trong đoạn nói về registry riêng có tích hợp scan bảo mật — suy luận là công cụ scan lỗ hổng bảo mật (kiểu Trivy/Clair) quét CVE trong image, nhưng transcript không đủ rõ để xác định chính xác tên công cụ.
- **"TabDest"** (một trong các môi trường được liệt kê: PC, TabDest, Product, Cloud Public) — không rõ đây là môi trường "Test", "Staging" hay tên riêng khác.
- **Lệnh kiểm tra hệ điều hành nghe thành "rsb"** — suy luận có thể là `lsb_release -a` hoặc lệnh tương tự, không chắc chắn.
- **Cơ chế lưu trữ của `docker events`** — chính giảng viên cũng nói "chưa chắc, khả năng phải tìm hiểu thêm", nên đây là điểm chưa rõ được cả người giảng lẫn transcript xác nhận.
- Nhiều đoạn transcript bị lỗi nặng do STT lặp từ vô nghĩa liên tục (ví dụ chuỗi lặp "dữ dữ dữ...", "xin xin xin...", "nhé nhé nhé...", "mở mở mở...", "trừ trừ trừ...", "A7 A7 A7...", "dòng dòng dòng...", "nằm nằm nằm...", "Đúng không?" lặp hàng chục lần liên tiếp) — các đoạn này rơi vào lúc giảng viên gõ lệnh dài trên màn hình hoặc dừng nói lâu; nội dung kỹ thuật thực chất không bị mất (được suy ra từ ngữ cảnh trước/sau), nhưng cần lưu ý transcript gốc có chất lượng kém ở các đoạn này.
- Tài liệu thực hành được giảng viên tham chiếu có đánh số mục (ví dụ "bước 9.1", "bài 10", "bài 11", "bài 13", "bài 15/16"...) nhưng transcript không cho thấy đầy đủ nội dung từ bài 1 đến bài 8 (phần cài đặt) và bài 14 — có thể tài liệu gốc (PDF) có chi tiết hơn transcript ghi lại qua lời nói.
