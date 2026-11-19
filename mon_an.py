
from validate import (
    nhap_so_thuc,
    nhap_chuoi_khong_rong,
    kiem_tra_ma_trung,
    tim_vi_tri_theo_ma,
)

CAC_TRANG_THAI_MON = ("Còn bán", "Hết hàng")


def them_mon(danh_sach_mon):

    print("\n--- THÊM MÓN ĂN ---")

    while True:
        ma_mon = nhap_chuoi_khong_rong("Nhập mã món: ")
        if kiem_tra_ma_trung(danh_sach_mon, "ma_mon", ma_mon):
            print(">> Lỗi: Mã món đã tồn tại, vui lòng nhập mã khác.")
            continue
        break

    ten_mon = nhap_chuoi_khong_rong("Nhập tên món: ")
    loai_mon = nhap_chuoi_khong_rong("Nhập loại món (vd: Khai vị, Món chính, Nước uống): ")
    don_gia = nhap_so_thuc("Nhập đơn giá (VNĐ): ")

    while True:
        trang_thai = input("Nhập trạng thái (Còn bán / Hết hàng): ").strip()
        if trang_thai in CAC_TRANG_THAI_MON:
            break
        print(">> Lỗi: Trạng thái chỉ được là 'Còn bán' hoặc 'Hết hàng'.")

    mon_moi = {
        "ma_mon": ma_mon,
        "ten_mon": ten_mon,
        "loai_mon": loai_mon,
        "don_gia": don_gia,
        "trang_thai": trang_thai,
        "so_luong_da_goi": 0,
    }

    danh_sach_mon.append(mon_moi)
    print(f">> Đã thêm món {ma_mon} - {ten_mon} thành công!")


def hien_thi_1_mon(mon):

    print(
        f"{mon['ma_mon']:<8}"
        f"{mon['ten_mon']:<20}"
        f"{mon['loai_mon']:<14}"
        f"{mon['don_gia']:<12,.0f}"
        f"{mon['trang_thai']:<10}"
        f"{mon['so_luong_da_goi']:<6}"
    )


def hien_thi_danh_sach(danh_sach_mon):
    print("\n--- DANH SÁCH MÓN ĂN ---")
    if len(danh_sach_mon) == 0:
        print(">> Thực đơn hiện đang trống.")
        return

    tieu_de = (
        f"{'Mã':<8}{'Tên món':<20}{'Loại':<14}{'Đơn giá':<12}"
        f"{'Trạng thái':<10}{'Đã gọi':<6}"
    )
    print(tieu_de)
    print("-" * len(tieu_de))
    for mon in danh_sach_mon:
        hien_thi_1_mon(mon)
    print(f"\nTổng số món: {len(danh_sach_mon)}")


def cap_nhat_mon(danh_sach_mon):

    print("\n--- CẬP NHẬT MÓN ĂN ---")
    ma_mon = nhap_chuoi_khong_rong("Nhập mã món cần cập nhật: ")
    vi_tri = tim_vi_tri_theo_ma(danh_sach_mon, "ma_mon", ma_mon)

    if vi_tri == -1:
        print(">> Lỗi: Không tìm thấy món với mã này.")
        return

    mon = danh_sach_mon[vi_tri]
    print("Thông tin hiện tại:")
    hien_thi_1_mon(mon)
    print("\n(Nhấn Enter để giữ nguyên giá trị cũ ở mỗi mục)")

    ten_moi = input(f"Tên món [{mon['ten_mon']}]: ").strip()
    if ten_moi != "":
        mon["ten_mon"] = ten_moi

    loai_moi = input(f"Loại món [{mon['loai_mon']}]: ").strip()
    if loai_moi != "":
        mon["loai_mon"] = loai_moi

    don_gia_moi = input(f"Đơn giá [{mon['don_gia']}]: ").strip()
    if don_gia_moi != "":
        try:
            gia_tri = float(don_gia_moi)
            if gia_tri <= 0:
                print(">> Lỗi: Đơn giá phải > 0, giữ nguyên giá trị cũ.")
            else:
                mon["don_gia"] = gia_tri
        except ValueError:
            print(">> Lỗi: Dữ liệu không hợp lệ, giữ nguyên giá trị cũ.")

    trang_thai_moi = input(f"Trạng thái (Còn bán/Hết hàng) [{mon['trang_thai']}]: ").strip()
    if trang_thai_moi != "":
        if trang_thai_moi in CAC_TRANG_THAI_MON:
            mon["trang_thai"] = trang_thai_moi
        else:
            print(">> Lỗi: Trạng thái không hợp lệ, giữ nguyên giá trị cũ.")

    print(">> Cập nhật thành công!")


def xoa_mon(danh_sach_mon):

    print("\n--- XÓA MÓN ĂN ---")
    ma_mon = nhap_chuoi_khong_rong("Nhập mã món cần xóa: ")
    vi_tri = tim_vi_tri_theo_ma(danh_sach_mon, "ma_mon", ma_mon)

    if vi_tri == -1:
        print(">> Lỗi: Không tìm thấy món với mã này.")
        return

    mon = danh_sach_mon[vi_tri]
    xac_nhan = input(f"Xác nhận xóa món '{mon['ten_mon']}'? (y/n): ").strip().lower()
    if xac_nhan != "y":
        print(">> Đã hủy thao tác xóa.")
        return

    danh_sach_mon.pop(vi_tri)
    print(f">> Đã xóa món {ma_mon} thành công!")
