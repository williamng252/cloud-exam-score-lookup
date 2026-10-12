# TUẦN 1: TÌM HIỂU LÝ THUYẾT, THIẾT KẾ KIẾN TRÚC & DỰNG NỀN TẢNG HẠ TẦNG VPC/S3 CHO HỆ THỐNG TRA CỨU ĐIỂM THI

Thời gian thực hiện: 05/10/2026 – 11/10/2026
Mục tiêu tuần 1:

* Phân tích yêu cầu, xác định chức năng và mô hình dữ liệu tra cứu điểm thi.
* Nghiên cứu lý thuyết các dịch vụ cốt lõi: API Gateway (Caching/Throttling), AWS Lambda, Amazon DynamoDB, ElastiCache và CloudWatch.
* Thiết kế mô hình kiến trúc hệ thống chịu tải đột biến và quy ước gắn nhãn (Tagging) cho tài nguyên.
* Dựng hạ tầng nền tảng trên AWS Learner Lab: Kiểm tra LabRole, tạo VPC và S3 Bucket.
* Kiểm tra quy chuẩn Tagging (`Project`/`Owner`), tổng hợp ảnh minh chứng và hoàn thành tài liệu báo cáo tuần 1.

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
* **Phân tích yêu cầu & Thiết kế:** Phân tích yêu cầu bài toán tra cứu điểm thi chịu tải đột biến, xác định các chức năng cốt lõi và cấu trúc dữ liệu tra cứu.
* **Nghiên cứu công nghệ:** Tìm hiểu cơ chế hoạt động của Amazon DynamoDB (NoSQL) và AWS Lambda (Serverless Compute) ứng dụng cho hệ thống.
* **Dựng hạ tầng mạng & Lưu trữ:** Kiểm tra môi trường AWS Learner Lab, phân quyền IAM LabRole, khởi tạo mạng ảo VPC và S3 Bucket làm nền tảng triển khai.
* **Tổng hợp tài liệu:** Vẽ sơ đồ kiến trúc hệ thống tổng quan và tổng hợp bản thảo báo cáo tiến độ Tuần 1.

### Sinh viên 2: Nguyễn Thành Huy (MSSV: 24110222)
* **Nghiên cứu công nghệ chịu tải:** Tìm hiểu chuyên sâu cơ chế API Gateway Caching, Throttling/Rate Limiting, giám sát qua CloudWatch và khảo sát giải pháp caching với Amazon ElastiCache để xử lý tải đột biến.
* **Quản lý tài nguyên & Minh chứng:** Kiểm tra và áp dụng chuẩn gắn nhãn (`Tag: Project/Owner`) cho toàn bộ tài nguyên AWS đã khởi tạo; thu thập và tổng hợp toàn bộ ảnh chụp minh chứng thao tác.
* **Quản lý mã nguồn & Worklog:** Cấu hình repository GitHub, viết file `README.md`, khởi tạo và cập nhật nhật ký công việc `WORKLOG.md`, đồng thời chuyển đổi tài liệu báo cáo sang chuẩn Markdown.
