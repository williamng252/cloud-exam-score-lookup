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

---

## 2. CHI TIẾT CÔNG VIỆC TỪNG SINH VIÊN

### Sinh viên 1: Nguyễn Anh Quân (MSSV: 24110309)
- **Khởi tạo cơ sở dữ liệu:** Tạo bảng Amazon DynamoDB mang tên `exam-scores`, thiết lập khóa phân vùng (Partition Key) là `sbd` (kiểu String) và thêm thành công bản ghi thí sinh giả lập đầu tiên để kiểm thử chức năng.
- **Xây dựng hàm xử lý Serverless:** Viết mã nguồn hàm AWS Lambda `exam-score-lookup` sử dụng ngôn ngữ Python 3.12, cấu hình gắn quyền LabRole để hàm có quyền truy vấn đọc dữ liệu từ DynamoDB, đồng thời xử lý các logic ràng buộc (kiểm tra tồn tại, thiếu hoặc sai định dạng số báo danh).
- **Triển khai REST API:** Tạo API Gateway mang tên `exam-score-api`, cấu hình phương thức `GET /scores` tích hợp dạng Lambda proxy, đồng thời tiến hành deploy API thành công tại môi trường `dev`.

### Sinh viên 2: Nguyễn Thành Huy (MSSV: 24110222)
- **Kiểm thử chức năng hệ thống:** Thực hiện các test case kiểm tra luồng hoạt động xuyên suốt từ API Gateway đến Lambda và DynamoDB qua URL thực tế; xác minh các trường hợp số báo danh hợp lệ, không tồn tại, hoặc nhập sai định dạng.
- **Giám sát & Quản lý Log thực thi:** Truy cập và kiểm tra chi tiết các nhật ký thực thi (Execution Logs) của hàm Lambda trên CloudWatch Logs để đảm bảo không phát sinh lỗi và thời gian phản hồi đạt yêu cầu.
- **Quản lý tài liệu & Mã nguồn:** Tổng hợp ảnh chụp minh chứng toàn bộ các bước thực hiện, hoàn thiện văn bản báo cáo chi tiết tuần 2, đồng thời cập nhật mã nguồn, tài liệu và liên kết các Commit lên GitHub theo đúng yêu cầu của giảng viên.

---

## 3. KẾT QUẢ VÀ PHẠM VI THỰC HIỆN TUẦN 2
- Triển khai thành công luồng API Gateway → Lambda → DynamoDB.
- Tra cứu thành công số báo danh mẫu `01000001`.
- Xử lý thành công các trường hợp không tìm thấy, thiếu hoặc sai định dạng số báo danh.
- Kiểm tra log thực thi Lambda trên CloudWatch Logs.
- Lưu mã nguồn tại `src/lambda_function.py` (hoặc `Tuan 2/lambda_function.py`).
- **Phạm vi tuần 2:** Sử dụng 1 bản ghi mẫu để kiểm thử chức năng; chưa nạp 100.000 thí sinh và chưa kiểm thử tải.

---

## 4. KẾ HOẠCH CHI TIẾT TUẦN 3

- **Nạp 100.000 bản ghi vào DynamoDB:** Viết script Python (sử dụng `boto3` và `batch_write_item`) để sinh dữ liệu giả lập và nạp 100.000 thí sinh vào bảng DynamoDB theo từng batch (mỗi batch tối đa 25 bản ghi), tính toán và ước tính dung lượng lưu trữ thực tế.
- **Kiểm thử tải (Load Testing):** Sử dụng công cụ kiểm thử tải (như Apache JMeter hoặc Locust) để bắn tải đồng thời vào API Gateway, đo lường các chỉ tiêu hiệu năng dự kiến (độ trễ phản hồi trung bình - Latency, số lượng request xử lý trên giây - RPS, tỷ lệ lỗi - Error Rate).
- **Tích hợp và đối chiếu ElastiCache:** Triển khai tầng Redis caching với Amazon ElastiCache để lưu đệm kết quả tra cứu, sau đó thực hiện kiểm thử tải lại để so sánh hiệu năng (thời gian phản hồi và tải trên DynamoDB) giữa hai phương án có dùng cache và không dùng cache.


