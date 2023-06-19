import math
from mod import get_int

height = get_int("身長(cm)を入力してください: ")
weight = get_int("体重(kg)を入力してください: ")

m = height/100
BMI = weight/math.pow(m,m)
print("BMI=",BMI)
string = ""
if 18.5 > BMI:
    string = "低体重"
elif 25.0 > BMI:
    string = "普通体重"
elif 30.0 > BMI:
    string = "肥満(1度)"
elif 35.0 > BMI:
    string = "肥満(2度)"
elif 40.0 > BMI:
    string = "肥満(3度)"
else:
    string = "肥満(4度)"
print(string,"です。")
