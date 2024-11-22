# Cho danh sách keys = ["id", "name", "age"] và values = [101, "Huy", 25].
# Viết chương trình chuyển hai danh sách này thành một dictionary bằng zip().
# Sau đó, thêm một key mới "city" với giá trị "Hà Nội" và in ra dictionary cuối cùng.

keys = ["id", "name", "age"]
values = [101, "Huy", 25]

my_dict = dict(zip(keys, values))

my_dict['city'] = 'ha nội'

print(my_dict)