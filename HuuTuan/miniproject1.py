# list chứa toàn bộ sinh viêm
danh_sach_sv = []
# dict chứa tên sinh viên
ho_ten_sv = {}
# dict chứa điểm trung bình sinh viên
diem_sv = {}
# class quản lý sinh viên
class Quan_lý_sinh_vien:
    # tạo đối tượng sinh viên
    def __init__(self, masv, hoten, mon_hoc_1, mon_hoc_2, mon_hoc_3, diem_mh1 = 0, diem_mh2 = 0, diem_mh3 = 0, diem_trung_binh = 0):
        self.masv = masv
        self.hoten = hoten
        self.mon_hoc_1 = mon_hoc_1
        self.mon_hoc_2 = mon_hoc_2
        self.mon_hoc_3 = mon_hoc_3
        self.diem_mon_hoc1 = diem_mh1
        self.diem_mon_hoc2 = diem_mh2
        self.diem_mon_hoc3 = diem_mh3
        self.diem_trung_binh = diem_trung_binh
    # hàm thêm sinh viên
    def themsv(self):
         try:
            # biến này để chống cho mã sinh viên không bị trùng nhau
            temp = True
            # hỏi người dùng muốn thêm bao nhiêu sinh viên
            hoi = int(input('bạn muốn thêm bao nhiêu sinh viên: '))
            # vòng for chạy theo số sinh viên người dùng muốn thêm
            for i in range(hoi):
                # nếu temp là False vòng lập sẽ dừng lại
                if temp == False:
                    break
                # nhập mã sinh viên
                ma_sv = int(input(f'nhập mã sinh viên thứ {i+1}: '))
                # vòng lập for này sẽ duyệt qua từng phần tử trong danh_sach_sv
                for j in danh_sach_sv:
                    # nếu mã sinh viên trong danh_sach_sv trùng với mã sinh viên mà người dùng nhập vào thì sẽ thông báo mã sinh viên đã tồn tại và biến temp sẽ là False để dừng vòng lập i
                    if j.masv == ma_sv:
                        print('mã sinh viên đã tồn tại')
                        temp = False
                # biến temp phải mà True thì mới cho người dùng nhập tiếp
                if temp:
                    ho_ten = input(f'nhập họ tên sinh viên thứ {i+1}: ')
                    mon1 = input('nhập môn học 1: ')
                    mon2 = input('nhập môn học 2: ')
                    mon3 = input('nhập môn học 3: ')
                    # tạo đối tượng sinh viên
                    sv = Quan_lý_sinh_vien(ma_sv, ho_ten, mon1, mon2, mon3)
                    # append đối tượng sinh viên vào danh_sach_sv
                    danh_sach_sv.append(sv)
         except:
             print('lỗi cú pháp')
    # hàm tính điểm trung bình
    def Diem_trung_binh(self):
        # duyệt qua từng phần tử trong danh_sach_sv
        for i in danh_sach_sv:
            # i.diem_trung_binh sẽ = điểm của 3 môn học công tổng vào xong rồi chia cho số lượng môn học
            i.diem_trung_binh = (i.diem_mon_hoc1 + i.diem_mon_hoc2 + i.diem_mon_hoc3) / 3

            # thêm họ tên sinh viên và điểm trung bình vào dict đã tạo ở trên
            ho_ten_sv[i.hoten] = i.diem_trung_binh
        # vòng lập for duyệt qua key và value
        for ten, diem in ho_ten_sv.items():
            # in ra màn hình họ tên và điểm trung bình của từng sinh viên
            print(f'{ten}: {diem}')
    # hàm xem tất cả sinh viên
    def xem_danh_sach_sinh_vien(self):
        # danh_sach_sv phải có sinh viên thì mới in ra màn hình
        if len(danh_sach_sv):
            # in ra số lượng sinh viên trong danh_sach_sv
            print(f'số lượng sinh viên {len(danh_sach_sv)}')
            # duyệt qua từng phần tử trong danh_sach_sv
            for i in danh_sach_sv:
                # in ra từng sinh viên trong danh_sach_sv
                print(f'Mã SV: {i.masv}, Họ tên: {i.hoten}, Điểm {i.mon_hoc_1}: {i.diem_mon_hoc1}, Điểm {i.mon_hoc_2}: {i.diem_mon_hoc2}, Điểm {i.mon_hoc_3}: {i.diem_mon_hoc3} ')
        # nếu trong danh_sach_sv không có sinh viên nào thì sẽ thông báo không có sinh viên nào
        else:
            print('không có sinh viên nào')
    # hàm tìm kiếm sinh viên theo tên
    def tim_kiem_theo_ten(self):
        # hập tên sinh viên cần tìm
        nhap_ten_sv = input('nhập tên sinh viên cần tìm: ')
        # duyệt qua từng phần tử trong danh_sach_sv
        for i in danh_sach_sv:
            # nếu i.hoten mà giống với họ tên nguoi dung nhập vào thì sẽ in ra màn hình thông tin của sinh viên ý
            if nhap_ten_sv == i.hoten:
                print(f'Mã SV: {i.masv}, Họ tên: {i.hoten}, Điểm {i.mon_hoc_1}: {i.diem_mon_hoc1}, Điểm {i.mon_hoc_2}: {i.diem_mon_hoc2}, Điểm {i.mon_hoc_3}: {i.diem_mon_hoc3} ')
    # hàm xóa sinh viên theo mã sinh viên
    def xoa_sv(self):
        try:
            # nhập mã sinh viên cần xóa
            nhap_ma_sinh_viem = int(input('nhập mã sinh viên cần xóa: '))
            # i sẽ đứng ở giữa danh_sach_sv
            i = len(danh_sach_sv) // 2
            # sắp xếp danh_sach_sv theo thứ tự tăng dâm
            danh_sach_sv.sort()
            while 1:
                if i > len(danh_sach_sv) or i < len(danh_sach_sv):
                    print('không có mã sinh viên này')
                    break
                # nếu danh_sach_sv[i] mà bằng với mã sinh nguoi dung nhập vào thì sẽ xóa phần tử trong danh_sach_sv đó và đừng vòng lập
                if danh_sach_sv[i].masv == nhap_ma_sinh_viem:
                    danh_sach_sv.remove(danh_sach_sv[i])
                    break
                # nếu số nguoi dung nhập vào mà bé hơn mã sinh viên tại vị trí i thì sẽ cho i trừ 1 để danh_sach_sv[i] lùi lại 1 phần tử
                elif danh_sach_sv[i].masv > nhap_ma_sinh_viem:
                    i -= 1
                # nếu số nguoi dung nhập vào mà lớn hơn mã sinh viên tại vị trí i thì sẽ cho i cộng 1 để danh_sach_sv[i] tiên lên 1 phần tử
                elif danh_sach_sv[i].masv < nhap_ma_sinh_viem:
                    i += 1
        except:
            print('lỗi cú pháp')

    # hàm cập nhật điểm sinh viên
    def Cap_nhat_diem(self):
        temp = True
        # nhập họ tên sinh viên cần cập nhật điểm
        cap_nhat_diem = input('nhập họ tên sinh viên cần cập nhật điểm: ')
        # duyệt qua từng phần tử trong danh_sach_sv
        for i in danh_sach_sv:
            # nếu i.hoten mà giống với họ têm sinh viên nguoi dung nhập vào thì sẽ cho người dùng nhập điểm của sinh viên ý
            if cap_nhat_diem == i.hoten:
                try:
                    mon1 = float(input(f'nhập điểm môn {i.mon_hoc_1} của sinh viên {i.hoten}: '))
                    mon2 = float(input(f'nhập điểm môn {i.mon_hoc_2} của sinh viên {i.hoten}: '))
                    mon3 = float(input(f'nhập điểm môn {i.mon_hoc_3} của sinh viên {i.hoten}: '))
                    i.diem_mon_hoc1 = mon1
                    i.diem_mon_hoc2 = mon2
                    i.diem_mon_hoc3 = mon3
                    temp = False
                except:
                    print('lỗi cú pháp')
        # nếu không tim thấy sinh viên trong danh_sach_sv thì sẽ thông báo không tìm thấy sinh viên này
        if temp:
            print('không tìm thấy sinh viên này')


