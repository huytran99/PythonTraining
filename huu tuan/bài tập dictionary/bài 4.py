# Cho dicti onary employees = {"Huy": 50000, "Linh": 70000, "Minh": 60000} lưu lương của nhân viên.
# Viết chương trình để:
# Sắp xếp danh sách nhân viên theo mức lương tăng dần.
# In danh sách nhân viên cùng lương sau khi sắp xếp.

# luu lương nhân viên
employees = {"Huy": 50000, "Linh": 70000, "Minh": 60000}

# sắp xếp tăng dần
sap_xep = dict(sorted(employees.items(), key = lambda item: item[1]))

# in danh sách nhân viên
print(sap_xep)