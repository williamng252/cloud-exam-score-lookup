# TUẦN 1: TÌM HIỂU LÝ THUYẾT, THIẾT KẾ KIẾN TRÚC & DỰNG NỀN TẢNG HẠ TẦNG VPC/S3 CHO HỆ THỐNG TRA CỨU ĐIỂM THI

Thời gian thực hiện: 05/10/2026 – 11/10/2026 
Mục tiêu tuần 1:

- Phân tích yêu cầu, xác định chức năng và mô hình dữ liệu tra cứu điểm thi.
- Nghiên cứu lý thuyết các dịch vụ cốt lõi: API Gateway (Caching/Throttling), AWS Lambda, Amazon DynamoDB, ElastiCache và CloudWatch.
- Thiết kế mô hình kiến trúc hệ thống chịu tải đột biến và quy ước gắn nhãn (Tagging) cho tài nguyên.
- Dựng hạ tầng nền tảng trên AWS Learner Lab: Kiểm tra LabRole, tạo VPC và S3 Bucket.
- Kiểm tra quy chuẩn Tagging (`Project`/`Owner`), tổng hợp ảnh minh chứng và hoàn thành tài liệu báo cáo tuần 1.

---

## 1. BẢNG TỔNG HỢP PHÂN CÔNG VÀ GIỜ LÀM VIỆC TUẦN 1

| Công việc | Nguyễn Anh Quân (24110309) | Nguyễn Thành Huy (24110222) | Trạng thái |
| :--- | :---: | :---: | :---: |
| Phân tích yêu cầu, xác định chức năng và dữ liệu tra cứu | ✓ | | Hoàn thành |
| Tìm hiểu DynamoDB, Lambda và thiết kế kiến trúc | ✓ | | Hoàn thành |
| Tìm hiểu API Gateway caching, throttling, CloudWatch và khảo sát ElastiCache | | ✓ | Hoàn thành |
| Kiểm tra Learner Lab, LabRole, dựng VPC và S3 | ✓ | | Hoàn thành |
| Vẽ sơ đồ kiến trúc, tổng hợp báo cáo tuần 1 | ✓ | | Hoàn thành |
| Kiểm tra tag Project/Owner, tổng hợp ảnh minh chứng và cập nhật worklog | | ✓ | Hoàn thành |

---

## 2. CHI TIẾT CÔNG VIỆC TỪNG SINH VIÊN

### Sinh viên 1: Nguyễn Anh Quân (MSSV: 24110309)
- **Phân tích yêu cầu & Thiết kế:** Phân tích yêu cầu bài toán tra cứu điểm thi chịu tải đột biến, xác định các chức năng cốt lõi và cấu trúc dữ liệu tra cứu.
- **Nghiên cứu công nghệ:** Tìm hiểu cơ chế hoạt động của Amazon DynamoDB (NoSQL) và AWS Lambda (Serverless Compute) ứng dụng cho hệ thống.
- **Dựng hạ tầng mạng & Lưu trữ:** Kiểm tra môi trường AWS Learner Lab, phân quyền IAM LabRole, khởi tạo mạng ảo VPC và S3 Bucket làm nền tảng triển khai.
- **Tổng hợp tài liệu:** Vẽ sơ đồ kiến trúc hệ thống tổng quan và tổng hợp bản thảo báo cáo tiến độ Tuần 1.

