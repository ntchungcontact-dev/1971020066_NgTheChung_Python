

from validate import nhap_chuoi_khong_rong
from ban_an import tim_ban_theo_ma
from goi_mon import hien_thi_don_hang_cua_ban


def tinh_tong_hoa_don(don_hang_dang_mo, ma_ban):
    danh_sach_dong = don_hang_dang_mo.get(ma_ban, [])
    return sum(dong["thanh_tien"] for dong in danh_sach_dong)


def thanh_toan(danh_sach_ban, don_hang_dang_mo, lich_su_hoa_don):
    print("\n--- THANH TOÁN ---")

    ma_ban = nhap_chuoi_khong_rong("Nhập mã bàn cần thanh toán: ")
    ban = tim_ban_theo_ma(danh_sach_ban, ma_ban)
    if ban is None:
        print(">> Lỗi: Bàn không tồn tại.")
        return

    danh_sach_dong = don_hang_dang_mo.get(ma_ban, [])
    if len(danh_sach_dong) == 0:
        print(">> Lỗi: Bàn này chưa gọi món nào, không có gì để thanh toán.")
        return

    print(f"\n>> HÓA ĐƠN BÀN {ban['so_ban']} (Mã bàn: {ma_ban})")
    hien_thi_don_hang_cua_ban(don_hang_dang_mo, ma_ban)

    tong_tien = tinh_tong_hoa_don(don_hang_dang_mo, ma_ban)
    print("-" * 40)
    print(f"TỔNG CỘNG: {tong_tien:,.0f} VNĐ")


    lich_su_hoa_don.append({
        "ma_ban": ma_ban,
        "so_ban": ban["so_ban"],
        "danh_sach_mon": danh_sach_dong,
        "tong_tien": tong_tien,
    })


    del don_hang_dang_mo[ma_ban]
    ban["trang_thai"] = "Trống"

    print(f">> Đã thanh toán xong, bàn {ban['so_ban']} đã được trả về trạng thái Trống.")
