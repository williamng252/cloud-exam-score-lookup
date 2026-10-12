# TUẦN 1: TÌM HIỂU LÝ THUYẾT, THIẾT KẾ KIẾN TRÚC & DỰNG NỀN TẢNG HẠ TẦNG VPC/S3 CHO HỆ THỐNG TRA CỨU ĐIỂM THI

Thời gian thực hiện: 05/10/2026 – 11/10/2026
Mục tiêu tuần 1:

* Nghiên cứu lý thuyết các dịch vụ cốt lõi: API Gateway, AWS Lambda, Amazon DynamoDB và Amazon CloudWatch.
* Thiết kế mô hình kiến trúc dự kiến cho hệ thống tra cứu điểm thi chịu tải đột biến và quy ước gắn nhẫn (Tagging) cho tài nguyên.
* Tạo hạ tầng mạng VPC, 02 Subnet, liên kết Route Table và kiểm tra IAM LabRole trên AWS Learner Lab.
* Khởi tạo S3 Bucket lưu trữ và cấu hình gắn Tag tài nguyên nền tảng.
* Khởi tạo GitHub Repository, cấu hình tài liệu chuẩn (`README.md`, `WORKLOG.md`) và hoàn thành tài liệu báo cáo tiến độ tuần 1.

---

## 1. BẢNG TỔNG HỢP PHÂN CÔNG VÀ GIỜ LÀM VIỆC TUẦN 1

| Công việc | Nguyễn Thành Huy (24110222) | [Tên Thành Viên 2] ([MSSV 2]) | Trạng thái |
| :--- | :---: | :---: | :---: |
| Tìm hiểu lý thuyết API Gateway, Lambda, DynamoDB, CloudWatch | ✓ | ✓ | Hoàn thành |
| Thiết kế kiến trúc dự kiến và quy ước tag tài nguyên | | ✓ | Hoàn thành |
| Dựng hạ tầng VPC, 2 Subnet, Route Table & kiểm tra IAM LabRole | ✓ | | Hoàn thành |
| Khởi tạo S3 Bucket và cấu hình gắn Tag tài nguyên | ✓ | | Hoàn thành |
| Cấu hình GitHub Repo, viết WORKLOG, README & báo cáo Tiến độ | ✓ | ✓ | Hoàn thành |

---

## 2. CHI TIẾT CÔNG VIỆC TỪNG SINH VIÊN

### Sinh viên 1: Nguyễn Thành Huy (MSSV: 24110222)

* **Tìm hiểu công nghệ:** Nghiên cứu tổng quan về mô hình Serverless, cơ chế hoạt động của AWS Lambda, Amazon API Gateway và cơ sở dữ liệu NoSQL DynamoDB.
* **Khởi tạo hạ tầng mạng:** Thực hiện thao tác trên AWS Learner Lab khởi tạo mạng ảo VPC, phân chia 02 Subnet, thiết lập và liên kết Route Table đảm bảo định tuyến mạng; đồng thời kiểm tra phân quyền bảo mật của IAM LabRole.
* **Cấu hình lưu trữ & Quản lý tài nguyên:** Khởi tạo S3 Bucket dùng làm nơi lưu trữ tài nguyên/mã nguồn, thiết lập hệ thống Tagging quản lý theo đúng quy ước của nhóm.
* **Quản lý mã nguồn & Báo cáo:** Tự khởi tạo GitHub Repository, thiết lập các file tài liệu chuẩn `README.md`, `WORKLOG.md` và chuyển đổi báo cáo sang định dạng Markdown chuẩn trên GitHub.

### Sinh viên 2: [Tên Thành Viên 2] (MSSV: [MSSV 2])

* **Nghiên cứu lý thuyết:** Phối hợp nghiên cứu tài liệu kỹ thuật về các dịch vụ chịu tải cao của AWS như API Gateway caching, Lambda execution lifecycle và giám sát hệ thống bằng CloudWatch Logs/Metrics.
* **Thiết kế hệ thống:** Xây dựng bản thiết kế kiến trúc dự kiến cho hệ thống Tra cứu điểm thi chịu tải đột biến và định nghĩa quy chuẩn gắn nhãn (`Tags`) cho toàn bộ tài nguyên AWS.
* **Lập tài liệu:** Tổng hợp thông tin, soạn thảo và hoàn thiện nội dung báo cáo tiến độ công việc của tuần 1.
