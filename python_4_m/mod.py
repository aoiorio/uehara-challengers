def get_int():
    while True:
        try:
            s = input("数値を入力してください：")
            n = int(s)
            return n
        except ValueError:
            print("整数を入力してください。")


def prime_number(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    else:
        return True
