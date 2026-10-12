# Hệ thống tra cứu điểm thi chịu tải đột biến

Đồ án môn Điện toán đám mây — Giảng viên hướng dẫn: Huỳnh Xuân Phụng.

## Thành viên

| Họ tên | MSSV |
|---|---|
| Nguyễn Anh Quân | 24110309 |
| Nguyễn Thành Huy | 24110222 |

## Giới thiệu

Thiết kế hệ thống tra cứu điểm thi trên AWS Learner Lab với dữ liệu giả lập 100.000 thí sinh lưu trong DynamoDB. Sử dụng API Gateway caching và throttling để giảm tải, giới hạn Lambda concurrency ≤ 10 và giám sát bằng CloudWatch.

Thực hiện kiểm thử tải, đánh giá khả năng đáp ứng và báo cáo chi phí sử dụng.

<img width="1020" height="650" alt="image" src="https://github.com/user-attachments/assets/80221df2-cc6f-4669-a0c7-1096b3b368a4" />


