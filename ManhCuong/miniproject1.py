students = {}  # Từ điển để lưu thông tin sinh viên


def add_student():
   sv_id = input('Nhập mã sinh viên: ')
   name = input('Nhập họ tên sinh viên: ')
   scores = []
   for i in range(3):  # Nhập điểm cho 3 môn
       while True:  # Lặp lại cho đến khi nhập đúng
           try:
               score = float(input(f'Nhập điểm môn {i + 1}: '))
               scores.append(score)  # Thêm điểm vào danh sách
               break  # Thoát khỏi vòng lặp nếu nhập thành công
           except ValueError:
               print('Điểm không hợp lệ. Vui lòng nhập lại.')
   students[sv_id] = {'name': name, 'scores': scores}  # Lưu thông tin sinh viên
   print('Đã thêm sinh viên.')


def view_students():
   if not students:  # Kiểm tra nếu không có sinh viên nào
       print('Không có sinh viên nào.')
       return
   for sv_id, info in students.items():
       avg_score = sum(info['scores']) / len(info['scores']) if info['scores'] else 0  # Tính điểm trung bình
       print(f'Mã SV: {sv_id}, Họ tên: {info["name"]}, Điểm: {info["scores"]}, Điểm TB: {avg_score:.2f}')


def update_scores():
   sv_id = input('Nhập mã sinh viên cần cập nhật điểm: ')
   if sv_id in students:  # Kiểm tra sinh viên có trong danh sách không
       scores = []
       for i in range(3):  # Nhập điểm cho 3 môn
           while True:  # Lặp lại cho đến khi nhập đúng
               try:
                   score = float(input(f'Nhập điểm môn {i + 1}: '))
                   scores.append(score)  # Thêm điểm vào danh sách
                   break  # Thoát khỏi vòng lặp nếu nhập thành công
               except ValueError:
                   print('Điểm không hợp lệ. Vui lòng nhập lại.')
       students[sv_id]['scores'] = scores  # Cập nhật điểm
       print('Đã cập nhật điểm.')
   else:
       print('Không tìm thấy sinh viên.')


def delete_student():
   sv_id = input('Nhập mã sinh viên cần xóa: ')
   if sv_id in students:  # Kiểm tra sinh viên có trong danh sách không
       del students[sv_id]  # Xóa sinh viên
       print('Đã xóa sinh viên.')
   else:
       print('Không tìm thấy sinh viên.')


def main():
   while True:
       print('''\nChào bạn! Mời bạn chọn chức năng:
       0 - Thoát
       1 - Thêm sinh viên
       2 - Xem danh sách sinh viên
       3 - Cập nhật điểm sinh viên
       4 - Xóa sinh viên
       ''')
       choice = input('Nhập lựa chọn: ')
       if choice == '0':
           break
       elif choice == '1':
           add_student()
       elif choice == '2':
           view_students()
       elif choice == '3':
           update_scores()
       elif choice == '4':
           delete_student()
       else:
           print('Lựa chọn không hợp lệ.')


if __name__ == '__main__':
   main()
