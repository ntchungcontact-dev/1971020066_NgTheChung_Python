# Giải thích mã nguồn chương trình quản lý nhà hàng

Tài liệu này giải thích các lệnh trong từng tệp Python theo thứ tự xuất hiện. Dòng trống chỉ để chia đoạn; các dòng nằm trong cùng một câu lệnh nhiều dòng (chẳng hạn chuỗi `f` ghép bằng nhiều cặp dấu ngoặc) được giải thích cùng nhau.

## 1. `main.py` — điểm khởi chạy và điều phối chương trình

### Các lệnh `import`

- `from mon_an import them_mon, hien_thi_danh_sach, cap_nhat_mon, xoa_mon`: lấy các chức năng thêm, xem, sửa và xóa món ăn.
- `from ban_an import menu_quan_ly_ban`: lấy menu quản lý bàn.
- `from tim_kiem import menu_tim_kiem`: lấy chức năng tìm món.
- `from sap_xep import menu_sap_xep`: lấy chức năng sắp xếp món.
- `from goi_mon import goi_mon`: lấy chức năng ghi nhận món khách gọi.
- `from thanh_toan import thanh_toan`: lấy chức năng thanh toán hóa đơn.
- `from thong_ke import in_thong_ke`: lấy chức năng hiển thị thống kê.
- `from file_io import luu_du_lieu, doc_du_lieu`: lấy chức năng ghi và đọc dữ liệu từ tệp.

### Hàm `in_menu()`

- `def in_menu():`: định nghĩa hàm in menu chính.
- Các lệnh `print(...)` tiếp theo lần lượt in đường kẻ, tiêu đề “QUẢN LÝ NHÀ HÀNG”, 12 lựa chọn chức năng và lựa chọn `0` để thoát. Số lựa chọn hiển thị tương ứng với các nhánh xử lý trong `main()`.

### Hàm `main()`

- `def main():`: định nghĩa luồng điều khiển chính.
- `danh_sach_mon = []`: tạo danh sách món ăn trong bộ nhớ.
- `danh_sach_ban = []`: tạo danh sách bàn ăn trong bộ nhớ.
- `don_hang_dang_mo = {}`: tạo từ điển lưu các dòng món đang gọi, tra cứu theo mã bàn.
- `lich_su_hoa_don = []`: tạo danh sách hóa đơn đã thanh toán để dùng cho thống kê.
- `while True:`: lặp menu liên tục cho đến khi người dùng chọn thoát.
- `in_menu()`: hiển thị menu ở đầu mỗi lượt.
- `lua_chon = input(...).strip()`: nhận lựa chọn từ bàn phím và bỏ khoảng trắng ở hai đầu.
- `try:`: bắt đầu vùng xử lý để nếu thao tác bên dưới phát sinh lỗi thì chương trình báo lỗi thay vì dừng đột ngột.
- `if lua_chon == "1":` rồi `them_mon(danh_sach_mon)`: thêm món vào danh sách hiện có.
- `elif lua_chon == "2":` rồi `hien_thi_danh_sach(danh_sach_mon)`: in danh sách món.
- `elif lua_chon == "3":` rồi `menu_tim_kiem(danh_sach_mon)`: mở chức năng tìm kiếm.
- `elif lua_chon == "4":` rồi `menu_sap_xep(danh_sach_mon)`: mở chức năng sắp xếp.
- `elif lua_chon == "5":` rồi `goi_mon(...)`: ghi món gọi, cập nhật số lượng đã gọi và trạng thái bàn.
- `elif lua_chon == "6":` rồi `thanh_toan(...)`: thanh toán đơn đang mở và ghi hóa đơn vào lịch sử.
- `elif lua_chon == "7":` rồi `in_thong_ke(...)`: thống kê thực đơn và các hóa đơn đã thanh toán.
- `elif lua_chon == "8":` rồi `luu_du_lieu(...)`: lưu danh sách món và bàn ra tệp.
- `elif lua_chon == "9":`: bắt đầu nhánh đọc dữ liệu.
- `mon_doc_duoc, ban_doc_duoc = doc_du_lieu()`: lấy hai danh sách món và bàn đọc từ tệp.
- `if mon_doc_duoc:` và phép gán `danh_sach_mon = mon_doc_duoc`: chỉ thay danh sách món trong bộ nhớ nếu tệp đọc được có dữ liệu.
- `if ban_doc_duoc:` và phép gán `danh_sach_ban = ban_doc_duoc`: chỉ thay danh sách bàn trong bộ nhớ nếu có dữ liệu.
- `elif lua_chon == "10":` rồi `cap_nhat_mon(...)`: cập nhật thông tin món.
- `elif lua_chon == "11":` rồi `xoa_mon(...)`: xóa món.
- `elif lua_chon == "12":` rồi `menu_quan_ly_ban(...)`: mở menu quản lý bàn.
- `elif lua_chon == "0":`: xử lý yêu cầu thoát.
- `print(...)`: thông báo tạm biệt.
- `break`: kết thúc vòng lặp menu.
- `else:` và `print(...)`: báo lựa chọn không thuộc các chức năng có sẵn.
- `except Exception as loi:`: nhận lỗi phát sinh trong vùng `try` và giữ thông tin lỗi trong biến `loi`.
- `print(f"...{loi}")`: hiển thị nội dung lỗi cho người dùng.
- `input("\nNhấn Enter để tiếp tục...")`: tạm dừng trước khi quay lại menu; lệnh này chạy sau mỗi lượt không thoát.
- `if __name__ == "__main__":`: chỉ khởi chạy luồng chính khi tệp được chạy trực tiếp, không chạy khi được tệp khác import.
- `main()`: gọi hàm điều khiển chương trình.