# TUẦN 3: TÍCH HỢP HỆ THỐNG, CẤU HÌNH BẢO MẬT, CACHING, THROTTLING VÀ GIÁM SÁT CLOUDWATCH CHO HỆ THỐNG TRA CỨU ĐIỂM THI

Thời gian thực hiện: 19/10/2026 – 28/10/2026  
Mục tiêu tuần 3:
- Sinh dữ liệu giả lập và nạp thành công 100.000 bản ghi thí sinh vào DynamoDB qua CloudShell.
- Cấu hình giới hạn số lần thực thi đồng thời (Reserved Concurrency = 10) cho hàm Lambda.
- Cấu hình API Gateway Caching (0.5GB, TTL 300s, khóa cache `sbd`) và API Throttling (Rate=5 RPS, Burst=10).
- Bật bảo mật xác thực `AWS_IAM` cho API Gateway và xác minh chữ ký SigV4.
- Thiết lập lưu vết nhật ký CloudWatch Log Retention (7 ngày), xây dựng CloudWatch Dashboard (`exam-score-week3`) và tạo 2 CloudWatch Alarms giám sát lỗi.
- Thực hiện kiểm thử tích hợp (T301 - T310), thu thập đầy đủ 12 hình minh chứng và hoàn thành báo cáo Tuần 3.

---

## 1. BẢNG TỔNG HỢP PHÂN CÔNG VÀ GIỜ LÀM VIỆC TUẦN 3

| Thành viên | Công việc thực hiện | Giờ làm việc | Kết quả |
| :--- | :--- | :---: | :--- |
| **Nguyễn Anh Quân** (24110309) | - Viết script `seed_scores.py` nạp 100.000 bản ghi dữ liệu vào DynamoDB.<br>- Cấu hình Reserved Concurrency (10) cho Lambda `exam-score-lookup`.<br>- Cấu hình API Gateway Cache Cluster (0.5GB) và Throttling (Rate=5, Burst=10).<br>- Bật xác thực `AWS_IAM` cho REST API method GET `/scores`. | 12 giờ | Nạp thành công 100k items; Lambda áp giới hạn 10 concurrency; Cache cluster trạng thái Provisioned với khóa `sbd`; API yêu cầu chữ ký IAM. |
| **Nguyễn Thành Huy** (24110222) | - Viết script `probe_api.py` kiểm thử các chế độ: single, burst, cache, `--unsigned`.<br>- Cấu hình CloudWatch Logs retention 7 ngày, tạo Dashboard `exam-score-week3` và tạo 2 Alarms.<br>- Tổng hợp minh chứng (12 ảnh), viết file báo cáo Tuần 3 và cập nhật GitHub/Worklog. | 12 giờ | Kiểm thử ghi nhận đủ mã 200, 429, 500, 403; Dashboard và 2 Alarms hoạt động ở trạng thái OK; Hoàn thành file báo cáo và Worklog. |

---

## 2. CHI TIẾT CÔNG VIỆC TỪNG SINH VIÊN

### Sinh viên 1: Nguyễn Anh Quân (MSSV: 24110309)
- **Nạp dữ liệu quy mô lớn (Data Seeding):** Viết script Python `seed_scores.py` sử dụng thư viện `boto3` và cơ chế `batch_writer` để sinh và ghi thành công 100.000 bản ghi điểm thi giả lập (SBD từ 01000001 đến 01100000) vào bảng DynamoDB `exam-scores` từ AWS CloudShell.
- **Cấu hình giới hạn tài nguyên Serverless:** Đặt giới hạn Reserved Concurrency bằng 10 cho hàm Lambda `exam-score-lookup` để chống quá tải cơ sở dữ liệu và quản lý tài nguyên hệ thống.
- **Cấu hình Tầng đệm & Giới hạn tải:** Khởi tạo API Gateway Cache Cluster 0.5GB tại Stage `dev`, cấu hình TTL 300 giây, bật khóa cache theo tham số `method.request.querystring.sbd`; thiết lập giới hạn Throttling với Rate = 5 requests/sec và Burst = 10 requests.
- **Tăng cường bảo mật API:** Chuyển cấu hình Authorization của phương thức `GET /scores` từ `NONE` sang `AWS_IAM` và tiến hành redeploy Stage `dev` để bắt buộc mọi truy cập phải có chữ ký SigV4 hợp lệ.

