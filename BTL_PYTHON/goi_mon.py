

from validate import nhap_so_nguyen_duong, nhap_chuoi_khong_rong, tim_vi_tri_theo_ma
from ban_an import tim_ban_theo_ma


def goi_mon(danh_sach_mon, danh_sach_ban, don_hang_dang_mo):
    print("\n--- GỌI MÓN ---")

    if len(danh_sach_ban) == 0:
        print(">> Chưa có bàn nào, vui lòng thêm bàn trước (mục 12).")
        return

    ma_ban = nhap_chuoi_khong_rong("Nhập mã bàn: ")
    ban = tim_ban_theo_ma(danh_sach_ban, ma_ban)
    if ban is None:
        print(">> Lỗi: Bàn không tồn tại.")
        return

    ma_mon = nhap_chuoi_khong_rong("Nhập mã món: ")
    vi_tri_mon = tim_vi_tri_theo_ma(danh_sach_mon, "ma_mon", ma_mon)
    if vi_tri_mon == -1:
        print(">> Lỗi: Món không tồn tại.")
        return

    mon = danh_sach_mon[vi_tri_mon]
    if mon["trang_thai"] == "Hết hàng":
        print(">> Lỗi: Món này hiện đã hết hàng, không thể gọi.")
        return

    so_luong = nhap_so_nguyen_duong("Nhập số lượng: ")
    thanh_tien = mon["don_gia"] * so_luong

    dong_goi_mon = {
        "ma_mon": mon["ma_mon"],
        "ten_mon": mon["ten_mon"],
        "don_gia": mon["don_gia"],
        "so_luong": so_luong,
        "thanh_tien": thanh_tien,
    }

    if ma_ban not in don_hang_dang_mo:
        don_hang_dang_mo[ma_ban] = []
    don_hang_dang_mo[ma_ban].append(dong_goi_mon)

    mon["so_luong_da_goi"] += so_luong
    ban["trang_thai"] = "Đang phục vụ"

    print(
        f">> Đã gọi {so_luong} x {mon['ten_mon']} cho bàn {ban['so_ban']} "
        f"- Thành tiền: {thanh_tien:,.0f} VNĐ"
    )


def hien_thi_don_hang_cua_ban(don_hang_dang_mo, ma_ban):

    danh_sach_dong = don_hang_dang_mo.get(ma_ban, [])
    if len(danh_sach_dong) == 0:
        print(">> Bàn này chưa gọi món nào.")
        return

    tieu_de = f"{'Món':<20}{'Đơn giá':<12}{'SL':<5}{'Thành tiền':<15}"
    print(tieu_de)
    print("-" * len(tieu_de))
    for dong in danh_sach_dong:
        print(
            f"{dong['ten_mon']:<20}{dong['don_gia']:<12,.0f}"
            f"{dong['so_luong']:<5}{dong['thanh_tien']:<15,.0f}"
        )
