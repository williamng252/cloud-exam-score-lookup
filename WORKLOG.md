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
- **Quản lý tài nguyên & Minh chứng:** Kiểm tra và áp dụng chuẩn gắn nhãn (`Tag: Project/Owner`) cho toàn bộ tài nguyên AWS đã khởi tạo; thu thập và tổng hợp toàn bộ ảnh chụp minh chứng thao tác.
- **Quản lý mã nguồn & Worklog:** Cấu hình repository GitHub, viết file `README.md`, khởi tạo và cập nhật nhật ký công việc `WORKLOG.md`, đồng thời chuyển đổi tài liệu báo cáo sang chuẩn Markdown.

---

# TUẦN 2: TRIỂN KHAI CHỨC NĂNG LÕI VÀ KIỂM THỬ TRÊN AWS

Thời gian thực hiện: 12/10/2026 – 18/10/2026  
Mục tiêu tuần 2:
- Tạo bảng DynamoDB và nạp dữ liệu mẫu kiểm thử.
- Viết và triển khai hàm AWS Lambda xử lý logic tra cứu điểm.
- Cấu hình API Gateway kết nối Lambda và kiểm thử luồng hoạt động qua CloudWatch Logs.

## 1. BẢNG TỔNG HỢP PHÂN CÔNG VÀ GIỜ LÀM VIỆC TUẦN 2

| Thành viên | Công việc thực hiện | Giờ làm việc | Kết quả |
| :--- | :--- | :---: | :--- |
| **Nguyễn Anh Quân** (24110309) | - Tạo bảng DynamoDB `exam-scores`, chọn khóa `sbd` kiểu String và thêm dữ liệu giả lập.<br>- Tạo Lambda `exam-score-lookup` bằng Python 3.12, sử dụng LabRole.<br>- Tạo REST API `exam-score-api`, cấu hình GET `/scores` kết nối Lambda và deploy stage dev. | 10 giờ | Đã lưu và kiểm tra 1 bản ghi mẫu; Lambda đọc được DynamoDB và trả kết quả JSON; Gọi API qua URL nhận đúng thông tin điểm thi. |
| **Nguyễn Thành Huy** (24110222) | - Kiểm thử các trường hợp tra cứu (tồn tại, không tồn tại, sai định dạng) và kiểm tra CloudWatch Logs.<br>- Tổng hợp báo cáo, cập nhật GitHub và liên kết các Commit. | 10 giờ | Hoàn thành kiểm thử, lưu ảnh minh chứng, hoàn thiện báo cáo tuần 2 và cập nhật mã nguồn, tài liệu lên GitHub. |

## 2. KẾT QUẢ VÀ PHẠM VI THỰC HIỆN TUẦN 2
- Triển khai thành công luồng API Gateway → Lambda → DynamoDB.
- Tra cứu thành công số báo danh mẫu `01000001`.
- Xử lý thành công các trường hợp không tìm thấy, thiếu hoặc sai định dạng số báo danh.
- Kiểm tra log thực thi Lambda trên CloudWatch Logs.
- Lưu mã nguồn tại `src/lambda_function.py` (hoặc `Tuan 2/lambda_function.py`).
- **Phạm vi tuần 2:** Sử dụng 1 bản ghi mẫu để kiểm thử chức năng; chưa nạp 100.000 thí sinh và chưa kiểm thử tải.

---

## 3. KẾ HOẠCH CHI TIẾT TUẦN 3

- **Nạp 100.000 bản ghi vào DynamoDB:** Viết script Python (sử dụng `boto3` và `batch_write_item`) để sinh dữ liệu giả lập và nạp 100.000 thí sinh vào bảng DynamoDB theo từng batch (mỗi batch tối đa 25 bản ghi), tính toán và ước tính dung lượng lưu trữ thực tế.
- **Kiểm thử tải (Load Testing):** Sử dụng công cụ kiểm thử tải (như Apache JMeter hoặc Locust) để bắn tải đồng thời vào API Gateway, đo lường các chỉ tiêu hiệu năng dự kiến (độ trễ phản hồi trung bình - Latency, số lượng request xử lý trên giây - RPS, tỷ lệ lỗi - Error Rate).
- **Tích hợp và đối chiếu ElastiCache:** Triển khai tầng Redis caching với Amazon ElastiCache để lưu đệm kết quả tra cứu, sau đó thực hiện kiểm thử tải lại để so sánh hiệu năng (thời gian phản hồi và tải trên DynamoDB) giữa hai phương án có dùng cache và không dùng cache.
