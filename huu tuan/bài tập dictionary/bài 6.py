# 6. Converting Strings into Dictionary
# Bài tập:
# Cho chuỗi JSON '{"name": "Huy", "age": 25, "city": "Hanoi"}'.
# Viết chương trình để:
# Chuyển chuỗi này thành một dictionary bằng thư viện json.
# Thay đổi giá trị của "age" thành 30.
# Chuyển dictionary trở lại thành chuỗi JSON và in ra
import json

json_str = '{"name": "Huy", "age": 25, "city": "Hanoi"}'

json_dict = json.loads(json_str)

json_dict['age'] = 30

json_str_1 = json.dumps(json_dict)
print(json_str_1)