# Viết hàm tinh_bmi nhận vào cân nặng và chiều cao, trả về chỉ số BMI.
# Nếu BMI > 25 trả về “Thừa cân”. Nếu 18.5 < BMI <= 25 thì trả về “Bình thường”, nếu BMI <= 18.5 thì trả về “Thiếu cân”

# Viết hàm tinh_bmi nhận vào cân nặng và chiều cao
def tinh_bmi(can_nang, chieu_cao):

    # công thức tính BMI
    bmi = can_nang / chieu_cao ** 2

    # nếu bmi lớn hơn 25 thì sẽ trả về "thừa cân"
    if bmi > 25:
        return 'thừa cân'

    # nếu bmi năm trong khoảng 18.5 đến 25 thì sẽ trả về "bình thường"
    elif 18.5 < bmi <= 25:
        return 'bình thường'

    # nếu bmi bé hơn hoạc bằng 18.5 thì sẽ trả về "thiếu cân"
    elif bmi <= 18.5:
        return 'thiếu cân'

# gọi hàm và truyền tham số
bmi = tinh_bmi(70, 1.75)
print(bmi)