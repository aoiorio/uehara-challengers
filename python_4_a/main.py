while True:
    integer = input("数値を入力してください: ")
    if not integer.isdigit():
        print("整数を入力してください")
        continue
    else:
        integer = int(integer)
        break

count = 0
for i in range(1, 10):
    if integer % i == 0:
        count += 1

if count <= 2:
    print(str(integer) + "は素数です")
else:
    print(str(integer) + "は素数ではありません")