while 1:
    # giới thiệu những chức năng
    print('''                         chào bạn. mời bạn chọn chức năng của phần mềm
                                  0 ==> thoát
                                  1 ==> thêm sinh viên
                                  2 ==> xem danh sách sinh viên
                                  3 ==> xóa sinh viên theo mã sinh viên
                                  4 ==> tìm kiếm sinh viên theo tên
                                  5 ==> tính điểm trung bình
                                  6 ==> cập nhật điểm sinh viên''')

    # cho người dùng chọn chức năng
    nguoi_dung = int(input('mời bạn nhập: '))

    # tạo đối tượng quản lý sinh viên
    qlsv = Quan_lý_sinh_vien(0, 'name', 'a', 'b', 'c')

    # nếu nguoi_dung chọn chức năng thêm sinh vinh thì sẽ gọi hàm themsv
    if nguoi_dung == 1:
        qlsv.themsv()

    # nếu nguoi_dung chọn chức năng xem tất cả sinh vinh thì sẽ gọi hàm xem_danh_sach_sinh_vien
    elif nguoi_dung == 2:
        qlsv.xem_danh_sach_sinh_vien()

     # nếu nguoi_dung chọn chức năng xóa sinh vinh thì sẽ gọi hàm xoa_sv
    elif nguoi_dung == 3:
        qlsv.xoa_sv()

    # nếu nguoi_dung chọn chức năng tìm kiếm sinh vinh thì sẽ gọi hàm tim_kiem_theo_ten
    elif nguoi_dung == 4:
        qlsv.tim_kiem_theo_ten()

    # nếu nguoi_dung chọn chức năng tính điểm trung binh sinh vinh thì sẽ gọi hàm diem_trung_binh
    elif nguoi_dung == 5:
        qlsv.Diem_trung_binh()

    # nếu nguoi_dung chọn chức năng cập nhật điểm sinh vinh thì sẽ gọi hàm cap_nhat_diem
    elif nguoi_dung == 6:
        qlsv.Cap_nhat_diem()

    # dừng lại chương chình
    elif nguoi_dung == 0:
        break