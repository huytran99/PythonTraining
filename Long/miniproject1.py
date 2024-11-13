print("Chao mung den voi chuong trinh quan ly sinh vien!")

# Danh sach sinh vien co san
danh_sach_sinh_vien = [
    {'ten': 'Tran Viet Long', 'mon_hoc': {'Toan': 8.5, 'Ly': 7.0, 'Hoa': 9}},
    {'ten': 'Nguyen Huu Tuan', 'mon_hoc': {'Toan': 6.5, 'Ly': 7.5, 'Hoa': 8}},
    {'ten': 'Giang Van Tan', 'mon_hoc': {'Toan': 9, 'Ly': 8.5, 'Hoa': 9.5}},
    {'ten': 'Dang Van Dong', 'mon_hoc': {'Toan': 6, 'Ly': 5, 'Hoa': 5.5}},
    {'ten': 'Le Huu Cuong', 'mon_hoc': {'Toan': 8.0, 'Ly': 7.5, 'Hoa': 6}}
]

while True:
    print("\n1. Them sinh vien\n2. Hien thi danh sach\n3. Tinh diem trung binh\n4. Tim sinh vien\n5. Cap nhat diem\n6. Xoa sinh vien\n7. Thoat")
    chon_chuc_nang = input("Chon chuc nang: ")

    if chon_chuc_nang == '1':  # Them sinh vien
        ten = input("Ten sinh vien: ")
        mon_hoc = {}
        while True:
            ten_mon = input("Ten mon hoc (go 'x' de dung): ")
            if ten_mon == 'x': break
            mon_hoc[ten_mon] = float(input(f"Diem {ten_mon}: "))
        danh_sach_sinh_vien.append({'ten': ten, 'mon_hoc': mon_hoc})
        print("Da them sinh vien.")

    elif chon_chuc_nang == '2':  # Hien thi danh sach sinh vien
        
        if not danh_sach_sinh_vien: print("Danh sach trong.")
        for sinh_vien in danh_sach_sinh_vien: 
            print(f"{sinh_vien['ten']} - Diem: {sinh_vien['mon_hoc']}")

    elif chon_chuc_nang == '3':  # Tinh diem trung binh
        for sinh_vien in danh_sach_sinh_vien:
            diem = sinh_vien['mon_hoc'].values()
            diem_trung_binh = sum(diem) / len(diem) if diem else 0
            print(f"{sinh_vien['ten']} - Diem trung binh: {diem_trung_binh:.2f}")

    elif chon_chuc_nang == '4':  # Tim sinh vin
        ten = input("Ten sinh vien can tim: ")
        tim_thay = False
        
        for sinh_vien in danh_sach_sinh_vien:
            if sinh_vien['ten'] == ten:
                print(f"{sinh_vien['ten']} - Diem: {sinh_vien['mon_hoc']}")
                tim_thay = True
                break
        if not tim_thay:
            print("Khong tim thay sinh vien.")
    
    elif chon_chuc_nang == '5':  # Cap nhat diem
        ten = input("Ten sinh vien can cap nhat: ")
        for sinh_vien in danh_sach_sinh_vien:
            if sinh_vien['ten'].lower() == ten.lower():
                ten_mon = input("Ten mon can cap nhat: ")
                sinh_vien['mon_hoc'][ten_mon] = float(input(f"Diem moi cho {ten_mon}: "))
                print("Da cap nhat diem.")
                break
        else:
            print("Khong tim thay sinh vien.")

    elif chon_chuc_nang == '6':  # Xoa sinh vien
        ten = input("Ten sinh vien can xoa: ")
        danh_sach_sinh_vien = [sv for sv in danh_sach_sinh_vien if sv['ten'].lower() != ten.lower()]
        print("Da xoa sinh vien neu co trong danh sach.")

    elif chon_chuc_nang == '7':  # Thoat chuong trinh
        print("Thoat chuong trinh")
        break

    else:
        print("Lua chon khong hop le.")