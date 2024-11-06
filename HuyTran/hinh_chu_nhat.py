
# Tạo 1 class HinhChuNhat
class HinhChuNhat:
    # tạo hàm tính diện tích
    def tinh_dien_tich(self, chieu_dai, chieu_rong):
        return chieu_dai * chieu_rong
    # tạo hàm tính chu vi
    def tinh_chu_vi(self, chieu_dai, chieu_rong):
        return 2 * (chieu_dai + chieu_rong)

# tạo đối tượng hình chữ nhật và truyền tham số vào
hcn = HinhChuNhat()
# in ra màn hình diện tích hình chữ nhật
print(hcn.tinh_dien_tich(5,10))
# in ra màn hình chu vi hình chữ nhật
print(hcn.tinh_chu_vi(2,4))

# hàm độc lập tính dien_tich_hinh_chu_nhat nhận vào chiều dài và chiều rộng để tính diện tích.
def dien_tich_hinh_chu_nhat(chieu_dai, chieu_rong):
    return chieu_dai * chieu_rong

print(dien_tich_hinh_chu_nhat(5,10))
