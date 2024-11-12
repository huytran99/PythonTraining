
# Tạo 1class HinhChuNhat
class HinhChuNhat:

    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
    # tạo hàm tính diện tích
    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong
    # tạo hàm tính chu vi
    def tinh_chu_vi(self):
        return 2 * (self.chieu_dai + self.chieu_rong)

# tạo đối tượng hình chữ nhật và truyền tham số vào
hcn = HinhChuNhat(20, 50)
# in ra màn hình diện tích hình chữ nhật
print(hcn.tinh_dien_tich())
# in ra màn hình chu vi hình chữ nhật
print(hcn.tinh_chu_vi())

# Viết hàm độc lập tính dien_tich_hinh_chu_nhat nhận vào chiều dài và chiều rộng để tính diện tích
def dien_tich_hinh_chu_nhat(chieu_dai, chieu_rong):
    return chieu_dai * chieu_rong
print(dien_tich_hinh_chu_nhat(20, 50))