## 2. `mon_an.py` — quản lý món ăn

- Khối `from validate import (...)`: dùng các hàm nhập số thực, nhập chuỗi không rỗng, kiểm tra mã trùng và tìm vị trí theo mã.
- `CAC_TRANG_THAI_MON = ("Còn bán", "Hết hàng")`: quy định hai trạng thái hợp lệ của món.

### `them_mon(danh_sach_mon)`

- `def them_mon(...)`: định nghĩa chức năng thêm món vào danh sách truyền vào.
- `print(...)`: in tiêu đề chức năng.
- `while True:`: yêu cầu nhập mã đến khi mã hợp lệ.
- `nhap_chuoi_khong_rong(...)`: nhận mã món không được để trống.
- `kiem_tra_ma_trung(...)`: kiểm tra mã vừa nhập đã tồn tại trong danh sách chưa.
- `if` mã đã tồn tại, `print(...)` báo lỗi; `continue` quay lại nhập mã mới.
- `break`: thoát vòng nhập mã khi mã không trùng.
- Ba lệnh gán `ten_mon`, `loai_mon`, `don_gia`: lần lượt lấy tên, loại và đơn giá; đơn giá được kiểm tra là số dương bởi `nhap_so_thuc`.
- Vòng `while True` nhập `trang_thai`: tiếp tục hỏi đến khi giá trị thuộc `CAC_TRANG_THAI_MON`.
- `if trang_thai in CAC_TRANG_THAI_MON`: chấp nhận trạng thái và `break` khỏi vòng lặp.
- `print(...)` trong trường hợp còn lại: báo trạng thái không hợp lệ.
- `mon_moi = {...}`: tạo từ điển chứa mã, tên, loại, giá, trạng thái và số lượng đã gọi ban đầu bằng `0`.
- `danh_sach_mon.append(mon_moi)`: thêm món mới vào danh sách.
- `print(...)`: xác nhận thêm món thành công.

### `hien_thi_1_mon(mon)`

- `def hien_thi_1_mon(mon):`: định nghĩa hàm in một món.
- Lệnh `print(...)` nhiều dòng ghép các f-string: in mã, tên, loại, đơn giá, trạng thái và số lượng đã gọi; các phần `<8`, `<20`... căn lề cột, `,.0f` hiển thị tiền có dấu phân cách hàng nghìn và không có chữ số thập phân.

### `hien_thi_danh_sach(danh_sach_mon)`

- `print(...)`: in tiêu đề danh sách.
- `if len(danh_sach_mon) == 0:`: kiểm tra thực đơn rỗng.
- `print(...)` và `return`: báo danh sách trống rồi kết thúc hàm sớm.
- `tieu_de = (...)`: dựng hàng tiêu đề các cột tương ứng với dữ liệu món.
- `print(tieu_de)`: in hàng tiêu đề.
- `print("-" * len(tieu_de))`: in đường phân cách có độ dài bằng tiêu đề.
- `for mon in danh_sach_mon:`: duyệt từng món.
- `hien_thi_1_mon(mon)`: in từng món theo cùng định dạng.
- `print(...)`: in tổng số món.

### `cap_nhat_mon(danh_sach_mon)`

- `print(...)`: in tiêu đề cập nhật.
- `nhap_chuoi_khong_rong(...)`: nhận mã món cần sửa.
- `tim_vi_tri_theo_ma(...)`: tìm vị trí món trong danh sách.
- `if vi_tri == -1:`: nhận biết không tìm thấy mã.
- `print(...)` và `return`: báo lỗi và dừng cập nhật nếu không có món tương ứng.
- `mon = danh_sach_mon[vi_tri]`: lấy từ điển món cần sửa.
- `print(...)` và `hien_thi_1_mon(mon)`: cho xem thông tin hiện tại.
- `print(...)`: hướng dẫn nhấn Enter để giữ nguyên dữ liệu.
- `ten_moi = input(...).strip()` và khối `if ten_moi != ""`: chỉ thay tên nếu có nhập giá trị mới.
- `loai_moi = input(...).strip()` và khối `if loai_moi != ""`: chỉ thay loại nếu có nhập giá trị mới.
- `don_gia_moi = input(...).strip()` và `if don_gia_moi != ""`: chỉ xử lý giá khi người dùng có nhập.
- `try:` cùng `gia_tri = float(don_gia_moi)`: chuyển giá nhập thành số thực.
- `if gia_tri <= 0:`: từ chối giá không dương và giữ giá cũ.
- `else` và `mon["don_gia"] = gia_tri`: lưu giá mới hợp lệ.
- `except ValueError:`: xử lý trường hợp nội dung nhập không chuyển được thành số.
- `trang_thai_moi = input(...).strip()` và `if trang_thai_moi != ""`: chỉ sửa trạng thái nếu có nhập.
- `if trang_thai_moi in CAC_TRANG_THAI_MON:`: chỉ nhận một trong hai trạng thái hợp lệ.
- `mon["trang_thai"] = trang_thai_moi`: lưu trạng thái hợp lệ.
- Các lệnh `print(...)` trong nhánh không hợp lệ: báo lỗi và giữ nguyên giá trị cũ.
- `print(">> Cập nhật thành công!")`: thông báo hoàn thành thao tác.

