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
  # TUẦN 4: KIỂM THỬ TỔNG THỂ, ĐÁNH GIÁ HIỆU NĂNG, HOÀN THIỆN GIAO DIỆN WEB VÀ DEMO HỆ THỐNG

Thời gian thực hiện: 20 Giờ

Mục tiêu tuần 4:
- Kiểm thử tổng thể chức năng tra cứu và bảo mật API.
- Đánh giá khả năng đáp ứng thông qua các kịch bản kiểm thử tải.
- Phân tích hiệu quả cache, throttling và số liệu giám sát CloudWatch.
- Xây dựng giao diện web cơ bản kết nối với backend AWS.
- Tổng hợp chi phí sử dụng và đề xuất tối ưu hệ thống.
- Hoàn thiện báo cáo tuần 4 và quay video demo.

---

## 1. BẢNG TỔNG HỢP PHÂN CÔNG VÀ GIỜ LÀM VIỆC TUẦN 4

| Thành viên | Công việc thực hiện | Giờ làm việc | Kết quả |
| :--- | :--- | :---: | :--- |
| **Nguyễn Anh Quân** (24110309) | - Xây dựng giao diện web tra cứu điểm bằng Flask, HTML, CSS và JavaScript.<br>- Kết nối giao diện với API AWS bằng request ký SigV4; bổ sung endpoint trả JSON.<br>- Kiểm thử chức năng tra cứu và bảo mật API.<br>- Quay video demo hệ thống.<br>- Viết phần báo cáo về kiến trúc, giao diện và kiểm thử chức năng. | 10 Giờ | Giao diện kết nối thành công với backend AWS; hiển thị đúng dữ liệu thí sinh và cảnh báo sai định dạng; endpoint cục bộ trả JSON; hoàn thành bản quay demo khoảng 2 phút 33 giây và bổ sung nội dung báo cáo phần phụ trách. |
| **Nguyễn Thành Huy** (24110222) | - Thực hiện và tổng hợp kiểm thử tải hệ thống ở các mức 3, 5, 10 và 20 RPS.<br>- Phân tích độ trễ, tỷ lệ phản hồi 200/429/5xx và khả năng đáp ứng.<br>- Đánh giá hiệu quả cache, throttling và các chỉ số CloudWatch.<br>- Tổng hợp chi phí, đề xuất tối ưu và viết phần báo cáo hiệu năng, giám sát, chi phí. | 10 Giờ | Tổng hợp kết quả kiểm thử tải; so sánh cache bật/tắt và phân bố dữ liệu hot/mixed; phân tích phản hồi 429 khi vượt ngưỡng; hoàn thiện nội dung báo cáo hiệu năng, giám sát và bảng ước tính chi phí. |
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

- **Kiểm thử tải tổng thể:** Thực hiện các kịch bản gửi request có ký SigV4 ở các mức 3, 5, 10 và 20 RPS, mỗi lượt kéo dài 60 giây. So sánh trường hợp tắt cache, bật cache với nhóm số báo danh truy cập lặp (hot) và phân bố ngẫu nhiên trên bộ dữ liệu 100.000 thí sinh (mixed).

- **Tổng hợp và phân tích hiệu năng:** Tổng hợp kết quả CSV/JSON, thống kê RPS gửi thực tế, goodput, số lượng phản hồi 200, 429, 5xx, lỗi mạng và độ trễ p50, p95, p99. Phân biệt mức tải đáp ứng tiêu chí với mức tải bị throttling; không sử dụng kết quả để khẳng định hệ thống phục vụ được 100.000 người đồng thời.

- **Đánh giá cache và giám sát CloudWatch:** Đối chiếu CacheHitCount, CacheMissCount, Lambda Invocations, Throttles và ConcurrentExecutions trong cùng cửa sổ đo. Kịch bản hot ghi nhận tỷ lệ cache hit khoảng 94,4%, số lượt gọi Lambda giảm từ 180 xuống 10; kịch bản mixed ghi nhận tỷ lệ cache hit khoảng 8,3%.

- **Phân tích giới hạn truy cập:** Với cấu hình Rate = 5 RPS và Burst = 10, các lượt thử 10 và 20 RPS lần lượt ghi nhận 256 và 855 phản hồi HTTP 429, không ghi nhận lỗi 5xx trong các lượt đo. Phân tích vai trò throttling trong việc kiểm soát lượng request chuyển đến backend.

- **Tổng hợp chi phí và đề xuất tối ưu:** Lập bảng ước tính chi phí theo dịch vụ và thời gian sử dụng, ghi rõ nguồn đơn giá và phân biệt với số liệu chi phí thực tế. Đánh giá chi phí duy trì API Gateway Cache, đề xuất chỉ provision cache trong thời gian cần thiết và tránh bổ sung hạ tầng không sử dụng.

- **Hoàn thiện báo cáo phần phụ trách:** Viết các phần kiểm thử tải, hiệu quả cache, giám sát CloudWatch, phân tích quá tải, chi phí và đề xuất tối ưu; bổ sung bảng kết quả và ảnh minh chứng tương ứng.

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
