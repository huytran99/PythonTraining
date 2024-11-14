# bài 1: Viết 1 hàm cap_nhat_gia_tri(danh_sach) nhận vào một danh sách, thêm phần tử mới vào danh sách và in danh sách.
# Quan sát sự thay đổi của danh sách sau khi gọi hàm

# def cap_nhat_gia_tri(danh_sach):
#     '''
#     hàm cập nhật giá trị
#     nhận vào một danh sách
#     trả về một danh sách mới đã thêm phần tử mới
#     '''
#     danh_sach.append(5)
#     return danh_sach
#
# # gọi hàm và truyền tham số
# ds_moi = cap_nhat_gia_tri([1, 2, 3, 4])
# print(ds_moi)
#
# # bài 2: Viết hàm tinh_tich(a,b) nhận vào 2 tham số. Gọi hàm này bằng cách truyền vào các giá trị trực tiếp và thông qua biến.
# # So sánh sự khác biệt
#
# def tinh_tich(a, b):
#     # # hàm tính tích
#     # nhận vào 2 số a và b
#     # trả về tích của 2 số a và b
#     return a * b
#
# ket_qua = tinh_tich(5, 3)
# print(ket_qua)
#
# y = 5
# x = 3
# def tinh_tich(a, b):
#     # hàm tính tích
#     # nhận vào 2 số a và b
#     # trả về tích của 2 số a và b
#     return a * b
#
# ket_qua1 = tinh_tich(y, x)
# print(ket_qua1)
#
# # bài 3: Viết hàm in_thong_tin(ten, tuoi) và gọi hàm này bằng cách truyền tham số theo thứ tự và không theo thứ tự
#
# def in_thong_tin(ten, tuoi):
#     # hàm in thông tin
#     # in ra tên và tuổi
#     return ten, tuoi
#
# # truyền tham số theo thứ tự
# kq = in_thong_tin('tuấn', 26)
# print('tên', kq[0], 'tuổi', kq[1])
#
# def in_thong_tin(ten, tuoi):
#     # hàm in thông tin
#     # in ra tên và tuổi
#     return ten, tuoi
#
# # truyền tham số không theo thứ tự
# kq = in_thong_tin(26,  'tuấn')
# print('tên', kq[0], 'tuổi', kq[1])
#
# # bài 4: Viết hàm in_ho_so(ten, tuoi, dia_chi) in ra tên tuổi và địa chỉ. Gọi hàm bằng 2 cách (từ khóa và vị trí)
#
# def in_ho_so(ten, tuoi, dia_chi):
#     # hàm in hồ sơ
#     # trả về tên, tuổi và địa chỉ
#     return ten, tuoi, dia_chi
#
# ten, tuoi, diachi = in_ho_so(dia_chi = 'hưng yên', tuoi = 26, ten = 'tuấn')
# print(ten, tuoi, diachi)
#
#
# def in_ho_so(ten, tuoi, dia_chi):
#     # hàm in hồ sơ
#     # trả về tên, tuổi và địa chỉ
#     return ten, tuoi, dia_chi
#
# ten, tuoi, diachi = in_ho_so('tuấn', 26, 'hưng yên')
# print(ten, tuoi, diachi)
#
# # bài 5: Viết hàm tinh_tien(khach_hang, san_pham=0) trong đó tham số san_pham có giá trị mặc định là 0.
# # Nếu khách không mua hàng thì in ra màn hình “Khach khong mua”.
# # Nếu san_pham >0 thì in ra màn hình Tên khách hàng + số lượng sản phẩm đã mua.
#
# def tinh_tien(khach_hang, san_pham = 0):
#     '''
#     hàm tính tiền
#     nhận vào tên khách hàng và số lượng sản phẩm
#     trả về, nếu khách hàng không mua gì thì sẽ in ra khách hàng không mua gì
#             nếu khách hanng mùa hàng thì sẽ in ra Tên khách hàng + số lượng sản phẩm đã mua.
#     '''
#     if san_pham <= 0:
#         print('khách hàng không mua gì')
#     else:
#         print(f'{khach_hang} đã mua số lượng sản phẩm là {san_pham}')
#
# tinh_tien('hữu tuấn', 6)
#
# # bài 6: Viết hàm tinh_tong(*args) nhận vào số lượng tham số bất kì và trả về tổng của chừng
#
# def tinh_tong(*args):
#     '''
#     hàm tính tổng
#     nhận vào một số lượng số int bất kỳ
#     trả về tổng của các số đó
#     '''
#     return sum(args)
#
# ket_qua_tinh_tong = tinh_tong(5, 5, 5)
# print(ket_qua_tinh_tong)
#
# # bài 7: Viết chương trình với biến toàn cục counter = 0 và một hàm tang_counter()
# # để tăng giá trị của biến này. In ra màn hình biến toàn cục sau khi tăng.
#
# counter = 0
# def tang_counter():
#     '''
#     hàm tăng counter
#     tăng biến toàn cục
#     '''
#     global counter
#     counter += 1
# tang_counter()
# print(counter)
#
# # bài 8: Viết chương trình với một biến toàn cục x = 10,
# # sau đó viết hàm thay_doi_x() để thay đổi giá trị của biến này bằng cách sử dụng từ khóa global
#
# x = 10
# def thay_doi_x():
#     '''
#     hàm thay đổi biến toàn cục (x)
#     '''
#     global x
#     x = 20
# thay_doi_x()
# print(x)