### `xoa_mon(danh_sach_mon)`

- `print(...)`: in tiêu đề xóa món.
- `nhap_chuoi_khong_rong(...)`: nhận mã món cần xóa.
- `tim_vi_tri_theo_ma(...)`: tìm món theo mã.
- `if vi_tri == -1:` với `print(...)` và `return`: báo không tìm thấy món rồi kết thúc.
- `mon = danh_sach_mon[vi_tri]`: lấy món để hiện tên trong câu hỏi xác nhận.
- `input(...).strip().lower()`: hỏi xác nhận và chuyển câu trả lời về chữ thường.
- `if xac_nhan != "y":`: nếu không trả lời `y`, hủy thao tác.
- `print(...)` và `return`: thông báo hủy rồi kết thúc hàm.
- `danh_sach_mon.pop(vi_tri)`: xóa món khỏi danh sách.
- `print(...)`: thông báo xóa thành công.

## 3. `ban_an.py` — quản lý bàn ăn

- `from validate import ...`: dùng nhập chuỗi không rỗng, kiểm tra mã trùng và tìm vị trí bàn theo mã.
- `CAC_TRANG_THAI_BAN = ("Trống", "Đang phục vụ")`: liệt kê các trạng thái bàn được chương trình sử dụng.

### `them_ban(danh_sach_ban)`

- `print(...)`: in tiêu đề thêm bàn.
- `while True:` cùng `nhap_chuoi_khong_rong(...)`: hỏi mã bàn đến khi có mã không rỗng.
- `kiem_tra_ma_trung(..., "ma_ban", ma_ban)`: kiểm tra mã bàn bị trùng.
- Nếu trùng, `print(...)` báo lỗi và `continue` yêu cầu nhập lại; nếu không trùng, `break` khỏi vòng lặp.
- `so_ban = nhap_chuoi_khong_rong(...)`: nhận số/nhãn bàn dưới dạng chuỗi.
- `ban_moi = {...}`: tạo thông tin bàn với trạng thái ban đầu `"Trống"`.
- `danh_sach_ban.append(ban_moi)`: thêm bàn vào danh sách.
- `print(...)`: xác nhận bàn đã được thêm.

### `hien_thi_1_ban(ban)`

- `print(...)`: in mã bàn, số bàn và trạng thái theo ba cột căn lề.

### `hien_thi_danh_sach_ban(danh_sach_ban)`

- `print(...)`: in tiêu đề danh sách bàn.
- `if len(danh_sach_ban) == 0:` kiểm tra danh sách rỗng; `print(...)` báo trống và `return` kết thúc hàm.
- `tieu_de = ...`: tạo tên ba cột.
- `print(tieu_de)` và `print("-" * len(tieu_de))`: in tiêu đề và đường phân cách.
- `for ban in danh_sach_ban:` duyệt các bàn; `hien_thi_1_ban(ban)` in từng bàn.
- `print(...)`: in tổng số bàn.

### `tim_ban_theo_ma(danh_sach_ban, ma_ban)`

- `tim_vi_tri_theo_ma(..., "ma_ban", ma_ban)`: tìm vị trí bàn theo trường mã.
- `if vi_tri == -1:` nghĩa là không tìm thấy; `return None` báo kết quả rỗng cho bên gọi.
- `return danh_sach_ban[vi_tri]`: trả về từ điển bàn tìm được.

### `menu_quan_ly_ban(danh_sach_ban)`

- `print(...)` ba lệnh đầu: in tiêu đề và hai lựa chọn thêm bàn/hiển thị bàn.
- `input(...).strip()`: nhận lựa chọn.
- Nhánh `"1"` gọi `them_ban(...)`; nhánh `"2"` gọi `hien_thi_danh_sach_ban(...)`.
- `else` cùng `print(...)`: báo lựa chọn không hợp lệ.

## 4. `validate.py` — kiểm tra dữ liệu nhập và tìm kiếm dùng chung

### `nhap_so_thuc(thong_bao, cho_phep_bang_khong=False)`

