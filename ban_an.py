

from validate import nhap_chuoi_khong_rong, kiem_tra_ma_trung, tim_vi_tri_theo_ma

CAC_TRANG_THAI_BAN = ("Trống", "Đang phục vụ")


def them_ban(danh_sach_ban):

    print("\n--- THÊM BÀN ĂN ---")

    while True:
        ma_ban = nhap_chuoi_khong_rong("Nhập mã bàn: ")
        if kiem_tra_ma_trung(danh_sach_ban, "ma_ban", ma_ban):
            print(">> Lỗi: Mã bàn đã tồn tại, vui lòng nhập mã khác.")
            continue
        break

    so_ban = nhap_chuoi_khong_rong("Nhập số bàn: ")

    ban_moi = {
        "ma_ban": ma_ban,
        "so_ban": so_ban,
        "trang_thai": "Trống",
    }
    danh_sach_ban.append(ban_moi)
    print(f">> Đã thêm bàn {ma_ban} (số {so_ban}) thành công!")


def hien_thi_1_ban(ban):
    print(f"{ban['ma_ban']:<8}{ban['so_ban']:<8}{ban['trang_thai']:<15}")


def hien_thi_danh_sach_ban(danh_sach_ban):

    print("\n--- DANH SÁCH BÀN ĂN ---")
    if len(danh_sach_ban) == 0:
        print(">> Danh sách bàn hiện đang trống.")
        return

    tieu_de = f"{'Mã bàn':<8}{'Số bàn':<8}{'Trạng thái':<15}"
    print(tieu_de)
    print("-" * len(tieu_de))
    for ban in danh_sach_ban:
        hien_thi_1_ban(ban)
    print(f"\nTổng số bàn: {len(danh_sach_ban)}")


def tim_ban_theo_ma(danh_sach_ban, ma_ban):

    vi_tri = tim_vi_tri_theo_ma(danh_sach_ban, "ma_ban", ma_ban)
    if vi_tri == -1:
        return None
    return danh_sach_ban[vi_tri]


def menu_quan_ly_ban(danh_sach_ban):

    print("\n--- QUẢN LÝ BÀN ĂN ---")
    print("1. Thêm bàn")
    print("2. Hiển thị danh sách bàn")
    lua_chon = input("Chọn chức năng: ").strip()

    if lua_chon == "1":
        them_ban(danh_sach_ban)
    elif lua_chon == "2":
        hien_thi_danh_sach_ban(danh_sach_ban)
    else:
        print(">> Lựa chọn không hợp lệ.")
