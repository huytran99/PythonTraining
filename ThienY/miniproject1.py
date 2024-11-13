#buoc 1
print("đây là chương trình quản lídanh sách sinh viên và điểm số")
#buoc 2
def main():
    while True:
        print("1. thêm sinh viên mới và điểm số các môn học")
        print("2. danh sách sinh viên cuùng điểm số")
        print("3. điểm số trung bình của từng sinh viên")
        print("4. tìm kiếm sinh viên theo tên")
        print("5. cập nật hoc xóa thông tin sinh viên")
        choice = input("chọn chức năng: ")
#buoc 3
    listSV= []

    def nhapSinhVien(self):

        name = input("Nhap ten sinh vien: ")
        diemToan = float(input("Nhap diem toan: "))
        diemLy = float(input("Nhap diem Ly: "))
        diemHoa = float(input("Nhap diem Hoa: "))
        sv = SinhVien(name, diemToan, diemLy, diemHoa)
        self.tinhDTB(sv)
        self.listSinhVien.append(sv)





#buoc 6
# Hàm tính điểm TB cho sinh viên
class SinhVien:

    def __init__(self, name, diemToan, diemLy, diemHoa):
        self._name = name
        self._diemToan = diemToan
        self._diemLy = diemLy
        self._diemHoa = diemHoa
        self._diemTB = 0

def tinhDTB(self, sv:SinhVien):
    diemTB = (sv._diemToan + sv._diemLy + sv._diemHoa) / 3

#buoc 7
def findByName(self, keyword):
    listSV = []
    if (self.soLuongSinhVien() > 0):
        for sv in self.listSinhVien:
            if (keyword.upper() in sv._name.upper()):
                listSV.append(sv)
    return listSV

#buoc 9
def deletSV():
    print("*** XÓA SINH VIÊN ***")
    print("Nhập tên sinh viên cần xóa:")