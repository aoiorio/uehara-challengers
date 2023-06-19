def get_int(string: str):
    while True:
        try:
            s = input(string)
            n = int(s)
            return n
        except ValueError:
            print("整数を入力してください。")

