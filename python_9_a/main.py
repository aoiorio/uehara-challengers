# (1)
string = input("文字を入力してください: ")
reversed_string = string[::-1]

if string == reversed_string:
    print(string + "は上から読んでも下から読んでも同じ！！ 面白いね！！")

# (2)
import random

random_num = random.randrange(0, 100)

if random_num >= 80:
    print("優")
elif 60 <= random_num < 80:
    print("良")
else:
    print("可")
