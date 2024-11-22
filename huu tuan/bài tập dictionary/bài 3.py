# Cho dictionary students = {"Huy": 9, "Linh": 8, "Minh": 7} lưu điểm của học sinh.
# Viết chương trình sử dụng vòng lặp for để:
# In từng học sinh cùng với điểm của họ.
# Tính và in ra điểm trung bình của cả lớp.

students = {"Huy": 9, "Linh": 8, "Minh": 7}

for ten, diem in students.items():
    print(ten, diem)

diem = students.values()
print(f'diểm trung bình của cả lớp là {sum(diem) / len(diem)}')