### Sinh viên 2: Nguyễn Thành Huy (MSSV: 24110222)
- **Nghiên cứu công nghệ chịu tải:** Tìm hiểu chuyên sâu cơ chế API Gateway Caching, Throttling/Rate Limiting, giám sát qua CloudWatch và khảo sát giải pháp caching với Amazon ElastiCache để xử lý tải đột biến.
- **Quản lý tài nguyên & Minh chứng:** Kiểm tra và áp dụng chuẩn gắn nhãn (`Tag:Giờ | Giao diện kết nối thành công với backend AWS; hiển thị đúng dữ liệu thí sinh và cảnh báo sai định dạng; endpoint cục bộ trả JSON; hoàn thành bản quay demo khoảng 2 phút 33 giây và bổ sung nội dung báo cáo phần phụ trách. |
| **Nguyễn Thành Huy** (24110222) | [Thành viên bổ sung công việc thực tế] | [điền] | [Thành viên bổ sung kết quả] |

---

## 2. CHI TIẾT CÔNG VIỆC TỪNG SINH VIÊN

### Sinh viên 1: Nguyễn Anh Quân (MSSV: 24110309)

- **Xây dựng giao diện web tra cứu điểm:** Sử dụng Flask, HTML, CSS và JavaScript để xây dựng trang nhập số báo danh, nút Tra cứu và khu vực hiển thị họ tên, điểm Toán, Ngữ văn, Tiếng Anh. Giao diện kiểm tra số báo danh gồm 8 chữ số, giữ nguyên số 0 ở đầu và hiển thị thông báo khi nhập sai định dạng.

- **Tích hợp giao diện với backend AWS:** Xây dựng phần xử lý Python ký request bằng SigV4 rồi gọi API Gateway `GET /scores`. Giữ cơ chế xác thực `AWS_IAM`; thông tin phiên Learner Lab được lưu riêng ngoài thư mục mã nguồn, không đưa vào HTML, JavaScript hoặc GitHub.

- **Bổ sung endpoint JSON:** Xây dựng endpoint cục bộ `GET /api/scores?sbd=...`, cho phép xem kết quả JSON trực tiếp trên trình duyệt. Flask chuyển tiếp request có ký tới API AWS và trả kết quả về phía người dùng.

- **Kiểm thử chức năng và bảo mật API:** Kiểm tra tra cứu số báo danh hợp lệ, đối chiếu dữ liệu trả về, các trường hợp không tìm thấy, thiếu hoặc sai định dạng số báo danh; kiểm tra phản hồi đối với request có và không có chữ ký SigV4. Phân biệt kiểm tra đầu vào trên giao diện với kiểm thử trực tiếp API AWS.

- **Quay video demo hệ thống:** Quay màn hình giới thiệu kiến trúc, thao tác tra cứu các số báo danh, kiểm tra đầu vào và xem phản hồi JSON. Giới thiệu các cấu hình DynamoDB, Lambda Reserved Concurrency, API Gateway Cache/TTL/Throttling và dashboard CloudWatch. Bản quay màn hình dài khoảng 2 phút 33 giây.

- **Hoàn thiện nội dung báo cáo phần phụ trách:** Bổ sung mô tả kiến trúc, giao diện web, luồng kết nối Flask – API Gateway – Lambda – DynamoDB, cơ chế bảo mật và kết quả kiểm thử chức năng; chuẩn bị các vị trí ảnh minh chứng tương ứng.

### Sinh viên 2: Nguyễn Thành Huy (MSSV: 24110222)

[Thành viên bổ sung chi tiết công việc thực tế tại đây.]

---

## 3. KẾT QUẢ VÀ PHẠM VI THỰC HIỆN TUẦN 4

- Kiểm thử chức năng tra cứu và cơ chế bảo mật `AWS_IAM` trên hệ thống đã triển khai.
- Thực hiện các kịch bản kiểm thử tải, tổng hợp RPS, số lượng phản hồi và độ trễ p50, p95, p99.
- Đánh giá hiệu quả cache thông qua CacheHitCount, CacheMissCount và số lượt thực thi Lambda.
- Phân tích phản hồi khi vượt giới hạn throttling, tách riêng mã 429 và lỗi 5xx.
- Bổ sung giao diện web chạy cục bộ, kết nối với các dịch vụ backend trên AWS.
- Tra cứu thành công các số báo danh `01000001`, `01050000` và `01100000` trên giao diện.
- Cung cấp endpoint cục bộ trả JSON qua request có ký tới API AWS.
- Tổng hợp chi phí sử dụng, các giới hạn còn lại và đề xuất tối ưu.
- Hoàn thành bản quay màn hình demo và bổ sung nội dung báo cáo tuần 4.
- **Phạm vi tuần 4:** Đánh giá hệ thống trong điều kiện cấu hình và tải thử nghiệm của AWS Learner Lab; kết quả không đại diện cho khả năng phục vụ 100.000 người truy cập đồng thời.

---

## 4. HOÀN THIỆN BÁO CÁO VÀ DEMO CUỐI KỲ

- **Rà soát nội dung:** Đối chiếu kết quả kiểm thử, bảng cấu hình và nhận xét với dữ liệu thực tế; thống nhất các thông số trong toàn bộ báo cáo.
- **Hoàn thiện minh chứng:** Bổ sung ảnh kiểm thử, giao diện, JSON, CloudWatch và nguồn số liệu chi phí; điền các thông tin còn trống.
- **Hoàn thiện video:** Bàn giao bản quay màn hình và kịch bản thuyết minh; bảo đảm video hoàn chỉnh không vượt quá 10 phút.
- **Tổng kết dự án:** Đối chiếu yêu cầu đề tài với kết quả đạt được, nêu rõ phạm vi kiểm thử và những hạn chế của môi trường Learner Lab.