- `while True:` lặp cho đến khi nhận được số hợp lệ.
- `input(thong_bao).strip()`: nhận dữ liệu và bỏ khoảng trắng hai đầu.
- `try` / `float(chuoi_nhap)`: thử đổi dữ liệu thành số thực.
- `except ValueError:` báo nhập sai kiểu số rồi `continue` hỏi lại.
- `if cho_phep_bang_khong:` chọn quy tắc cho phép giá trị 0.
- `if gia_tri < 0:` báo lỗi và hỏi lại nếu giá trị âm trong chế độ cho phép 0.
- Nhánh `else` kiểm tra chế độ mặc định; `if gia_tri <= 0:` báo lỗi nếu số không dương.
- `return gia_tri`: trả về số sau khi vượt qua kiểm tra.

### `nhap_so_nguyen_duong(thong_bao)`

- `while True:` tiếp tục hỏi đến khi hợp lệ.
- `input(...).strip()` lấy chuỗi nhập.
- `int(chuoi_nhap)` thử chuyển thành số nguyên.
- `except ValueError:` báo lỗi và `continue` hỏi lại nếu không phải số nguyên.
- `if gia_tri <= 0:` báo lỗi và hỏi lại nếu số không dương.
- `return gia_tri`: trả về số nguyên dương.

### `nhap_chuoi_khong_rong(thong_bao)`

- `while True:` lặp quá trình nhận chuỗi.
- `input(...).strip()`: nhận chuỗi và bỏ khoảng trắng ở hai đầu.
- `if chuoi_nhap == "":`: phát hiện chuỗi rỗng.
- `print(...)` và `continue`: báo lỗi rồi hỏi lại.
- `return chuoi_nhap`: trả về chuỗi có nội dung.

### `kiem_tra_ma_trung(danh_sach, ten_khoa_ma, ma_can_kiem_tra, ma_dang_sua=None)`

- `for phan_tu in danh_sach:` duyệt từng phần tử.
- `if ...`: kiểm tra giá trị ở trường `ten_khoa_ma` có trùng mã cần kiểm tra hay không; nếu đang sửa một phần tử, mã bằng `ma_dang_sua` được bỏ qua.
- `return True`: báo có mã trùng ngay khi tìm thấy.
- `return False`: báo không trùng sau khi duyệt hết danh sách.

### `tim_vi_tri_theo_ma(danh_sach, ten_khoa_ma, ma_can_tim)`

- `for vi_tri, phan_tu in enumerate(danh_sach):` duyệt danh sách đồng thời lấy chỉ số.
- `if phan_tu[ten_khoa_ma] == ma_can_tim:` so sánh mã của phần tử với mã cần tìm.
- `return vi_tri`: trả về chỉ số khi tìm thấy.
- `return -1`: dùng `-1` làm dấu hiệu không tìm thấy.

## 5. `goi_mon.py` — tạo đơn đang mở cho một bàn

- Dòng import từ `validate`: dùng nhập số lượng nguyên dương, chuỗi không rỗng và tìm mã món.
- `from ban_an import tim_ban_theo_ma`: dùng tra cứu bàn theo mã.

### `goi_mon(danh_sach_mon, danh_sach_ban, don_hang_dang_mo)`

- `print(...)`: in tiêu đề gọi món.
- `if len(danh_sach_ban) == 0:` kiểm tra đã có bàn chưa; nếu chưa, thông báo và `return`.
- `ma_ban = nhap_chuoi_khong_rong(...)`: nhận mã bàn.
- `ban = tim_ban_theo_ma(...)`: tìm bàn tương ứng.
- `if ban is None:` báo bàn không tồn tại và kết thúc.
- `ma_mon = nhap_chuoi_khong_rong(...)`: nhận mã món.
- `tim_vi_tri_theo_ma(...)`: tìm vị trí món theo trường `ma_mon`.
- `if vi_tri_mon == -1:` báo món không tồn tại và kết thúc.
- `mon = danh_sach_mon[vi_tri_mon]`: lấy thông tin món.
- `if mon["trang_thai"] == "Hết hàng":`: không cho gọi món đang hết hàng; in lỗi và kết thúc.
- `so_luong = nhap_so_nguyen_duong(...)`: nhận số lượng lớn hơn 0.
- `thanh_tien = mon["don_gia"] * so_luong`: tính tiền cho dòng gọi món.
- `dong_goi_mon = {...}`: tạo bản ghi gồm mã/tên món, đơn giá, số lượng và thành tiền.
- `if ma_ban not in don_hang_dang_mo:`: nếu bàn chưa có đơn thì khởi tạo danh sách trống cho bàn.
- `don_hang_dang_mo[ma_ban].append(dong_goi_mon)`: thêm dòng gọi món vào đơn của bàn.
- `mon["so_luong_da_goi"] += so_luong`: cộng số lượng vừa gọi vào thống kê của món.
- `ban["trang_thai"] = "Đang phục vụ"`: đánh dấu bàn đang phục vụ.
- `print(...)` nhiều dòng: xác nhận số lượng, tên món, số bàn và tiền dòng gọi.

### `hien_thi_don_hang_cua_ban(don_hang_dang_mo, ma_ban)`

