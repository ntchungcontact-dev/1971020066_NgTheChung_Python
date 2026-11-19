import json
from pathlib import Path

import streamlit as st

from file_io import doc_ban_an, doc_mon_an, luu_ban_an, luu_mon_an
from sap_xep import sap_xep_theo_don_gia, sap_xep_theo_ten
from thong_ke import thong_ke_tong_hop
from tim_kiem import tim_theo_loai_mon, tim_theo_ten_mon


THU_MUC_DU_LIEU = Path(__file__).resolve().parent / "data"
FILE_MON_AN = THU_MUC_DU_LIEU / "mon_an.txt"
FILE_BAN_AN = THU_MUC_DU_LIEU / "ban_an.txt"
FILE_TRANG_THAI_WEB = THU_MUC_DU_LIEU / "trang_thai_web.json"
CAC_TRANG_THAI_MON = ("Còn bán", "Hết hàng")


def doc_trang_thai_web():
    if not FILE_TRANG_THAI_WEB.exists():
        return {"don_hang_dang_mo": {}, "lich_su_hoa_don": []}

    try:
        du_lieu = json.loads(FILE_TRANG_THAI_WEB.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as loi:
        st.error(f"Không thể đọc dữ liệu đơn hàng: {loi}")
        st.stop()

    if (
        not isinstance(du_lieu, dict)
        or not isinstance(du_lieu.get("don_hang_dang_mo"), dict)
        or not isinstance(du_lieu.get("lich_su_hoa_don"), list)
    ):
        st.error(f"Dữ liệu trong '{FILE_TRANG_THAI_WEB.name}' không đúng định dạng.")
        st.stop()
    return du_lieu


def luu_trang_thai_web():
    du_lieu = {
        "don_hang_dang_mo": st.session_state["don_hang_dang_mo"],
        "lich_su_hoa_don": st.session_state["lich_su_hoa_don"],
    }
    try:
        THU_MUC_DU_LIEU.mkdir(parents=True, exist_ok=True)
        file_tam = FILE_TRANG_THAI_WEB.with_suffix(".tmp")
        file_tam.write_text(
            json.dumps(du_lieu, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        file_tam.replace(FILE_TRANG_THAI_WEB)
        return True
    except OSError as loi:
        st.error(f"Không thể lưu đơn hàng: {loi}")
        return False


def luu_thuc_don():
    if luu_mon_an(st.session_state["danh_sach_mon"], str(FILE_MON_AN)):
        return True
    st.error("Không lưu được thực đơn. Kiểm tra quyền ghi thư mục data.")
    return False


def luu_danh_sach_ban():
    if luu_ban_an(st.session_state["danh_sach_ban"], str(FILE_BAN_AN)):
        return True
    st.error("Không lưu được danh sách bàn. Kiểm tra quyền ghi thư mục data.")
    return False


def luu_thuc_don_va_ban():
    mon_da_luu = luu_thuc_don()
    ban_da_luu = luu_danh_sach_ban()
    if mon_da_luu and ban_da_luu:
        return True
    return False


def khoi_tao_du_lieu():
    if "danh_sach_mon" in st.session_state:
        return

    THU_MUC_DU_LIEU.mkdir(parents=True, exist_ok=True)
    st.session_state["danh_sach_mon"] = doc_mon_an(str(FILE_MON_AN))
    st.session_state["danh_sach_ban"] = doc_ban_an(str(FILE_BAN_AN))
    trang_thai = doc_trang_thai_web()
    st.session_state["don_hang_dang_mo"] = trang_thai["don_hang_dang_mo"]
    st.session_state["lich_su_hoa_don"] = trang_thai["lich_su_hoa_don"]


def hien_thi_bang_mon(danh_sach_mon):
    st.dataframe(
        [
            {
                "Mã món": mon["ma_mon"],
                "Tên món": mon["ten_mon"],
                "Loại": mon["loai_mon"],
                "Đơn giá (VNĐ)": mon["don_gia"],
                "Trạng thái": mon["trang_thai"],
                "Đã gọi": mon["so_luong_da_goi"],
            }
            for mon in danh_sach_mon
        ],
        hide_index=True,
        width="stretch",
    )


def trang_thuc_don():
    st.header("Thực đơn")
    danh_sach_mon = st.session_state["danh_sach_mon"]

    if danh_sach_mon:
        cot_loc, cot_sap_xep = st.columns(2)
        cac_loai = sorted({mon["loai_mon"] for mon in danh_sach_mon})
        loai_loc = cot_loc.selectbox("Lọc theo loại", ["Tất cả"] + cac_loai)
        cach_sap_xep = cot_sap_xep.selectbox(
            "Sắp xếp",
            ["Mặc định", "Tên: A-Z", "Tên: Z-A", "Giá: thấp đến cao", "Giá: cao đến thấp"],
        )
        tu_khoa = st.text_input("Tìm theo mã hoặc tên món")

        ket_qua = danh_sach_mon
        if loai_loc != "Tất cả":
            ket_qua = tim_theo_loai_mon(ket_qua, loai_loc)
        if tu_khoa.strip():
            tu_khoa_chuan_hoa = tu_khoa.strip().lower()
            khop_ma = [
                mon
                for mon in ket_qua
                if tu_khoa_chuan_hoa in mon["ma_mon"].lower()
            ]
            khop_ten = tim_theo_ten_mon(ket_qua, tu_khoa)
            ma_khop = {mon["ma_mon"] for mon in khop_ma + khop_ten}
            ket_qua = [mon for mon in ket_qua if mon["ma_mon"] in ma_khop]
        if cach_sap_xep == "Tên: A-Z":
            ket_qua = sap_xep_theo_ten(ket_qua)
        elif cach_sap_xep == "Tên: Z-A":
            ket_qua = sap_xep_theo_ten(ket_qua, tang_dan=False)
        elif cach_sap_xep == "Giá: thấp đến cao":
            ket_qua = sap_xep_theo_don_gia(ket_qua)
        elif cach_sap_xep == "Giá: cao đến thấp":
            ket_qua = sap_xep_theo_don_gia(ket_qua, tang_dan=False)

        hien_thi_bang_mon(ket_qua)
        st.caption(f"Hiển thị {len(ket_qua)} / {len(danh_sach_mon)} món")
    else:
        st.info("Thực đơn chưa có món.")

    with st.expander("Thêm món"):
        with st.form("them_mon_web"):
            ma_mon = st.text_input("Mã món")
            ten_mon = st.text_input("Tên món")
            loai_mon = st.text_input("Loại món")
            don_gia = st.number_input("Đơn giá (VNĐ)", min_value=1, step=1000)
            trang_thai = st.selectbox("Trạng thái", CAC_TRANG_THAI_MON)
            da_gui = st.form_submit_button("Thêm món")

        if da_gui:
            ma_mon = ma_mon.strip()
            ten_mon = ten_mon.strip()
            loai_mon = loai_mon.strip()
            if not ma_mon or not ten_mon or not loai_mon:
                st.error("Mã, tên và loại món không được để trống.")
            elif any(mon["ma_mon"].lower() == ma_mon.lower() for mon in danh_sach_mon):
                st.error("Mã món đã tồn tại.")
            else:
                danh_sach_mon.append(
                    {
                        "ma_mon": ma_mon,
                        "ten_mon": ten_mon,
                        "loai_mon": loai_mon,
                        "don_gia": float(don_gia),
                        "trang_thai": trang_thai,
                        "so_luong_da_goi": 0,
                    }
                )
                if luu_thuc_don():
                    st.success(f"Đã thêm món {ten_mon}.")
                    st.rerun()

    if danh_sach_mon:
        cac_ma_mon = [mon["ma_mon"] for mon in danh_sach_mon]
        with st.expander("Cập nhật món"):
            ma_cap_nhat = st.selectbox("Chọn món cần cập nhật", cac_ma_mon, key="ma_mon_cap_nhat")
            mon_cap_nhat = next(mon for mon in danh_sach_mon if mon["ma_mon"] == ma_cap_nhat)
            with st.form("cap_nhat_mon_web"):
                ten_moi = st.text_input("Tên món", value=mon_cap_nhat["ten_mon"])
                loai_moi = st.text_input("Loại món", value=mon_cap_nhat["loai_mon"])
                gia_moi = st.number_input(
                    "Đơn giá (VNĐ)",
                    min_value=1,
                    value=max(1, int(mon_cap_nhat["don_gia"])),
                    step=1000,
                )
                trang_thai_moi = st.selectbox(
                    "Trạng thái",
                    CAC_TRANG_THAI_MON,
                    index=CAC_TRANG_THAI_MON.index(mon_cap_nhat["trang_thai"]),
                )
                cap_nhat = st.form_submit_button("Lưu thay đổi")

            if cap_nhat:
                if not ten_moi.strip() or not loai_moi.strip():
                    st.error("Tên và loại món không được để trống.")
                else:
                    mon_cap_nhat.update(
                        {
                            "ten_mon": ten_moi.strip(),
                            "loai_mon": loai_moi.strip(),
                            "don_gia": float(gia_moi),
                            "trang_thai": trang_thai_moi,
                        }
                    )
                    if luu_thuc_don():
                        st.success("Đã cập nhật món.")
                        st.rerun()

        with st.expander("Xóa món"):
            ma_xoa = st.selectbox("Chọn món cần xóa", cac_ma_mon, key="ma_mon_xoa")
            xac_nhan = st.checkbox("Tôi xác nhận muốn xóa món này")
            if st.button("Xóa món", disabled=not xac_nhan):
                dang_co_trong_don = any(
                    dong["ma_mon"] == ma_xoa
                    for don in st.session_state["don_hang_dang_mo"].values()
                    for dong in don
                )
                if dang_co_trong_don:
                    st.error("Không thể xóa món đang có trong đơn hàng chưa thanh toán.")
                else:
                    danh_sach_mon[:] = [
                        mon for mon in danh_sach_mon if mon["ma_mon"] != ma_xoa
                    ]
                    if luu_thuc_don():
                        st.success(f"Đã xóa món {ma_xoa}.")
                        st.rerun()


def trang_ban_an():
    st.header("Quản lý bàn ăn")
    danh_sach_ban = st.session_state["danh_sach_ban"]
    if danh_sach_ban:
        st.dataframe(
            [
                {
                    "Mã bàn": ban["ma_ban"],
                    "Số bàn": ban["so_ban"],
                    "Trạng thái": ban["trang_thai"],
                }
                for ban in danh_sach_ban
            ],
            hide_index=True,
            width="stretch",
        )
    else:
        st.info("Chưa có bàn ăn.")

    with st.form("them_ban_web"):
        ma_ban = st.text_input("Mã bàn")
        so_ban = st.text_input("Số bàn")
        da_gui = st.form_submit_button("Thêm bàn")

    if da_gui:
        ma_ban = ma_ban.strip()
        so_ban = so_ban.strip()
        if not ma_ban or not so_ban:
            st.error("Mã bàn và số bàn không được để trống.")
        elif any(ban["ma_ban"].lower() == ma_ban.lower() for ban in danh_sach_ban):
            st.error("Mã bàn đã tồn tại.")
        else:
            danh_sach_ban.append(
                {"ma_ban": ma_ban, "so_ban": so_ban, "trang_thai": "Trống"}
            )
            if luu_danh_sach_ban():
                st.success(f"Đã thêm bàn {so_ban}.")
                st.rerun()


def trang_goi_mon():
    st.header("Gọi món")
    danh_sach_ban = st.session_state["danh_sach_ban"]
    danh_sach_mon = [
        mon
        for mon in st.session_state["danh_sach_mon"]
        if mon["trang_thai"] == "Còn bán"
    ]
    if not danh_sach_ban:
        st.info("Hãy thêm bàn trước khi gọi món.")
        return
    if not danh_sach_mon:
        st.info("Hiện không có món nào còn bán.")
        return

    ma_ban = st.selectbox(
        "Chọn bàn",
        [ban["ma_ban"] for ban in danh_sach_ban],
        format_func=lambda ma: next(
            f"{ban['so_ban']} ({ban['trang_thai']})"
            for ban in danh_sach_ban
            if ban["ma_ban"] == ma
        ),
    )
    with st.form("goi_mon_web"):
        ma_mon = st.selectbox(
            "Chọn món",
            [mon["ma_mon"] for mon in danh_sach_mon],
            format_func=lambda ma: next(
                f"{mon['ten_mon']} - {mon['don_gia']:,.0f} VNĐ"
                for mon in danh_sach_mon
                if mon["ma_mon"] == ma
            ),
        )
        so_luong = st.number_input("Số lượng", min_value=1, step=1)
        da_goi = st.form_submit_button("Thêm vào đơn")

    if da_goi:
        mon = next(mon for mon in danh_sach_mon if mon["ma_mon"] == ma_mon)
        ban = next(ban for ban in danh_sach_ban if ban["ma_ban"] == ma_ban)
        dong_goi_mon = {
            "ma_mon": mon["ma_mon"],
            "ten_mon": mon["ten_mon"],
            "don_gia": mon["don_gia"],
            "so_luong": int(so_luong),
            "thanh_tien": mon["don_gia"] * int(so_luong),
        }
        st.session_state["don_hang_dang_mo"].setdefault(ma_ban, []).append(dong_goi_mon)
        mon["so_luong_da_goi"] += int(so_luong)
        ban["trang_thai"] = "Đang phục vụ"
        if luu_thuc_don_va_ban() and luu_trang_thai_web():
            st.success(f"Đã gọi {so_luong} x {mon['ten_mon']} cho bàn {ban['so_ban']}.")
            st.rerun()

    don_hang = st.session_state["don_hang_dang_mo"].get(ma_ban, [])
    if don_hang:
        st.subheader("Đơn đang mở")
        st.dataframe(don_hang, hide_index=True, width="stretch")
        tong_tien = sum(dong["thanh_tien"] for dong in don_hang)
        st.metric("Tạm tính", f"{tong_tien:,.0f} VNĐ")


def trang_thanh_toan():
    st.header("Thanh toán")
    don_hang_dang_mo = st.session_state["don_hang_dang_mo"]
    cac_ma_ban = [ma for ma, don in don_hang_dang_mo.items() if don]
    if not cac_ma_ban:
        st.info("Không có đơn hàng nào cần thanh toán.")
        return

    ma_ban = st.selectbox("Chọn bàn cần thanh toán", cac_ma_ban)
    danh_sach_dong = don_hang_dang_mo[ma_ban]
    st.dataframe(danh_sach_dong, hide_index=True, width="stretch")
    tong_tien = sum(dong["thanh_tien"] for dong in danh_sach_dong)
    st.metric("Tổng cộng", f"{tong_tien:,.0f} VNĐ")

    if st.button("Xác nhận đã thanh toán", type="primary"):
        ban = next(
            (ban for ban in st.session_state["danh_sach_ban"] if ban["ma_ban"] == ma_ban),
            None,
        )
        if ban is None:
            st.error("Không tìm thấy bàn của đơn hàng.")
            return
        st.session_state["lich_su_hoa_don"].append(
            {
                "ma_ban": ma_ban,
                "so_ban": ban["so_ban"],
                "danh_sach_mon": [dict(dong) for dong in danh_sach_dong],
                "tong_tien": tong_tien,
            }
        )
        del don_hang_dang_mo[ma_ban]
        ban["trang_thai"] = "Trống"
        if luu_thuc_don_va_ban() and luu_trang_thai_web():
            st.success("Thanh toán thành công; bàn đã chuyển về trạng thái Trống.")
            st.rerun()


def trang_thong_ke():
    st.header("Thống kê")
    danh_sach_mon = st.session_state["danh_sach_mon"]
    ket_qua = thong_ke_tong_hop(
        danh_sach_mon,
        st.session_state["lich_su_hoa_don"],
    )
    cot1, cot2 = st.columns(2)
    cot1.metric("Tổng số món", ket_qua["tong_so_mon"])
    cot2.metric("Tổng doanh thu", f"{ket_qua['tong_doanh_thu']:,.0f} VNĐ")

    if ket_qua["mon_gia_cao_nhat"]:
        mon = ket_qua["mon_gia_cao_nhat"]
        st.write(f"**Món có giá cao nhất:** {mon['ten_mon']} ({mon['don_gia']:,.0f} VNĐ)")
    if ket_qua["mon_goi_nhieu_nhat"]:
        mon = ket_qua["mon_goi_nhieu_nhat"]
        st.write(f"**Món được gọi nhiều nhất:** {mon['ten_mon']} ({mon['so_luong_da_goi']} lượt)")
    else:
        st.write("**Món được gọi nhiều nhất:** Chưa có món nào được gọi.")

    doanh_thu_theo_loai = [
        {"Loại món": loai, "Doanh thu (VNĐ)": doanh_thu}
        for loai, doanh_thu in ket_qua["doanh_thu_theo_loai"].items()
    ]
    if doanh_thu_theo_loai:
        st.subheader("Doanh thu theo loại món")
        st.dataframe(doanh_thu_theo_loai, hide_index=True, width="stretch")
    else:
        st.info("Chưa có hóa đơn đã thanh toán.")


def main():
    st.set_page_config(page_title="Quản lý nhà hàng", page_icon="🍜", layout="wide")
    khoi_tao_du_lieu()
    st.title("Quản lý nhà hàng")
    st.sidebar.caption("Ứng dụng quản lý thực đơn, bàn và đơn hàng")
    trang = st.sidebar.radio(
        "Chức năng",
        ["Thực đơn", "Bàn ăn", "Gọi món", "Thanh toán", "Thống kê"],
    )

    if trang == "Thực đơn":
        trang_thuc_don()
    elif trang == "Bàn ăn":
        trang_ban_an()
    elif trang == "Gọi món":
        trang_goi_mon()
    elif trang == "Thanh toán":
        trang_thanh_toan()
    else:
        trang_thong_ke()

    st.sidebar.divider()
    st.sidebar.caption("Món ăn và bàn được lưu trong thư mục data.")


if __name__ == "__main__":
    main()
