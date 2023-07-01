# (1)
max = input("お風呂の最大量を入力してください: ")
minute = input("毎分の水の量を入力してください: ")

top = 0

for i in range(1, int(max)+2):

    top += int(minute)
    print(str(i) + "分経ちました。お風呂の水の量は" + str(top) + "mlです")
    
    if top >= int(max):
        print("お風呂が満水になりました。あったかいうちにどうぞ")
        break