- `don_hang_dang_mo.get(ma_ban, [])`: lấy các dòng của bàn; nếu chưa có thì dùng danh sách rỗng.
- `if len(danh_sach_dong) == 0:` in thông báo chưa gọi món rồi kết thúc bằng `return`.
- `tieu_de = ...`: tạo tiêu đề các cột món, đơn giá, số lượng và thành tiền.
- Hai lệnh `print(...)`: in tiêu đề và đường phân cách.
- `for dong in danh_sach_dong:` duyệt từng dòng món.
- `print(...)` nhiều dòng: in tên, giá, số lượng và thành tiền theo cột.

## 6. `thanh_toan.py` — tính tiền và kết thúc đơn

- `from validate import nhap_chuoi_khong_rong`: dùng nhận mã bàn.
- `from ban_an import tim_ban_theo_ma`: dùng tìm bàn.
- `from goi_mon import hien_thi_don_hang_cua_ban`: dùng in chi tiết món trong đơn.

### `tinh_tong_hoa_don(don_hang_dang_mo, ma_ban)`

- `don_hang_dang_mo.get(ma_ban, [])`: lấy các dòng gọi món của bàn.
- `sum(...)`: cộng trường `thanh_tien` của tất cả dòng và trả về tổng.

### `thanh_toan(danh_sach_ban, don_hang_dang_mo, lich_su_hoa_don)`

- `print(...)`: in tiêu đề thanh toán.
- `ma_ban = nhap_chuoi_khong_rong(...)`: hỏi mã bàn cần thanh toán.
- `ban = tim_ban_theo_ma(...)`: lấy thông tin bàn.
- `if ban is None:` báo lỗi và `return` nếu bàn không tồn tại.
- `danh_sach_dong = don_hang_dang_mo.get(ma_ban, [])`: lấy đơn hiện tại của bàn.
- `if len(danh_sach_dong) == 0:` báo chưa có món để thanh toán rồi dừng.
- `print(...)`: in số bàn và mã bàn trên hóa đơn.
- `hien_thi_don_hang_cua_ban(...)`: hiển thị chi tiết từng món.
- `tong_tien = tinh_tong_hoa_don(...)`: tính tổng hóa đơn.
- `print("-" * 40)`: in đường phân cách.
- `print(...)`: in tổng tiền, định dạng phân cách hàng nghìn và đơn vị VNĐ.
- `lich_su_hoa_don.append({...})`: lưu mã bàn, số bàn, các dòng món và tổng tiền vào lịch sử.
- `del don_hang_dang_mo[ma_ban]`: xóa đơn đang mở của bàn vì đã thanh toán.
- `ban["trang_thai"] = "Trống"`: chuyển bàn về trạng thái trống.
- `print(...)`: xác nhận thanh toán và trả bàn.

## 7. `thong_ke.py` — tổng hợp số liệu

### `thong_ke_tong_hop(danh_sach_mon, lich_su_hoa_don)`

- `tong_so_mon = len(danh_sach_mon)`: đếm số món.
- `mon_gia_cao_nhat = None`: khởi tạo kết quả là chưa có món.
- `if tong_so_mon > 0:` chỉ tìm món đắt nhất khi danh sách không rỗng.
- `max(..., key=lambda m: m["don_gia"])`: chọn món có đơn giá lớn nhất.
- `mon_goi_nhieu_nhat = None`: khởi tạo kết quả món được gọi nhiều nhất.
- `if tong_so_mon > 0:` chỉ tìm món khi có thực đơn.
- `max(..., key=lambda m: m["so_luong_da_goi"])`: chọn món có số lượng đã gọi lớn nhất.
- `if ... == 0:` nếu món đứng đầu chưa được gọi thì đặt kết quả lại thành `None`.
- `tong_doanh_thu = sum(...)`: cộng tổng tiền của mọi hóa đơn trong lịch sử.
- `doanh_thu_theo_loai = {}`: tạo từ điển doanh thu theo loại món.
- Vòng `for hoa_don ...` duyệt các hóa đơn đã thanh toán.
- Vòng `for dong ...` bên trong duyệt từng dòng món của một hóa đơn.
- `loai = _tim_loai_mon(...)`: xác định loại của món dựa trên mã món.
- `doanh_thu_theo_loai[loai] = ...`: cộng thành tiền vào tổng doanh thu của loại đó; `.get(loai, 0)` dùng 0 nếu loại chưa có trong từ điển.
- `return {...}`: trả về từ điển chứa số món, món đắt nhất, món gọi nhiều nhất, tổng doanh thu và doanh thu theo loại.

### `_tim_loai_mon(danh_sach_mon, ma_mon)`

- `for mon in danh_sach_mon:` duyệt danh sách món.
- `if mon["ma_mon"] == ma_mon:` so sánh mã món.
- `return mon["loai_mon"]`: trả về loại khi tìm thấy.
- `return "Không xác định"`: trả về nhãn dự phòng nếu mã không còn trong thực đơn.

