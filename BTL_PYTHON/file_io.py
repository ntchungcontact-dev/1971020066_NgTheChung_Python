
import os

TEN_FILE_MON_MAC_DINH = "data/mon_an.txt"
TEN_FILE_BAN_MAC_DINH = "data/ban_an.txt"
DAU_PHAN_CACH = "|"

CAC_TRUONG_MON = ["ma_mon", "ten_mon", "loai_mon", "don_gia", "trang_thai", "so_luong_da_goi"]
CAC_TRUONG_MON_SO_THUC = {"don_gia"}
CAC_TRUONG_MON_SO_NGUYEN = {"so_luong_da_goi"}

CAC_TRUONG_BAN = ["ma_ban", "so_ban", "trang_thai"]


def _tao_thu_muc_neu_can(ten_file):
    thu_muc = os.path.dirname(ten_file)
    if thu_muc and not os.path.exists(thu_muc):
        os.makedirs(thu_muc)


def luu_mon_an(danh_sach_mon, ten_file=TEN_FILE_MON_MAC_DINH):

    try:
        _tao_thu_muc_neu_can(ten_file)
        with open(ten_file, "w", encoding="utf-8") as file:
            for mon in danh_sach_mon:
                dong = DAU_PHAN_CACH.join(str(mon[truong]) for truong in CAC_TRUONG_MON)
                file.write(dong + "\n")
        print(f">> Đã lưu {len(danh_sach_mon)} món vào file '{ten_file}'.")
        return True
    except (IOError, OSError) as loi:
        print(f">> Lỗi: Không thể ghi file '{ten_file}'. Chi tiết: {loi}")
        return False


def doc_mon_an(ten_file=TEN_FILE_MON_MAC_DINH):

    if not os.path.exists(ten_file):
        print(f">> Lỗi: File '{ten_file}' không tồn tại.")
        return []

    danh_sach_mon = []
    try:
        with open(ten_file, "r", encoding="utf-8") as file:
            for so_dong, dong in enumerate(file, start=1):
                dong = dong.strip()
                if dong == "":
                    continue

                cac_gia_tri = dong.split(DAU_PHAN_CACH)
                if len(cac_gia_tri) != len(CAC_TRUONG_MON):
                    print(f">> Cảnh báo: Bỏ qua dòng {so_dong} do sai định dạng.")
                    continue

                try:
                    mon = {}
                    for ten_truong, gia_tri in zip(CAC_TRUONG_MON, cac_gia_tri):
                        if ten_truong in CAC_TRUONG_MON_SO_THUC:
                            mon[ten_truong] = float(gia_tri)
                        elif ten_truong in CAC_TRUONG_MON_SO_NGUYEN:
                            mon[ten_truong] = int(gia_tri)
                        else:
                            mon[ten_truong] = gia_tri
                    danh_sach_mon.append(mon)
                except ValueError:
                    print(f">> Cảnh báo: Bỏ qua dòng {so_dong} do dữ liệu số không hợp lệ.")
                    continue

        print(f">> Đã đọc {len(danh_sach_mon)} món từ file '{ten_file}'.")
        return danh_sach_mon
    except (IOError, OSError) as loi:
        print(f">> Lỗi: Không thể đọc file '{ten_file}'. Chi tiết: {loi}")
        return []


def luu_ban_an(danh_sach_ban, ten_file=TEN_FILE_BAN_MAC_DINH):

    try:
        _tao_thu_muc_neu_can(ten_file)
        with open(ten_file, "w", encoding="utf-8") as file:
            for ban in danh_sach_ban:
                dong = DAU_PHAN_CACH.join(str(ban[truong]) for truong in CAC_TRUONG_BAN)
                file.write(dong + "\n")
        print(f">> Đã lưu {len(danh_sach_ban)} bàn vào file '{ten_file}'.")
        return True
    except (IOError, OSError) as loi:
        print(f">> Lỗi: Không thể ghi file '{ten_file}'. Chi tiết: {loi}")
        return False


def doc_ban_an(ten_file=TEN_FILE_BAN_MAC_DINH):

    if not os.path.exists(ten_file):
        print(f">> Lỗi: File '{ten_file}' không tồn tại.")
        return []

    danh_sach_ban = []
    try:
        with open(ten_file, "r", encoding="utf-8") as file:
            for so_dong, dong in enumerate(file, start=1):
                dong = dong.strip()
                if dong == "":
                    continue

                cac_gia_tri = dong.split(DAU_PHAN_CACH)
                if len(cac_gia_tri) != len(CAC_TRUONG_BAN):
                    print(f">> Cảnh báo: Bỏ qua dòng {so_dong} do sai định dạng.")
                    continue

                ban = dict(zip(CAC_TRUONG_BAN, cac_gia_tri))
                danh_sach_ban.append(ban)

        print(f">> Đã đọc {len(danh_sach_ban)} bàn từ file '{ten_file}'.")
        return danh_sach_ban
    except (IOError, OSError) as loi:
        print(f">> Lỗi: Không thể đọc file '{ten_file}'. Chi tiết: {loi}")
        return []


def luu_du_lieu(danh_sach_mon, danh_sach_ban):

    ket_qua_mon = luu_mon_an(danh_sach_mon)
    ket_qua_ban = luu_ban_an(danh_sach_ban)
    return ket_qua_mon and ket_qua_ban


def doc_du_lieu():

    danh_sach_mon = doc_mon_an()
    danh_sach_ban = doc_ban_an()
    return danh_sach_mon, danh_sach_ban
