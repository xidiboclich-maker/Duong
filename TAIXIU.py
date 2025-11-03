import random

def choi_tai_xiu_dat_cuoc():
    """
    Hàm mô phỏng trò chơi Tài Xỉu có tính năng đặt cược và quản lý tiền.
    """
    print("=====================================================")
    print("🌟 CHÀO MỪNG ĐẾN VỚI TRÒ CHƠI TÀI XỈU (SIC BO) CÓ CƯỢC! 🌟")
    print("=====================================================")

    # 1. NHẬP SỐ TIỀN BAN ĐẦU
    while True:
        try:
            tai_khoan = int(input("💰 Vui lòng nhập số tiền vốn ban đầu của bạn (ví dụ: 1000): "))
            if tai_khoan > 0:
                break
            else:
                print("Số tiền phải lớn hơn 0.")
        except ValueError:
            print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")

    while tai_khoan > 0:
        print(f"\n💵 Số tiền hiện có của bạn: {tai_khoan}")
        print("\n---")

        # 2. NHẬP LỰA CHỌN CƯỢC
        print("Lựa chọn cược:")
        print("  1. Tài (Tổng 11-17, không Bão) | Tỉ lệ 1:1")
        print("  2. Xỉu (Tổng 4-10, không Bão) | Tỉ lệ 1:1")
        print("  3. Bão (Triple - 3 số giống nhau) | Tỉ lệ 1:30")
        
        lua_chon_cuoc = input("Chọn cược (Nhập 'Tai', 'Xiu' hoặc 'Bao') hoặc 'Thoat' để dừng: ").lower()

        if lua_chon_cuoc == 'thoat':
            break
        
        if lua_chon_cuoc not in ['tai', 'xiu', 'bao']:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
            continue

        # 3. NHẬP SỐ TIỀN CƯỢC
        while True:
            try:
                tien_cuoc = int(input(f"Đặt cược bao nhiêu tiền cho '{lua_chon_cuoc.upper()}'? "))
                if 0 < tien_cuoc <= tai_khoan:
                    break
                elif tien_cuoc <= 0:
                    print("Số tiền cược phải lớn hơn 0.")
                else:
                    print(f"Số tiền cược không được vượt quá số dư hiện có ({tai_khoan}).")
            except ValueError:
                print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")
        
        # 4. TUNG XÚC XẮC
        print("\n--- LẮC XÚC XẮC! ---")
        xuc_xac_1 = random.randint(1, 6)
        xuc_xac_2 = random.randint(1, 6)
        xuc_xac_3 = random.randint(1, 6)
        tong_diem = xuc_xac_1 + xuc_xac_2 + xuc_xac_3

        print(f"Ba viên xúc xắc ra: [{xuc_xac_1}, {xuc_xac_2}, {xuc_xac_3}]")
        print(f"👉 Tổng điểm là: {tong_diem}")

        # 5. XÁC ĐỊNH KẾT QUẢ VÀ TÍNH TOÁN
        
        thang_cuoc = False
        ti_le_thang = 0
        ket_qua_game = ""
        
        is_bao = (xuc_xac_1 == xuc_xac_2 == xuc_xac_3)
        
        if is_bao:
            ket_qua_game = "Bão (Triple)"
            print("⚡ KẾT QUẢ GAME: Bão! (Mọi cược Tài/Xỉu đều thua)")
            if lua_chon_cuoc == 'bao':
                thang_cuoc = True
                ti_le_thang = 30 # Tỉ lệ Bão 1:30
                print(f"🎉 Chúc mừng! Bạn đã thắng cược Bão!")
        
        elif 11 <= tong_diem <= 17:
            ket_qua_game = "Tài (Big)"
            print("⭐ KẾT QUẢ GAME: Tài!")
            if lua_chon_cuoc == 'tai':
                thang_cuoc = True
                ti_le_thang = 1 # Tỉ lệ Tài/Xỉu 1:1
                print(f"🎉 Chúc mừng! Bạn đã thắng cược Tài!")
        
        elif 4 <= tong_diem <= 10:
            ket_qua_game = "Xỉu (Small)"
            print("⭐ KẾT QUẢ GAME: Xỉu!")
            if lua_chon_cuoc == 'xiu':
                thang_cuoc = True
                ti_le_thang = 1 # Tỉ lệ Tài/Xỉu 1:1
                print(f"🎉 Chúc mừng! Bạn đã thắng cược Xỉu!")
        
        # Cập nhật tiền
        if thang_cuoc:
            tien_thang = tien_cuoc * ti_le_thang
            tai_khoan += tien_thang
            print(f"💵 Bạn thắng: +{tien_thang} (Tổng thưởng = cược * {ti_le_thang})")
        else:
            tai_khoan -= tien_cuoc
            print(f"💸 Bạn thua: -{tien_cuoc}. Kết quả là {ket_qua_game}.")
        
        print(f"--- SỐ DƯ MỚI: {tai_khoan} ---")
        
        if tai_khoan <= 0:
            print("\n❌ Bạn đã hết tiền. Trò chơi kết thúc.")
            break
            
    print("\n👋 Cảm ơn bạn đã chơi. Tạm biệt!")
    print(f"Số tiền cuối cùng của bạn là: {tai_khoan}")

# Chạy trò chơi
if __name__ == "__main__":
    choi_tai_xiu_dat_cuoc()
