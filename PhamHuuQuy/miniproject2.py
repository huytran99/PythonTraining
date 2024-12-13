print("Chào mừng bạn đến với chương trình Quản lý Chi tiêu cá nhân!")
print("Chương trình giúp bạn quản lý chi tiêu hàng ngày, tổng hợp và phân tích dễ dàng.")

def hien_thi_menu():
    print("\nChọn chức năng:")
    print("1. Thêm khoản chi tiêu")
    print("2. Hiển thị danh sách chi tiêu")
    print("3. Tổng hợp chi tiêu")
    print("4. Tìm kiếm chi tiêu")
    print("5. Xóa hoặc cập nhật chi tiêu")
    print("6. Phân tích chi tiêu nâng cao")
    print("0. Thoát chương trình")

hien_thi_menu()

chi_tieu = []

def them_chi_tieu():
    danh_muc = input("Nhập danh mục: ")
    so_tien = float(input("Nhập số tiền: "))
    ngay_chi = input("Nhập ngày (dd/mm/yyyy): ")
    ghi_chu = input("Nhập ghi chú: ")
    chi_tieu.append([danh_muc, so_tien, ngay_chi, ghi_chu])
    print("Đã thêm khoản chi tiêu!")
def hien_thi_chi_tieu():
    print("\nDanh sách chi tiêu:")
    print("Danh mục | Số tiền | Ngày | Ghi chú")
    [print(f"{item[0]} | {item[1]} | {item[2]} | {item[3]}") for item in chi_tieu]
from collections import defaultdict

def tong_hop_chi_tieu():
    tong_hop = defaultdict(float)
    for item in chi_tieu:
        tong_hop[item[0]] += item[1]
    sorted_tong_hop = dict(sorted(tong_hop.items(), key=lambda x: x[1], reverse=True))
    print("\nTổng hợp chi tiêu:")
    for dm, tong in sorted_tong_hop.items():
        print(f"{dm}: {tong} VND")
def tim_kiem_chi_tieu():
    tu_khoa = input("Nhập từ khóa (danh mục, ngày, ghi chú): ").lower()
    ket_qua = [item for item in chi_tieu if tu_khoa in item[0].lower() or tu_khoa in item[2] or tu_khoa in item[3].lower()]
    if ket_qua:
        print("\nKết quả tìm kiếm:")
        [print(f"{item[0]} | {item[1]} | {item[2]} | {item[3]}") for item in ket_qua]
    else:
        print("Không tìm thấy kết quả phù hợp.")
def xoa_sua_chi_tieu():
    hien_thi_chi_tieu()
    vi_tri = int(input("Nhập vị trí khoản chi tiêu cần xóa/sửa (bắt đầu từ 0): "))
    if 0 <= vi_tri < len(chi_tieu):
        lua_chon = input("Bạn muốn (xóa/sửa): ").lower()
        if lua_chon == "xóa":
            chi_tieu.pop(vi_tri)
            print("Đã xóa khoản chi tiêu.")
        elif lua_chon == "sửa":
            danh_muc = input("Nhập danh mục mới: ")
            so_tien = float(input("Nhập số tiền mới: "))
            ngay_chi = input("Nhập ngày mới (dd/mm/yyyy): ")
            ghi_chu = input("Nhập ghi chú mới: ")
            chi_tieu[vi_tri] = [danh_muc, so_tien, ngay_chi, ghi_chu]
            print("Đã cập nhật khoản chi tiêu.")
    else:
        print("Vị trí không hợp lệ.")
def phan_tich_chi_tieu():
    if not chi_tieu:
        print("Chưa có dữ liệu chi tiêu.")
        return
    from itertools import groupby

    tong_hop = defaultdict(float)
    for item in chi_tieu:
        tong_hop[item[0]] += item[1]
    max_danh_muc = max(tong_hop, key=tong_hop.get)
    min_danh_muc = min(tong_hop, key=tong_hop.get)
    print(f"Danh mục chi tiêu lớn nhất: {max_danh_muc} - {tong_hop[max_danh_muc]} VND")
    print(f"Danh mục chi tiêu nhỏ nhất: {min_danh_muc} - {tong_hop[min_danh_muc]} VND")
    print("\nDuyệt qua dữ liệu:")
    for chi in iter(chi_tieu):
        print(chi)