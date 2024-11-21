# Bài tập 1: Tạo, cập nhật và xử lý List
# Tạo một danh sách chứa các số nguyên từ 1 đến 10 bằng cách sử dụng hàm range().
# Thay đổi giá trị của phần tử thứ 4 thành 20.
# Thêm một phần tử mới có giá trị 25 vào cuối danh sách.
# Xóa phần tử đầu tiên trong danh sách.
# Sắp xếp danh sách theo thứ tự giảm dần.
# Tạo một danh sách mới là bản sao của danh sách hiện tại và thêm phần tử 30 vào danh sách mới.
# Kiểm tra xem số 20 có tồn tại trong danh sách hay không.

# # Tạo list số nguyên từ 1 đến 10
# so_nguyen = list(range(1, 11))
#
# # Thay đổi giá trị của phần tử thứ 4 thành 20
# so_nguyen[3] = 20
#
# # Thêm một phần tử mới có giá trị 25 vào cuối danh sách.
# so_nguyen.append(25)
#
# # Xóa phần tử đầu tiên trong danh sách.
# so_nguyen.pop(0)
#
# # Sắp xếp danh sách theo thứ tự giảm dần.
# so_nguyen.sort(reverse = True)
#
# # Tạo bản sao
# ban_sao_so_nguyen = so_nguyen[:]
# # thêm phần tử 30 vào danh sách mới
# ban_sao_so_nguyen.append(30)
#
# # Kiểm tra xem số 20 có tồn tại trong danh sách hay không.
# print(20 in so_nguyen)
# print(so_nguyen)

# Bài tập 2: Sử dụng Nested List và List Comprehensions
# Tạo một danh sách lồng nhau chứa ba danh sách con, mỗi danh sách con chứa các số nguyên từ 1 đến 3.
# Truy cập và hiển thị phần tử thứ 2 của danh sách con thứ 2.
# Sử dụng list comprehension để tạo một danh sách mới chứa các bình phương của các số từ 1 đến 10.
# Tính tổng của tất cả các phần tử trong danh sách mới tạo.

# # list lồng nhau
# list_long = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# # Truy cập và hiển thị phần tử thứ 2 của danh sách con thứ 2.
# print(list_long[1][1])
#
# # bình phương của các số từ 1 đến 10
# binh_phuong = [i ** 2 for i in range(1, 11)]
#
# # Tính tổng của tất cả các phần tử trong danh sách mới tạo.
# tong = sum(binh_phuong)
# print(binh_phuong)
# print(tong)

# Bài tập 3: Tạo và xử lý Tuple
# Tạo một tuple chứa các số nguyên từ 1 đến 5.
# Truy cập và hiển thị phần tử thứ 3 của tuple.
# Tạo một tuple mới bằng cách nối tuple ban đầu với một tuple chứa các số 6, 7, 8.
# Sử dụng các hàm len(), min(), max(), và sum() để tính toán và hiển thị độ dài, giá trị nhỏ nhất, giá trị lớn nhất và tổng của các phần tử trong tuple mới tạo.
# Tạo một tuple lồng nhau chứa ba tuple con, mỗi tuple con chứa ba số nguyên. Truy cập và hiển thị phần tử thứ 2 của tuple con thứ 3.

# Tạo một tuple chứa các số nguyên từ 1 đến 5.
# so_nguyen = tuple(range(1, 6))
#
# # Truy cập và hiển thị phần tử thứ 3 của tuple.
# print(so_nguyen[2])
#
# # Tạo một tuple mới bằng cách nối tuple ban đầu với một tuple chứa các số 6, 7, 8.
# tuple_moi = (6, 7, 8)
# hop_nhat = so_nguyen + tuple_moi
#
# # độ dài của tuple hop_nhat
# do_dai = len(hop_nhat)
#
# # giá trị nhỏ nhất
# nho_nhat = min(hop_nhat)
#
# # giá trị nhỏ nhất
# lon_nhat = max(hop_nhat)
#
# # tổng các phần tử
# tong = sum(hop_nhat)
#
# # Tạo một tuple lồng nhau chứa ba tuple con
# tuple_long_nhau = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
#
# # Truy cập và hiển thị phần tử thứ 2 của tuple con thứ 3.
# print(tuple_long_nhau[2][1])

# Bài tập 4: Kết hợp List và Tuple
# Tạo một danh sách chứa các tuple, mỗi tuple chứa hai phần tử là tên và tuổi của một người.
# Thêm một tuple mới vào danh sách với thông tin của một người mới.
# Tìm và hiển thị thông tin của người có tuổi lớn nhất trong danh sách.
# Sử dụng list comprehension để tạo một danh sách chứa tên của tất cả mọi người trong danh sách ban đầu.

# list chứa tuple
# list_tuple = [('tuấn', 26), ('lan anh', 30), ('quý', 18)]
#
# # Thêm một tuple mới vào danh sách
# list_tuple.append(('cường', 29))
#
# # tạo một list chứa tuổi
# tuoi = []
# # duyệt qua từng phần tử tuổi trong list
# for i in range(len(list_tuple)):
#     # lấy tuổi của mỗi người, cho vào list tuoi
#     tuoi.append(list_tuple[i][1])
#
# # duyệt qua từng phần tử trong list_tuple
# for i in list_tuple:
#
#     if i[1] == max(tuoi):
#         print(i)
#
# ten_moi_nguoi = [i[0] for i in list_tuple[:]]
#
# print(ten_moi_nguoi)

# Bài tập 5: Sử dụng List và Tuple để xử lý dữ liệu
# Tạo một danh sách chứa các số nguyên từ 1 đến 10.
# Sử dụng hàm tuple() để chuyển đổi danh sách này thành một tuple.
# Tạo một tuple chứa các phần tử có kiểu dữ liệu khác nhau (số nguyên, chuỗi, số thực).
# Tạo một danh sách lồng nhau chứa các tuple, mỗi tuple chứa ba số nguyên. Tính tổng của tất cả các phần tử trong danh sách lồng nhau này.

so_nguyen = [i for i in range(1, 11)]

so_nguyen = tuple(so_nguyen)

tong_hop = ('tuấn', 26, 2.544)

list_chua_tuple = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
tong = sum(list_chua_tuple[0] + list_chua_tuple[1] + list_chua_tuple[2])
print(tong)
