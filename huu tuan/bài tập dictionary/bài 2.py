# Tạo một hệ thống quản lý điểm của học sinh. Tạo dictionary grades lưu tên học sinh và điểm trung bình của họ.
# Yêu cầu:
# Thêm một học sinh mới và điểm của họ bằng update().
# In tất cả các học sinh và điểm bằng cách sử dụng items().
# Lấy điểm của một học sinh cụ thể bằng get() (nhập từ bàn phím).
# Xóa học sinh có điểm thấp nhất bằng pop().

# Tạo dictionary grades
grades = {'tuấn': 9.5, 'long': 10, 'quy': 9}

# Thêm một học sinh mới và điểm của họ bằng update().
grades.update([('cường', 9.2)])

# In tất cả các học sinh và điểm bằng cách sử dụng items().
for ten, diem in grades.items():
    print(ten, diem)

# Lấy điểm của một học sinh cụ thể bằng get() (nhập từ bàn phím).
nhap = input('nhập tên học sinh: ')
print(grades.get(nhap))

# lấy điểm từng học sinh
list_diem = grades.values()

for ten, diem in grades.items():
    # nếu diem bằng với số bé nhất trong list_diem thì xóa học sinh ý
    if diem == min(list_diem):
        grades.pop(ten)

print(grades)