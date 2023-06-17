def get_int():
    while True:
        try:
            s = input("数値を入力してください：")
            n = int(s)
            return n
        except ValueError:
            print("整数を入力してください。")
