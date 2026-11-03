
## 1 Giải nén và mở Terminal

Giải nén ZIP, vào thư mục score-web chứa app.py. Bấm vào thanh địa chỉ File Explorer, gõ powershell rồi Enter. Hoặc VS Code → Open Folder → Terminal → New Terminal.

Kiểm tra Python:

```powershell
py --version
```

Nếu không nhận py, thử python --version và thay py bằng python ở các lệnh sau. Nếu chưa có Python, cài Python 3.12 hoặc mới hơn từ python.org, bật Add Python to PATH, rồi mở Terminal mới.

## 2 Cài thư viện lần đầu

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Không cần activate nên không cần đổi PowerShell ExecutionPolicy.

## 3 Kết nối phiên Learner Lab

Start Lab, đợi AWS sẵn sàng. Trong trang lab mở AWS Details → AWS CLI . Khu vực credentials có access key ID, secret access key và session token của phiên hiện tại.

Trong Terminal chạy:

```powershell
py configure_lab.py
```

## 4 Chạy web

```powershell
.\.venv\Scripts\python.exe app.py
```

Giữ Terminal mở, vào trình duyệt:

http://127.0.0.1:5000

Đây cũng là http://localhost:5000. Web chỉ lắng nghe trên laptop; điện thoại hoặc máy khác không mở được bằng localhost của bạn.

## 5 Thử dữ liệu

- 01000001: Nguyễn Văn An, Toán 8.5, Văn 7, Anh 9 theo mẫu tuần 2; đối chiếu lại dữ liệu thực.
- 01050000 và 01100000: dữ liệu giả lập tuần 3, kiểm tra khác nhau.
- 99999999: thông báo không tìm thấy nếu không có item đó.
- Nhập abc hoặc thiếu số: báo sai định dạng tại giao diện; kiểm thử 400 từ AWS vẫn dùng script đã ký như kế hoạch tuần 4.