### `in_thong_ke(danh_sach_mon, lich_su_hoa_don)`

- `print(...)`: in tiêu đề thống kê.
- `if len(danh_sach_mon) == 0:` kiểm tra thực đơn rỗng.
- `print(...)` và `return`: báo chưa có dữ liệu và kết thúc nếu rỗng.
- `ket_qua = thong_ke_tong_hop(...)`: lấy các số liệu đã tổng hợp.
- `print(...)`: in tổng số món.
- `if ket_qua["mon_gia_cao_nhat"]:` chỉ in món đắt nhất nếu có kết quả.
- `mon = ...` lấy món đắt nhất; `print(...)` in tên và giá.
- `if ket_qua["mon_goi_nhieu_nhat"]:` kiểm tra có món đã được gọi.
- `mon = ...` lấy món gọi nhiều nhất; `print(...)` in tên và số lượng đã gọi.
- `else` và `print(...)`: thông báo chưa có món nào được gọi.
- `print(...)`: in tổng doanh thu.
- `print(...)`: in nhãn doanh thu theo loại.
- `if len(...) == 0:` kiểm tra chưa có doanh thu theo loại.
- `print(...)`: thông báo chưa có hóa đơn đã thanh toán.
- `else` cùng `for loai, doanh_thu in ...items():`: duyệt từng loại và doanh thu tương ứng.
- `print(...)`: in doanh thu mỗi loại theo định dạng tiền.

## 8. `tim_kiem.py` — tìm món theo mã, tên hoặc loại

### `tim_theo_ma_mon(danh_sach_mon, ma_mon)`

- `ma_mon.strip().lower()`: chuẩn hóa mã tìm kiếm bằng cách bỏ khoảng trắng và chuyển chữ thường.
- List comprehension `[...]`: trả về danh sách món có mã sau khi chuyển chữ thường khớp chính xác.

### `tim_theo_ten_mon(danh_sach_mon, ten)`

- `ten.strip().lower()`: chuẩn hóa từ khóa tên.
- List comprehension: trả về các món có tên chứa từ khóa, không phân biệt chữ hoa/thường.

### `tim_theo_loai_mon(danh_sach_mon, loai)`

- `loai.strip().lower()`: chuẩn hóa từ khóa loại.
- List comprehension: trả về món có loại khớp chính xác, không phân biệt chữ hoa/thường.

### `menu_tim_kiem(danh_sach_mon)`

- `from mon_an import hien_thi_1_mon`: import hàm in món bên trong hàm để dùng khi có kết quả.
- Các lệnh `print(...)` đầu hàm: in tiêu đề và ba cách tìm kiếm.
- `lua_chon = input(...).strip()`: nhận cách tìm.
- `ket_qua = []`: khởi tạo danh sách kết quả.
- Nhánh `"1"` nhận mã món và gọi `tim_theo_ma_mon(...)`.
- Nhánh `"2"` nhận tên hoặc một phần tên và gọi `tim_theo_ten_mon(...)`.
- Nhánh `"3"` nhận loại món và gọi `tim_theo_loai_mon(...)`.
- `else` cùng `print(...)` và `return`: báo lựa chọn sai và kết thúc.
- `if len(ket_qua) == 0:` báo không tìm thấy khi danh sách rỗng.
- `else`: thông báo số món tìm được.
- `for mon in ket_qua:` duyệt kết quả.
- `hien_thi_1_mon(mon)`: in từng món tìm thấy.

## 9. `sap_xep.py` — sắp xếp và hiển thị thực đơn

### `sap_xep_theo_ten(danh_sach_mon, tang_dan=True)`

- `sorted(...)`: tạo danh sách đã sắp xếp theo tên chuyển thành chữ thường.
- `reverse=not tang_dan`: đảo thứ tự khi cần sắp xếp giảm dần; danh sách ban đầu không bị sắp xếp tại chỗ.

### `sap_xep_theo_don_gia(danh_sach_mon, tang_dan=True)`

- `sorted(...)`: tạo danh sách đã sắp xếp theo trường đơn giá.
- `reverse=not tang_dan`: chọn tăng/giảm theo tham số; danh sách gốc không bị thay đổi.

### `menu_sap_xep(danh_sach_mon)`

- `from mon_an import hien_thi_1_mon`: lấy hàm dùng để in từng món.
- `if len(danh_sach_mon) == 0:` kiểm tra thực đơn rỗng.
- `print(...)` và `return`: báo không có gì để sắp xếp rồi kết thúc.
- Các lệnh `print(...)`: in tiêu đề và lựa chọn sắp xếp theo tên hoặc giá.
- `lua_chon = input(...).strip()`: nhận tiêu chí.
- `thu_tu = input(...).strip().lower()`: nhận lựa chọn tăng/giảm; chữ thường hóa giúp nhận `Y`/`N` nhất quán.
- `tang_dan = thu_tu != "n"`: mọi câu trả lời ngoài `n` được xem là tăng dần theo mặc định.
- Nhánh `"1"` gọi `sap_xep_theo_ten(...)` và gán kết quả vào `ket_qua`.
- Nhánh `"2"` gọi `sap_xep_theo_don_gia(...)`.
- `else` cùng `print(...)` và `return`: báo tiêu chí không hợp lệ.
- `print(...)`: cho biết kết quả tăng hay giảm.
- `tieu_de = (...)`: tạo tiêu đề các cột món.
- Hai lệnh `print(...)`: in tiêu đề và đường phân cách.
- `for mon in ket_qua:` duyệt danh sách đã sắp xếp.
- `hien_thi_1_mon(mon)`: in từng dòng kết quả.

