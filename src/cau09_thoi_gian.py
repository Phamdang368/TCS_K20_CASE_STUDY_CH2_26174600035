from datetime import datetime

thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")

print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))

# Bổ sung tính toán khoảng thời gian
bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)
thoi_luong = ket_thuc - bat_dau

print(thoi_luong)
print(type(thoi_luong))

# Giải thích:
# - datetime: Đối tượng kiểu ngày giờ đầy đủ trong Python.
# - str: Chuỗi văn bản đại diện cho mốc thời gian sau khi được định dạng bằng strftime.
# - timedelta: Kích thước/khoảng thời gian chênh lệch giữa 2 thời điểm (kết quả của phép trừ 2 datetime).
