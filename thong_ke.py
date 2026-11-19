
def thong_ke_tong_hop(danh_sach_mon, lich_su_hoa_don):
    tong_so_mon = len(danh_sach_mon)

    mon_gia_cao_nhat = None
    if tong_so_mon > 0:
        mon_gia_cao_nhat = max(danh_sach_mon, key=lambda m: m["don_gia"])

    mon_goi_nhieu_nhat = None
    if tong_so_mon > 0:
        mon_goi_nhieu_nhat = max(danh_sach_mon, key=lambda m: m["so_luong_da_goi"])
        if mon_goi_nhieu_nhat["so_luong_da_goi"] == 0:
            mon_goi_nhieu_nhat = None  # chưa có món nào được gọi

    tong_doanh_thu = sum(hoa_don["tong_tien"] for hoa_don in lich_su_hoa_don)

    doanh_thu_theo_loai = {}
    for hoa_don in lich_su_hoa_don:
        for dong in hoa_don["danh_sach_mon"]:
            loai = _tim_loai_mon(danh_sach_mon, dong["ma_mon"])
            doanh_thu_theo_loai[loai] = doanh_thu_theo_loai.get(loai, 0) + dong["thanh_tien"]

    return {
        "tong_so_mon": tong_so_mon,
        "mon_gia_cao_nhat": mon_gia_cao_nhat,
        "mon_goi_nhieu_nhat": mon_goi_nhieu_nhat,
        "tong_doanh_thu": tong_doanh_thu,
        "doanh_thu_theo_loai": doanh_thu_theo_loai,
    }


def _tim_loai_mon(danh_sach_mon, ma_mon):
    for mon in danh_sach_mon:
        if mon["ma_mon"] == ma_mon:
            return mon["loai_mon"]
    return "Không xác định"


def in_thong_ke(danh_sach_mon, lich_su_hoa_don):
    print("\n--- THỐNG KÊ ---")
    if len(danh_sach_mon) == 0:
        print(">> Thực đơn đang trống, chưa có dữ liệu để thống kê.")
        return

    ket_qua = thong_ke_tong_hop(danh_sach_mon, lich_su_hoa_don)

    print(f"Tổng số món            : {ket_qua['tong_so_mon']}")

    if ket_qua["mon_gia_cao_nhat"]:
        mon = ket_qua["mon_gia_cao_nhat"]
        print(f"Món có giá cao nhất     : {mon['ten_mon']} ({mon['don_gia']:,.0f} VNĐ)")

    if ket_qua["mon_goi_nhieu_nhat"]:
        mon = ket_qua["mon_goi_nhieu_nhat"]
        print(f"Món được gọi nhiều nhất : {mon['ten_mon']} ({mon['so_luong_da_goi']} lượt)")
    else:
        print("Món được gọi nhiều nhất : (chưa có món nào được gọi)")

    print(f"Tổng doanh thu          : {ket_qua['tong_doanh_thu']:,.0f} VNĐ")

    print("Doanh thu theo loại món :")
    if len(ket_qua["doanh_thu_theo_loai"]) == 0:
        print("   (chưa có hóa đơn nào được thanh toán)")
    else:
        for loai, doanh_thu in ket_qua["doanh_thu_theo_loai"].items():
            print(f"   - {loai:<15}: {doanh_thu:,.0f} VNĐ")
