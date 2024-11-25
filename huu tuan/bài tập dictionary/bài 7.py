# 7. Passing Dictionaries to Functions
# Bài tập:
# Viết chương trình quản lý thông tin học sinh. Tạo dictionary student = {"name": "Huy", "age": 25, "grade": "A"}.
# Yêu cầu:
# Viết hàm print_student_info(student) để in thông tin chi tiết.
# Viết hàm update_grade(student, new_grade) để cập nhật điểm học sinh.
# Gọi cả hai hàm và in kết quả.

def print_student_info(student):
    for k, v in student.items():
        print(k, v)

def update_grade(student, new_grade):
    student['điểm học sinh'] = new_grade


student = {"name": "Huy", "age": 25, "grade": "A"}

update_grade(student, 10)
print_student_info(student)