#Bước 1: Thông báo chào mừng và giới thiệu về chương trình.
print("Chào mừng bạn đến với hệ thống quản lý sinh viên và điểm số")

#Bước 2: Tạo một menu để người dùng chọn chức năng muốn thực hiện.
def hien_thi_menu():
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ SINH VIÊN VÀ ĐIỂM SỐ =====")
        print("\n1. Thêm sinh viên")
        print("2. Hiển thị danh sách sinh viên")
        print("3. Tính điểm trung bình của sinh viên")
        print("4. Tìm kiếm sinh viên")
        print("5. Cập nhật thông tin sinh viên")
        print("6. Xóa sinh viên")
        print("7. Thoát chương trình")

        chon = input("Bạn chọn chức năng nào? ")

        if chon.isdigit():
            chon = int(chon)
            if chon == 1:
                them_sinh_vien()
            elif chon == 2:
                hien_thi_danh_sach_sinh_vien()
            elif chon == 3:
                tinh_diem_trung_binh_cua_sinh_vien()  
            elif chon == 4:
                tim_kiem_sinh_vien()
            elif chon == 5:
                cap_nhat_thong_tin_sinh_vien()  
            elif chon == 6:
                xoa_sinh_vien()
            elif chon == 7:
                print("Thoát chương trình.") 
                break
            else:
                print("Vui lòng chọn lại chức năng từ 1 đến 7.")
        else:
            print("Vui lòng nhập một số hợp lệ.")
            
# Khởi tạo danh sách sinh viên
danh_sach_sinh_vien = []

# Hàm thêm sinh viên mới
def them_sinh_vien():
    name = input("Nhập tên sinh viên: ")
    diem_mon_hoc = {}
    while True:
        mon_hoc = input(f"Nhập tên môn học: ")
        if mon_hoc =="":
            break
        diem = float(input(f"Nhập điểm cho môn {mon_hoc}: "))
        diem_mon_hoc[mon_hoc] = diem 
         
    sinh_vien = {
        "ten": name,
        "diem": diem_mon_hoc
    }
    
    danh_sach_sinh_vien.append(sinh_vien)
    print(f"Đã thêm sinh viên thành công!\n")
    
#Tính điểm trung bình của từng sinh viên
def tinh_diem_trung_binh():
        for sv in danh_sach_sinh_vien:
            diem_so = sv['diem']
            trung_binh = sum(diem_so.values()) / len(diem_so) if diem_so else 0
            print(f"Tên: {sv['ten']}, điểm trung bình: {trung_binh:.2f}")

#Hàm tìm kiếm sinh viên theo tên
def tim_kiem_sinh_vien():
        ten_tim_kiem = input("Nhập tên sinh viên cần tìm: ").lower()
        for sv in danh_sach_sinh_vien:
            if sv['ten'].lower() == ten_tim_kiem:
                print(f"Tên: {sv['ten']}")
                for mon, diem in sv['diem'].items():
                    print(f"Môn {mon}: {diem}")
                break
        if not sinh_vien_tim_thay:
            print(f"Không tìm thấy sinh viên có tên '{ten_tim_kiem}'.")
            
#Cập nhật điểm số của sinh viên
def cap_nhat_diem_sinh_vien():
    name = input("Nhập tên sinh viên cần cập nhật điểm số: ")
    for sv in danh_sach_sinh_vien:
        if sinh_vien['ten'].lower() == ten.lower():
                ten_mon = input("Tên môn học cần cập nhật: ")
                sinh_vien['mon_hoc'][ten_mon] = float(input(f"Điểm {ten_mon}: "))
                print("Cập nhật điểm thành công.")
                break  
            
# Hàm xóa sinh viên khỏi danh sách
def xoa_sinh_vien():
    name = input("Nhập tên sinh viên cần xóa: ")
    for sv in danh_sach_sinh_vien:
        if sv['ten'].lower() == name.lower(): 
            danh_sach_sinh_vien.remove(sv) 
            print(f"Đã xóa sinh viên có tên {sv['ten']}.")