# bài 9: Viết hàm in_danh_sach(danh_sach) nhận vào một danh sách và in từng phần tử của danh sách đó

# def in_danh_sach(danh_sach):
#     '''
#     hàm in danh sách
#     nhận vào một danh sách
#     trả về từng phần tử của danh sách đó
#     '''
#     for i in danh_sach:
#         print(i)
#
# ds = ['xin', 'chào', 'bạn' ]
# in_danh_sach(ds)

# bài 10: Viết hàm đệ quy giai_thua(n) để tính giai thừa của một số nguyên

# def giai_thua(n):
#     '''
#     hàm tính giai thừa
#     nhận vào 1 số nguyên
#     trả về giai thừa của số ý
#     '''
#     if n == 0:
#         return 1
#     return n * giai_thua(n - 1)
#
# print(giai_thua(5))

# bài 11: Sử dụng hàm lambda để viết biểu thức tính tổng của 2 số,
#         và sử dụng nó để tính tổng của các số 3 và 5

# # tạo hàm vô danh lambda
# tinh_tong = lambda x, y: x + y
#
# # gọi hàm và truyền tham số
# ket_qua = tinh_tong(3, 5)
# print(ket_qua)

# bài 12: Viết một hàm trang_tri(f) là một decorator,
#         và sử dụng decorator này để trang trí một hàm chao() in ra “Xin chào!”

# def trang_tri(f):
#     def thuc_thi():
#         f()
#     return thuc_thi()
#
# @trang_tri
# def chao():
#     print('xin chào')

# def so_chan():
#     for i in range(0, 11, 2):
#         yield i
#
# kq = so_chan()
# for i in kq:
#     print(i)

# bài 13: Viết chương trình thực hiện tính diện tích và chu vi của một hình chữ nhật,
# tỏng đó bạn phải tách các hàm tính toán thành các hàm riêng biệt

# def tinh_dien_tich(chieu_dai, chieu_rong):
#   """Hàm tính diện tích hình chữ nhật"""
#   return chieu_dai * chieu_rong
#
# def tinh_chu_vi(chieu_dai, chieu_rong):
#   """Hàm tính chu vi hình chữ nhật"""
#   return 2 * (chieu_dai + chieu_rong)
#
# if __name__ == "__main__":
#   chieu_dai = float(input("Nhập chiều dài: "))
#   chieu_rong = float(input("Nhập chiều rộng: "))
#
#   dien_tich = tinh_dien_tich(chieu_dai, chieu_rong)
#   chu_vi = tinh_chu_vi(chieu_dai, chieu_rong)
#
#   print("Diện tích hình chữ nhật là:", dien_tich)
#   print("Chu vi hình chữ nhật là:", chu_vi)

# bài 14: Tạo một file Python my_math.py với các hàm tính tổng và hiệu.
# Sau đó, tạo một file khác và import module my_math để sử dụng các hàm này

import my_math
print(my_math.tinh_tong(4,5,8))
print(my_math.tinh_hieu(5, 3))

