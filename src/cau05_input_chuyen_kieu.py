# Nhập dữ liệu và kiểm tra kiểu dữ liệu ban đầu
ma_may = input("Nhập mã máy: ")
print("Kiểu ma_may:", type(ma_may))

cong_suat_raw = input("Nhập công suất W: ")
print("Kiểu cong_suat ban đầu:", type(cong_suat_raw))

so_phut_raw = input("Nhập số phút sử dụng: ")
print("Kiểu so_phut ban đầu:", type(so_phut_raw))

don_gia_raw = input("Nhập đơn giá điện/kWh: ")
print("Kiểu don_gia ban đầu:", type(don_gia_raw))

# Chuyển đổi kiểu dữ liệu
cong_suat_w = float(cong_suat_raw)
so_phut = int(so_phut_raw)
don_gia_kwh = float(don_gia_raw)

# Tính toán lại
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print(f"Điện năng: {dien_nang_kwh} kWh")
print(f"Chi phí: {chi_phi} VND")
