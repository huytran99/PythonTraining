# Khởi tạo danh sách tiêu đề và danh sách chi tiêu
danh_muc = ['Danh mục', 'Số tiền', 'Ngày', 'Ghi chú']
danh_sach_chi_tieu = []

# Hiển thị menu chức năng
def menu():
    '''
    Hàm hiển thị menu các chức năng
    '''
    print('''
    Mời bạn chọn chức năng:
    0 =>> Thoát
    1 =>> Thêm khoản chi tiêu
    2 =>> Hiển thị chi tiêu
    3 =>> Tổng hợp chi tiêu
    4 =>> Tìm kiếm chi tiêu
    5 =>> Xóa hoặc cập nhật chi tiêu
    6 =>> Tìm và hiển thị danh mục có chi tiêu lớn nhất, nhỏ nhất
    ''')

# Thêm khoản chi tiêu
def them_khoan_chi_tiẽu():
    '''
    Hàm thêm khoản chi tiêu mới vào danh sách
    '''
    danh_muc = input('Mời bạn nhập danh mục: ')
    tien_da_tieu = int(input('Mời bạn nhập số tiền đã tiêu: '))
    ngay_thang = input('Mời bạn nhập ngày tháng: ')
    ghi_chu = input('Mời bạn nhập ghi chú: ')
    danh_sach_chi_tieu.append([danh_muc, tien_da_tieu, ngay_thang, ghi_chu])

# Hiển thị danh sách chi tiêu
def hien_thi_chi_tieu():
    '''
    Hàm hiển thị danh sách chi tiêu dưới dạng bảng
    '''
    print(f'{danh_muc[0]: <10} | {danh_muc[1]: <10} | {danh_muc[2]: <12} | {danh_muc[3]: <20}')
    print(',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,')
    for i in range(len(danh_sach_chi_tieu)):
        print(f'{danh_sach_chi_tieu[i][0]: <10} | {danh_sach_chi_tieu[i][1]: <10} |'
              f' {danh_sach_chi_tieu[i][2]: <12} | {danh_sach_chi_tieu[i][3]: <20}')

# Tổng hợp chi tiêu theo danh mục
def tong_hop_chi_tieu(ds):
    '''
    Hàm tổng hợp số tiền chi tiêu theo danh mục
    '''
    tong_hop = {}
    for i in ds:
        danh_muc = i[0]
        so_tien = i[1]
        if danh_muc in tong_hop:
            tong_hop[danh_muc] += so_tien
        else:
            tong_hop[danh_muc] = so_tien
    print(dict(sorted(tong_hop.items(), key=lambda x: x[1], reverse=True)))
    return tong_hop

# Tìm kiếm khoản chi tiêu
def tim_kiem(ds):
    '''
    Hàm tìm kiếm khoản chi tiêu dựa trên từ khóa
    '''
    tamp = True
    user_nhap = input('Mời bạn nhập từ khóa muốn tìm kiếm: ')
    for i in ds:
        if user_nhap in i:
            print(i)
            tamp = False
    if tamp:
        print('Không tìm thấy:')

# Xóa khoản chi tiêu
def xoa_chi_tieu(ds):
    '''
    Hàm xóa khoản chi tiêu dựa trên từ khóa hoặc vị trí
    '''
    nhap = input('Mời bạn nhập từ khóa hoặc muốn xóa: ')
    tamp = True
    if nhap.isnumeric():
        nhap = int(nhap)
        ds.pop(nhap)
    else:
        for i in ds:
            if nhap in i:
                ds.remove(i)
        if tamp:
            print('Không tìm thấy:')

# Tìm danh mục có chi tiêu lớn nhất và nhỏ nhất
def danh_muc_lon_nhat_nho_nhat(ds):
    '''
    Hàm tìm danh mục có chi tiêu lớn nhất và nhỏ nhất
    '''
    tong_hop = tong_hop_chi_tieu(ds)
    if not tong_hop:
        print("Không có dữ liệu để phân tích.")
        return

    max_danh_muc = max(tong_hop.items(), key=lambda x: x[1])
    min_danh_muc = min(tong_hop.items(), key=lambda x: x[1])

    print(f"Danh mục chi tiêu lớn nhất: {max_danh_muc[0]} với số tiền: {max_danh_muc[1]}")
    print(f"Danh mục chi tiêu nhỏ nhất: {min_danh_muc[0]} với số tiền: {min_danh_muc[1]}")

# Vòng lặp chính
while True:
    menu()
    user = int(input("Chọn chức năng: "))

    if user == 0:
        print('Đã thoát chương trình.')
        break
    elif user == 1:
        them_khoan_chi_tiẽu()
    elif user == 2:
        hien_thi_chi_tieu()
    elif user == 3:
        tong_hop_chi_tieu(danh_sach_chi_tieu)
    elif user == 4:
        tim_kiem(danh_sach_chi_tieu)
    elif user == 5:
        xoa_chi_tieu(danh_sach_chi_tieu)
    elif user == 6:
        danh_muc_lon_nhat_nho_nhat(danh_sach_chi_tieu)
    else:
        print("Chức năng không hợp lệ, vui lòng thử lại!")
