
def sap_xep_theo_ten(danh_sach_mon, tang_dan=True):
    return sorted(danh_sach_mon, key=lambda m: m["ten_mon"].lower(), reverse=not tang_dan)


def sap_xep_theo_don_gia(danh_sach_mon, tang_dan=True):
    return sorted(danh_sach_mon, key=lambda m: m["don_gia"], reverse=not tang_dan)


def menu_sap_xep(danh_sach_mon):

    from mon_an import hien_thi_1_mon

    if len(danh_sach_mon) == 0:
        print(">> Thực đơn đang trống, không có gì để sắp xếp.")
        return

    print("\n--- SẮP XẾP MÓN ĂN ---")
    print("1. Theo tên món")
    print("2. Theo đơn giá")
    lua_chon = input("Chọn tiêu chí sắp xếp: ").strip()

    thu_tu = input("Sắp xếp tăng dần? (y/n, mặc định y): ").strip().lower()
    tang_dan = thu_tu != "n"

    if lua_chon == "1":
        ket_qua = sap_xep_theo_ten(danh_sach_mon, tang_dan)
    elif lua_chon == "2":
        ket_qua = sap_xep_theo_don_gia(danh_sach_mon, tang_dan)
    else:
        print(">> Lựa chọn không hợp lệ.")
        return

    print(f"\n>> Kết quả sắp xếp ({'tăng dần' if tang_dan else 'giảm dần'}):")
    tieu_de = (
        f"{'Mã':<8}{'Tên món':<20}{'Loại':<14}{'Đơn giá':<12}"
        f"{'Trạng thái':<10}{'Đã gọi':<6}"
    )
    print(tieu_de)
    print("-" * len(tieu_de))
    for mon in ket_qua:
        hien_thi_1_mon(mon)
