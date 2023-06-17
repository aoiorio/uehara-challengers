def get_int(string):
    while True:
        try:
            s = input(string + "の整数を入力してください：")
            n = int(s)
            return n
        except ValueError:
            print("整数を入力してください。")
