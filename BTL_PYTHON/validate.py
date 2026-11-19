


def nhap_so_thuc(thong_bao, cho_phep_bang_khong=False):
    while True:
        chuoi_nhap = input(thong_bao).strip()
        try:
            gia_tri = float(chuoi_nhap)
        except ValueError:
            print(">> Lỗi: Vui lòng nhập một con số hợp lệ (vd: 25000 hoặc 25000.5).")
            continue

        if cho_phep_bang_khong:
            if gia_tri < 0:
                print(">> Lỗi: Giá trị không được âm.")
                continue
        else:
            if gia_tri <= 0:
                print(">> Lỗi: Giá trị phải lớn hơn 0.")
                continue

        return gia_tri


def nhap_so_nguyen_duong(thong_bao):
    while True:
        chuoi_nhap = input(thong_bao).strip()
        try:
            gia_tri = int(chuoi_nhap)
        except ValueError:
            print(">> Lỗi: Vui lòng nhập một số nguyên hợp lệ (vd: 1, 2, 3).")
            continue

        if gia_tri <= 0:
            print(">> Lỗi: Số lượng phải lớn hơn 0.")
            continue

        return gia_tri


def nhap_chuoi_khong_rong(thong_bao):
    while True:
        chuoi_nhap = input(thong_bao).strip()
        if chuoi_nhap == "":
            print(">> Lỗi: Không được để trống.")
            continue
        return chuoi_nhap


def kiem_tra_ma_trung(danh_sach, ten_khoa_ma, ma_can_kiem_tra, ma_dang_sua=None):
    for phan_tu in danh_sach:
        if phan_tu[ten_khoa_ma] == ma_can_kiem_tra and ma_can_kiem_tra != ma_dang_sua:
            return True
    return False


def tim_vi_tri_theo_ma(danh_sach, ten_khoa_ma, ma_can_tim):
    for vi_tri, phan_tu in enumerate(danh_sach):
        if phan_tu[ten_khoa_ma] == ma_can_tim:
            return vi_tri
    return -1
