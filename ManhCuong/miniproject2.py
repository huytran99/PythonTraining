# quan_ly_chi_tieu.py

from collections import OrderedDict

chi_tieu = []

def chao_mung():
    print("="*30)
    print("Chào mừng bạn đến với chương trình Quản Lý Chi Tiêu Cá Nhân!")
    print("="*30)

def hien_thi_menu():
    print("\nChọn chức năng:")
    print("1. Thêm chi tiêu mới")
    print("2. Hiển thị chi tiêu")
    print("3. Tổng hợp chi tiêu theo danh mục")
    print("4. Thoát chương trình")

def them_chi_tieu():
    danh_muc = input("Nhập danh mục (vd: Ăn uống, Đi lại): ")
    so_tien = float(input("Nhập số tiền: "))
    ngay = input("Nhập ngày chi (dd/mm/yyyy): ")
    ghi_chu = input("Nhập ghi chú (nếu có): ")
    chi_tieu.append([danh_muc, so_tien, ngay, ghi_chu])
    print("Thêm chi tiêu thành công!")

def hien_thi_chi_tieu():
    print("\nDanh mục | Số tiền | Ngày | Ghi chú")
    print("-"*40)
    for muc in chi_tieu:
        print(f"{muc[0]} | {muc[1]} | {muc[2]} | {muc[3]}")

def tong_hop_chi_tieu():
    tong_hop = {}
    for muc in chi_tieu:
        tong_hop[muc[0]] = tong_hop.get(muc[0], 0) + muc[1]
    sap_xep = sorted(tong_hop.items(), key=lambda x: x[1], reverse=True)
    print("\nTổng hợp chi tiêu theo danh mục:")
    for dm, tong in sap_xep:
        print(f"{dm}: {tong} VND")

def main():
    chao_mung()
    while True:
        hien_thi_menu()
        lua_chon = input("Nhập lựa chọn của bạn: ")
        if lua_chon == "1":
            them_chi_tieu()
        elif lua_chon == "2":
            hien_thi_chi_tieu()
        elif lua_chon == "3":
            tong_hop_chi_tieu()
        elif lua_chon == "4":
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()

