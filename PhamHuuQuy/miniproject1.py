# quan_ly_sinh_vien.py

#chào mừng
def chao_mung():
    print("Chào mừng bạn đến với chương trình Quản Lý Sinh Viên")
    print("Chương trình này giúp bạn quản lý thông tin sinh viên một cách hiệu quả.")
    print("Bạn có thể thêm, cập nhật, tìm kiếm và xóa thông tin sinh viên trong hệ thống.")

#menu chính
def menu():
    chao_mung()
    while True:
        print("--- Menu ---")
        print("1. Thêm sinh viên mới")
        print("2. Hiển thị danh sách sinh viên")
        print("3. Tính điểm trung bình của từng sinh viên")
        print("4. Tìm kiếm sinh viên theo tên")
        print("5. Cập nhật điểm số sinh viên")
        print("6. Xóa sinh viên")
        print("7. Thoát")
        lua_chon = input("Chọn chức năng (1-7): ")

        if lua_chon == "1":
            them_sinh_vien()
        elif lua_chon == "2":
            hien_thi_sinh_vien()
        elif lua_chon == "3":
            tinh_diem_trung_binh()
        elif lua_chon == "4":
            tim_kiem_sinh_vien()
        elif lua_chon == "5":
            cap_nhat_diem_so_sinh_vien()
        elif lua_chon =="6":
            xoa_sinh_vien()
        elif lua_chon == "7":
            print("thoát ra.")
            break
        else:
            print("lựa chọn không hợp lệ. Vui lòng chọn lại")
#Tạo danh sách vinh viên
danh_sach_sinh_vien = []

#thêm sinh viên mới
def them_sinh_vien():
    ten = input("nhập tên sinh vien: ")
    diem_so = {}
    while True:
        mon = input("nhập tên môn học (nhấn enter để dừng)")
        if mon =="":
            break
        diem = float (input(f"nhập điểm cho môn {mon}: "))
        diem_so[mon] = diem
    danh_sach_sinh_vien.append({"ten": ten, "diem_so": diem_so})
    print("đã thêm sinh viên thành công")

#Hiện thị danh sách sinh viên
def hien_thi_sinh_vien():
    for sinh_vien in danh_sach_sinh_vien:
        print(f"tên: {sinh_vien['ten']}, Điểm: {sinh_vien['diem_so']}")

#tinh điểm trung bình của từng sinh vien
def tinh_diem_trung_binh():
    for sinh_vien in danh_sach_sinh_vien:
        diem_so = sinh_vien['diem_so']
        trung_binh = sum(diem_so.values()) / len(diem_so) if diem_so else 0
        print(f"tên: {sinh_vien['ten']}, điểm trung bình: :{trung_binh:.2f}")

#tiềm kiếm sinh viên theo tên
def tim_kiem_sinh_vien():
    ten = input("nhập ten sinh viên cần tìm: ")
    for sinh_vien in danh_sach_sinh_vien:
        if sinh_vien['ten'].lower() == ten.lower():
            print(f"đã tìm thấy: tên: {sinh_vien['ten']}, điểm: {sinh_vien['diem_so']}")
            return
    print("không tìm thấy sinh viên.")


# Cập nhật điểm số của sinh viên
def cap_nhat_diem_so_sinh_vien():
    ten = input("Nhập tên sinh viên cần cập nhật điểm số: ")

    # Tìm sinh viên theo tên
    for sinh_vien in danh_sach_sinh_vien:
        if sinh_vien['ten'].lower() == ten.lower():
            # Nhập tên môn học cần cập nhật
            mon = input("Nhập tên môn học cần cập nhật: ")
            # Kiểm tra nếu môn học đã có trong danh sách môn học của sinh viên
            if mon in sinh_vien['diem_so']:
                # Nhập điểm số mới
                diem_moi = float(input(f"Nhập điểm mới cho môn {mon}: "))
                sinh_vien['diem_so'][mon] = diem_moi
                print(f"Đã cập nhật điểm số cho môn {mon} của sinh viên {ten}.")
            else:
                print(f"Môn học {mon} không tồn tại trong danh sách môn học của sinh viên {ten}.")
            return

    print("Không tìm thấy sinh viên với tên đã nhập.")

# Xóa sinh viên khỏi danh sách
def xoa_sinh_vien():
    ten = input("Nhập tên sinh viên cần xóa: ")
    for sinh_vien in danh_sach_sinh_vien:
        if sinh_vien['ten'].lower() == ten.lower():
            danh_sach_sinh_vien.remove(sinh_vien)
            print("Đã xóa sinh viên.")
            return
    print("Không tìm thấy sinh viên.")


# Khởi động chương trình
if __name__ == "__main__":
    menu()