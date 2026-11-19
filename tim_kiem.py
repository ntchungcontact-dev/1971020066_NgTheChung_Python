
def tim_theo_ma_mon(danh_sach_mon, ma_mon):
    ma_mon = ma_mon.strip().lower()
    return [m for m in danh_sach_mon if m["ma_mon"].lower() == ma_mon]


def tim_theo_ten_mon(danh_sach_mon, ten):
    ten = ten.strip().lower()
    return [m for m in danh_sach_mon if ten in m["ten_mon"].lower()]


def tim_theo_loai_mon(danh_sach_mon, loai):
    loai = loai.strip().lower()
    return [m for m in danh_sach_mon if m["loai_mon"].lower() == loai]


def menu_tim_kiem(danh_sach_mon):
    from mon_an import hien_thi_1_mon

    print("\n--- TÌM KIẾM MÓN ĂN ---")
    print("1. Theo mã món")
    print("2. Theo tên món")
    print("3. Theo loại món")
    lua_chon = input("Chọn cách tìm kiếm: ").strip()

    ket_qua = []
    if lua_chon == "1":
        tu_khoa = input("Nhập mã món: ")
        ket_qua = tim_theo_ma_mon(danh_sach_mon, tu_khoa)
    elif lua_chon == "2":
        tu_khoa = input("Nhập tên món: ")
        ket_qua = tim_theo_ten_mon(danh_sach_mon, tu_khoa)
    elif lua_chon == "3":
        tu_khoa = input("Nhập loại món: ")
        ket_qua = tim_theo_loai_mon(danh_sach_mon, tu_khoa)
    else:
        print(">> Lựa chọn không hợp lệ.")
        return

    if len(ket_qua) == 0:
        print(">> Không tìm thấy món nào phù hợp.")
    else:
        print(f"\n>> Tìm thấy {len(ket_qua)} món:")
        for mon in ket_qua:
            hien_thi_1_mon(mon)
