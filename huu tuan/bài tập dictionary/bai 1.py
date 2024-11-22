# Viết chương trình quản lý giỏ hàng. Tạo dictionary cart để lưu thông tin sản phẩm (tên sản phẩm là key, số lượng là value).
# Yêu cầu:
# Thêm một sản phẩm vào giỏ hàng.
# Cập nhật số lượng của một sản phẩm có sẵn.
# Xóa một sản phẩm khỏi giỏ hàng.
# In danh sách sản phẩm hiện tại trong giỏ hàng.

# Tạo dictionary cart
cart = {'táo': 10, 'lê': 15, 'dưa': 20, 'chuối': 9}

# Thêm một sản phẩm vào giỏ hàng.
cart['bưởi'] = 4

# Cập nhật số lượng của một sản phẩm có sẵn.
cart['lê'] = 19

# Xóa một sản phẩm khỏi giỏ hàng.
cart.pop('táo')
print(cart)