## 10. `file_io.py` — lưu và đọc dữ liệu

- `import os`: dùng các thao tác hệ thống tệp và thư mục.
- `TEN_FILE_MON_MAC_DINH = "data/mon_an.txt"`: đường dẫn mặc định khi lưu/đọc món.
- `TEN_FILE_BAN_MAC_DINH = "data/ban_an.txt"`: đường dẫn mặc định khi lưu/đọc bàn.
- `DAU_PHAN_CACH = "|"`: dùng dấu `|` ngăn cách các trường trên mỗi dòng.
- `CAC_TRUONG_MON = [...]`: quy định thứ tự sáu trường món trong tệp.
- `CAC_TRUONG_MON_SO_THUC = {"don_gia"}`: các trường món cần chuyển thành số thực khi đọc.
- `CAC_TRUONG_MON_SO_NGUYEN = {"so_luong_da_goi"}`: các trường món cần chuyển thành số nguyên khi đọc.
- `CAC_TRUONG_BAN = [...]`: quy định thứ tự ba trường bàn trong tệp.

### `_tao_thu_muc_neu_can(ten_file)`

- `os.path.dirname(ten_file)`: lấy phần thư mục trong đường dẫn.
- `if thu_muc and not os.path.exists(thu_muc):`: chỉ tạo khi có tên thư mục và thư mục chưa tồn tại.
- `os.makedirs(thu_muc)`: tạo thư mục cần thiết.

### `luu_mon_an(danh_sach_mon, ten_file=TEN_FILE_MON_MAC_DINH)`

- `try:` bắt lỗi thao tác tệp.
- `_tao_thu_muc_neu_can(ten_file)`: đảm bảo thư mục chứa tệp đã có.
- `with open(..., "w", encoding="utf-8") as file:` mở tệp để ghi mới bằng UTF-8; nội dung cũ bị thay thế.
- `for mon in danh_sach_mon:` duyệt từng món.
- `DAU_PHAN_CACH.join(...)`: lấy các trường theo thứ tự `CAC_TRUONG_MON`, đổi thành chuỗi rồi nối bằng `|`.
- `file.write(dong + "\n")`: ghi mỗi món thành một dòng.
- `print(...)`: báo số món đã ghi và tên tệp.
- `return True`: báo ghi thành công.
- `except (IOError, OSError) as loi:` bắt lỗi đọc/ghi hệ thống tệp.
- `print(...)`: báo tệp và nội dung lỗi.
- `return False`: báo ghi thất bại.

### `doc_mon_an(ten_file=TEN_FILE_MON_MAC_DINH)`

- `if not os.path.exists(ten_file):`: kiểm tra tệp có tồn tại.
- `print(...)` và `return []`: báo không có tệp rồi trả về danh sách rỗng.
- `danh_sach_mon = []`: tạo danh sách kết quả đọc.
- `try:` bắt lỗi thao tác tệp.
- `with open(..., "r", encoding="utf-8") as file:` mở tệp để đọc UTF-8.
- `for so_dong, dong in enumerate(file, start=1):`: duyệt từng dòng và đánh số từ 1 để báo lỗi dễ tìm.
- `dong = dong.strip()`: bỏ ký tự xuống dòng và khoảng trắng hai đầu.
- `if dong == "": continue`: bỏ qua dòng trống.
- `cac_gia_tri = dong.split(DAU_PHAN_CACH)`: tách các trường theo dấu `|`.
- `if len(cac_gia_tri) != len(CAC_TRUONG_MON):`: kiểm tra dòng có đúng số trường.
- `print(...)` và `continue`: cảnh báo, bỏ qua dòng sai định dạng.
- `try:` bắt lỗi chuyển kiểu dữ liệu trên từng dòng.
- `mon = {}`: tạo từ điển món.
- `for ten_truong, gia_tri in zip(...):`: ghép từng tên trường với giá trị cùng vị trí.
- Nếu trường là `don_gia`, `float(gia_tri)` chuyển thành số thực.
- Nếu trường là `so_luong_da_goi`, `int(gia_tri)` chuyển thành số nguyên.
- `else` và `mon[ten_truong] = gia_tri`: các trường còn lại giữ dạng chuỗi.
- `danh_sach_mon.append(mon)`: thêm món hợp lệ vào kết quả.
- `except ValueError:` bắt giá trị giá/ số lượng không chuyển được.
- `print(...)` và `continue`: cảnh báo và bỏ qua dòng có dữ liệu số sai.
- `print(...)`: báo số món đọc được.
- `return danh_sach_mon`: trả danh sách đã đọc.
- `except (IOError, OSError) as loi:` bắt lỗi đọc tệp.
- `print(...)` và `return []`: báo lỗi, trả danh sách rỗng.