### Sinh viên 2: Nguyễn Thành Huy (MSSV: 24110222)
- **Xây dựng kịch bản kiểm thử tích hợp:** Viết script `probe_api.py` tích hợp `botocore` để tự động hóa các bài test: kiểm tra tính đúng đắn dữ liệu (single), kiểm thử giới hạn tải 120 requests liên tục (burst), gọi lặp 30 lần để sinh metrics (cache), và kiểm tra cơ chế từ chối khi không ký SigV4 (`--unsigned`).
- **Thiết lập hệ thống Giám sát & Cảnh báo:** Đổi Retention cho Lambda Log Group thành 7 ngày; xây dựng CloudWatch Dashboard mang tên `exam-score-week3` tích hợp các chỉ số API Gateway và Lambda; tạo 2 CloudWatch Alarms (`exam-score-lambda-errors` và `exam-score-api-5xx`) ở ngưỡng $\ge 1$ lỗi/phút.
- **Thu thập minh chứng & Quản lý tài liệu:** Chụp và hoàn thiện 12 hình ảnh minh chứng theo tiêu chuẩn báo cáo; tổng hợp file báo cáo `Mau_BaoCaoTuan3.docx`, cập nhật kết quả các test case T301 - T310, đồng thời cập nhật mã nguồn script và nhật ký `WORKLOG.md` lên GitHub repository.

---

## 3. KẾT QUẢ VÀ PHẠM VI THỰC HIỆN TUẦN 3
- Triển khai thành công luồng tra cứu hoàn chỉnh có Caching, Throttling và Bảo mật IAM.
- Nạp đủ và kiểm tra chính xác 100.000 bản ghi thí sinh trong DynamoDB.
- Giới hạn Lambda Concurrency = 10 hoạt động đúng cấu hình.
- API Gateway Caching và Throttling hoạt động chính xác: ghi nhận mã lỗi 429 Too Many Requests khi quá tải và HTTP 200 từ phản hồi Cache đệm.
- Bảo mật `AWS_IAM` chặn thành công request không ký (HTTP 403) và chấp nhận request có ký SigV4 (HTTP 200).
- Hoàn thành CloudWatch Dashboard `exam-score-week3` và kích hoạt 2 Alarms ở trạng thái OK.
- Thu thập đầy đủ 12/12 ảnh minh chứng và hoàn thiện 10/10 tiêu chí kiểm thử tích hợp (T301 - T310).
- Lưu mã nguồn script tại `scripts/seed_scores.py` và `scripts/probe_api.py`.
- **Phạm vi tuần 3:** Hoàn thành toàn bộ kiến trúc Serverless có Caching/Throttling/Security/Monitoring trên AWS Learner Lab; tiến hành tắt Cache cluster sau khi thu thập minh chứng để tối ưu chi phí.

---

## 4. KẾ HOẠCH TỔNG KẾT VÀ BÁO CÁO CUỐI KỲ

- **Rà soát toàn bộ tài nguyên AWS:** Tiến hành kiểm tra, dọn dẹp và ngắt kết nối các tài nguyên có phát sinh chi phí theo giờ (như API Gateway Cache Cluster) trên AWS Learner Lab.
- **Tổng hợp báo cáo và tổng kết dự án:** Hoàn thiện file báo cáo tổng hợp dự án Tra cứu điểm thi chịu tải đột biến trên AWS, đối chiếu các yêu cầu ban đầu với kết quả kiểm thử thực tế.
- **Đóng gói mã nguồn & Tài liệu:** Kiểm tra lại toàn bộ cấu trúc thư mục dự án trên GitHub (`src/`, `scripts/`, `docs/`), đảm bảo file `README.md` và `WORKLOG.md` cập nhật đầy đủ thông tin trước khi nộp bài cuối kỳ.
