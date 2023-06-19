def get_int(string: str):
    while True:
        try:
            s = input(string)
            n = int(s)
            return n
        except ValueError:
            print("整数を入力してください。")


def select_list(array: list):
    length = len(array)
    map = dict(zip([i for i in range(1,length+1)], array))
    while True:
        number = get_int(str(map) + " から選んでください: ")
        if number in map:
            return map.get(number)

def get_int_list():
    list = []
    while True:
        n = None
        while True:
            try:
                s = input("整数を入力してください " + str(list) + "(cで終了): ")
                if s == "c":
                    return list
                n = int(s)
                break
            except ValueError:
                print("整数を入力してください。")
        list.append(n)
