# 8. Ordered Dictionaries
# Bài tập:
# Sử dụng OrderedDict để lưu trữ danh sách mua sắm.
# Yêu cầu:
# Thêm 3 sản phẩm theo thứ tự nhập vào (tên sản phẩm và số lượng).
# Hiển thị danh sách mua sắm.
# Thêm một sản phẩm mới và hiển thị lại danh sách để kiểm tra thứ tự vẫn được giữ nguyên.

from collections import OrderedDict

# Tạo danh sách mua sắm bằng OrderedDict
shopping_list = OrderedDict()

# Thêm 3 sản phẩm theo thứ tự nhập vào
shopping_list["Sữa"] = 2
shopping_list["Bánh mì"] = 1
shopping_list["Trứng"] = 12

# Hiển thị danh sách mua sắm
print("Danh sách mua sắm ban đầu:")
for item, quantity in shopping_list.items():
    print(f"- {item}: {quantity}")

# Thêm một sản phẩm mới
shopping_list["Táo"] = 6

# Hiển thị lại danh sách mua sắm để kiểm tra thứ tự
print("\nDanh sách mua sắm sau khi thêm sản phẩm mới:")
for item, quantity in shopping_list.items():
    print(f"- {item}: {quantity}")
