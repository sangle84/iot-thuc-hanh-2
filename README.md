# Buổi thực hành 2 - AMQP

| Họ và Tên | Mã Sinh Viên |
| :--- | :--- |
| **Nguyễn Quốc Thịnh** | `B23DCCN790` |
| **Lê Tiến Sang** | `B23DCCN710` |


## 1. Broker

- RabbitMQ local: `localhost:5672`
- Không yêu cầu xác thực theo cấu hình mặc định.

## 2. Cài đặt

```bash
pip install pika
```

Nếu dùng môi trường ảo:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install pika
```

## 3. Chạy các chương trình

### Bài 1: Producer và Consumer cơ bản

```powershell
# Terminal 1
python consumer_bai1.py

# Terminal 2
python producer_bai1.py
```

### Bài 2: Sensor Producer và Monitor Consumer

```powershell
# Terminal 1
python monitor_consumer_bai2.py

# Terminal 2
python sensor_producer_bai2.py
```

### Bài 3: Alert Producer và Consumer với Exchange

```powershell
# Terminal 1
python warning_consumer_bai3.py

# Terminal 2
python critical_consumer_bai3.py

# Terminal 3
python alert_producer_bai3.py warning "Nhiệt độ phòng máy vượt ngưỡng"
python alert_producer_bai3.py critical "Cảm biến kho lạnh mất kết nối"
python alert_producer_bai3.py info "Hệ thống khởi động"
```

## 4. Kết quả đạt được

### Bài 1

- Producer kết nối RabbitMQ và gửi bản tin vào queue `iot_lab_queue`.
- Consumer nhận và hiển thị nội dung message cùng thời gian nhận.

### Bài 2

- Sensor Producer gửi JSON mỗi 3 giây với các trường `device_id`, `temperature`, `humidity`.
- Monitor Consumer phân tích dữ liệu và cảnh báo:
  - Nhiệt độ > 35: cảnh báo nhiệt độ cao.
  - Độ ẩm < 40: cảnh báo độ ẩm thấp.

### Bài 3

- Alert Producer gửi message tới exchange `iot_alert_exchange` với routing key `info`, `warning` hoặc `critical`.
- Warning Consumer chỉ nhận message có routing key `warning`.
- Critical Consumer chỉ nhận message có routing key `critical`.
- Message `info` không được consumer nào nhận vì không có queue bind với routing key `info`.

## 5. Lưu ý

- Đảm bảo RabbitMQ đang chạy trước khi thực thi các script.
- Nếu RabbitMQ chưa được cài đặt, có thể khởi động broker bằng Docker.