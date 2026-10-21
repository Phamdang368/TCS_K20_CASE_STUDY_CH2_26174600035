cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000

# Tính điện năng tiêu thụ (kWh) và chi phí (VND)
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

# In giá trị và kiểu dữ liệu
print("Điện năng (kWh):", dien_nang_kwh, "| Kiểu:", type(dien_nang_kwh))
print("Chi phí (VND):", chi_phi, "| Kiểu:", type(chi_phi))

# Thay so_phut = 60 và chạy lại
so_phut_moi = 60
dien_nang_moi = cong_suat_w * so_phut_moi / 60 / 1000
chi_phi_moi = dien_nang_moi * don_gia_kwh
print("--- Khi thay so_phut = 60 ---")
print("Điện năng mới:", dien_nang_moi, "| Chi phí mới:", chi_phi_moi)
