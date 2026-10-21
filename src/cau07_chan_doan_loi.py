# MÃ NGUYÊN TRẠNG (Chạy lần đầu sẽ báo lỗi TypeError ở dòng dien_nang_kwh do cong_suat_w là str)
ma_may = input("Nhập mã máy: ")
cong_suat_w = input("Nhập công suất W: ")
so_phut = int(input("Nhập số phút: "))

# Sửa lỗi: Cần ép kiểu cong_suat_w sang float/int
cong_suat_w = float(cong_suat_w)

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")

# Comment mô tả lỗi:
# Lỗi phát hiện: TypeError tại dòng thực hiện phép nhân/chia do 'cong_suat_w' thu được từ input() có kiểu dữ liệu là str (chuỗi).
# Khắc phục: Ép kiểu 'cong_suat_w' sang kiểu float bằng float(cong_suat_w) trước khi tính toán.
