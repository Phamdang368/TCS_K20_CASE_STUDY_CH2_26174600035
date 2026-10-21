tong_phut = 135
cong_suat_w = 250

# Dùng // và % để tính số giờ trọn vẹn và số phút còn lại
so_gio = tong_phut // 60
so_phut_du = tong_phut % 60
print(f"Thời gian: {so_gio} giờ {so_phut_du} phút")

# Tạo biến su_dung_lau và du_lieu_hop_le
su_dung_lau = tong_phut > 60
du_lieu_hop_le = (cong_suat_w > 0) and (tong_phut > 0)

print("Sử dụng lâu:", su_dung_lau)
print("Dữ liệu hợp lệ:", du_lieu_hop_le)

# Dự đoán: 100 + 20 * 3 = 160 | (100 + 20) * 3 = 360
print("100 + 20 * 3 =", 100 + 20 * 3)
print("(100 + 20) * 3 =", (100 + 20) * 3)
