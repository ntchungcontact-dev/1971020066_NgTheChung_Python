
from mon_an import them_mon, hien_thi_danh_sach, cap_nhat_mon, xoa_mon
from ban_an import menu_quan_ly_ban
from tim_kiem import menu_tim_kiem
from sap_xep import menu_sap_xep
from goi_mon import goi_mon
from thanh_toan import thanh_toan
from thong_ke import in_thong_ke
from file_io import luu_du_lieu, doc_du_lieu


def in_menu():
    print("\n========================================")
    print("           QUẢN LÝ NHÀ HÀNG")
    print("========================================")
    print("1. Thêm món")
    print("2. Hiển thị món ăn")
    print("3. Tìm kiếm")
    print("4. Sắp xếp")
    print("5. Gọi món")
    print("6. Thanh toán")
    print("7. Thống kê")
    print("8. Lưu dữ liệu")
    print("9. Đọc dữ liệu")
    print("10. Cập nhật món")
    print("11. Xóa món")
    print("12. Quản lý bàn ăn (thêm / hiển thị bàn)")
    print("0. Thoát")
    print("========================================")


def main():
    danh_sach_mon = []
    danh_sach_ban = []
    don_hang_dang_mo = {}   # {ma_ban: [dòng gọi món]}
    lich_su_hoa_don = []    # list các hóa đơn đã thanh toán, phục vụ thống kê

    while True:
        in_menu()
        lua_chon = input("Lựa chọn: ").strip()

        try:
            if lua_chon == "1":
                them_mon(danh_sach_mon)
            elif lua_chon == "2":
                hien_thi_danh_sach(danh_sach_mon)
            elif lua_chon == "3":
                menu_tim_kiem(danh_sach_mon)
            elif lua_chon == "4":
                menu_sap_xep(danh_sach_mon)
            elif lua_chon == "5":
                goi_mon(danh_sach_mon, danh_sach_ban, don_hang_dang_mo)
            elif lua_chon == "6":
                thanh_toan(danh_sach_ban, don_hang_dang_mo, lich_su_hoa_don)
            elif lua_chon == "7":
                in_thong_ke(danh_sach_mon, lich_su_hoa_don)
            elif lua_chon == "8":
                luu_du_lieu(danh_sach_mon, danh_sach_ban)
            elif lua_chon == "9":
                mon_doc_duoc, ban_doc_duoc = doc_du_lieu()
                if mon_doc_duoc:
                    danh_sach_mon = mon_doc_duoc
                if ban_doc_duoc:
                    danh_sach_ban = ban_doc_duoc
            elif lua_chon == "10":
                cap_nhat_mon(danh_sach_mon)
            elif lua_chon == "11":
                xoa_mon(danh_sach_mon)
            elif lua_chon == "12":
                menu_quan_ly_ban(danh_sach_ban)
            elif lua_chon == "0":
                print("\nCảm ơn đã sử dụng chương trình. Tạm biệt!")
                break
            else:
                print(">> Lựa chọn không hợp lệ, vui lòng chọn lại.")

        except Exception as loi:

            print(f">> Đã có lỗi xảy ra: {loi}")

        input("\nNhấn Enter để tiếp tục...")


if __name__ == "__main__":
    main()