### `luu_ban_an(danh_sach_ban, ten_file=TEN_FILE_BAN_MAC_DINH)`

- Hàm dùng cùng cách ghi tệp như `luu_mon_an`, nhưng duyệt danh sách bàn và lấy trường theo `CAC_TRUONG_BAN`.
- `_tao_thu_muc_neu_can(...)` tạo thư mục nếu cần.
- `open(..., "w", encoding="utf-8")` mở tệp bàn để ghi mới.
- `for ban in danh_sach_ban:` duyệt từng bàn.
- `join(...)` ghép mã bàn, số bàn, trạng thái theo dấu `|`; `file.write(...)` ghi từng bàn thành một dòng.
- `print(...)` và `return True`: thông báo và trả kết quả thành công.
- `except (IOError, OSError)`: báo lỗi ghi và trả `False`.

### `doc_ban_an(ten_file=TEN_FILE_BAN_MAC_DINH)`

- Kiểm tra tệp tồn tại; nếu không có thì báo lỗi và trả danh sách rỗng.
- `danh_sach_ban = []`: tạo nơi chứa các bàn đọc được.
- `try` và `with open(..., "r", encoding="utf-8")`: mở tệp để đọc.
- `enumerate(file, start=1)`: duyệt và đánh số từng dòng.
- `strip()` bỏ khoảng trắng; dòng trống được bỏ qua bằng `continue`.
- `split(DAU_PHAN_CACH)`: tách các giá trị.
- Kiểm tra số giá trị bằng số trường ở `CAC_TRUONG_BAN`; nếu sai thì cảnh báo và bỏ qua.
- `dict(zip(CAC_TRUONG_BAN, cac_gia_tri))`: ghép tên trường với giá trị để tạo từ điển bàn.
- `danh_sach_ban.append(ban)`: thêm bàn vào kết quả.
- Sau vòng lặp, `print(...)` báo số bàn và `return danh_sach_ban` trả kết quả.
- `except (IOError, OSError)`: báo lỗi đọc và trả danh sách rỗng.

### `luu_du_lieu(danh_sach_mon, danh_sach_ban)`

- `ket_qua_mon = luu_mon_an(...)`: lưu danh sách món.
- `ket_qua_ban = luu_ban_an(...)`: lưu danh sách bàn.
- `return ket_qua_mon and ket_qua_ban`: chỉ trả `True` khi cả hai thao tác đều thành công.

### `doc_du_lieu()`

- `danh_sach_mon = doc_mon_an()`: đọc món từ tệp mặc định.
- `danh_sach_ban = doc_ban_an()`: đọc bàn từ tệp mặc định.
- `return danh_sach_mon, danh_sach_ban`: trả về hai danh sách cho `main.py`.

## 11. Các tệp dữ liệu `.txt`

- `ban_an.txt`: mỗi dòng có cấu trúc `mã bàn|số bàn|trạng thái`; ví dụ `B001|1|Trống` là bàn mã B001, số 1, đang trống.
- `mon_an.txt`: mỗi dòng có cấu trúc `mã món|tên món|loại món|đơn giá|trạng thái|số lượng đã gọi`. Đơn giá được đọc thành số thực, số lượng đã gọi thành số nguyên.
- Các tệp mẫu đang nằm ở thư mục gốc. Riêng `file_io.py` mặc định đọc/ghi trong thư mục `data`, vì vậy đường dẫn thực tế phải khớp vị trí tệp nếu chạy chương trình theo mặc định.

## 12. Chạy ứng dụng trên web bằng Streamlit

- `web_app.py` cung cấp giao diện web cho thực đơn, bàn ăn, gọi món, thanh toán và thống kê; chương trình dòng lệnh `main.py` vẫn dùng được như trước.
- Cài các thư viện được khai báo trong `requirements.txt` bằng `python -m pip install -r requirements.txt`.
- Chạy trên máy tính bằng `python -m streamlit run web_app.py`.
- Để deploy, đẩy `web_app.py`, `requirements.txt`, các tệp `.py` hiện có và thư mục `data` lên GitHub. Trên Streamlit Community Cloud, chọn repo/nhánh rồi đặt `web_app.py` làm Main file path.
- Ứng dụng lưu thực đơn và bàn vào các tệp `.txt` trong `data`; đơn hàng đang mở và lịch sử hóa đơn của giao diện web nằm trong `data/trang_thai_web.json`.
- Bản deploy mẫu không đảm bảo dữ liệu ghi vào ổ đĩa được giữ sau khi ứng dụng khởi động lại, và chưa có đăng nhập/phân quyền. Dùng thử hoặc trình diễn thì phù hợp; nếu dùng thực tế, hãy chuyển dữ liệu sang cơ sở dữ liệu có lưu trữ bền vững và bổ sung xác thực.
