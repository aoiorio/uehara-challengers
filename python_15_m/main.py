import random
from mod import get_int

win_len = 0
lose_len = 0
equals_len = 0

def select_list(array: list):
    length = len(array)
    map = dict(zip([i for i in range(1,length+1)], array))
    while True:
        number = get_int(str(map) + "から選んでください: ")
        if number in map:
            return map.get(number)

hands = ["パー", "チョキ", "グー"]
while True:
    print("じゃんけん")
    hand = select_list(hands)
    enemy = random.choice(hands)
    print("あなたは",hand,"を出しました。")
    print("相手は",enemy,"を出しました。")
    # 0があいこで、1が勝ち、2が負け です。
    number = 0
    if hand == enemy:
        pass
    elif hand == "パー":
        if enemy == "チョキ":
            number = -1
        else:
            number = 1
    elif hand == "チョキ":
        if enemy == "パー":
            number = 1
        else:
            number = -1
    else:
        if enemy == "チョキ":
            number = 1
        else:
            number = -1
    if number == 0:
        print("あいこです。")
        equals_len += 1
    elif number == 1:
        print("あなたの勝ちです。")
        win_len += 1
    else:
        print("あなたの負けです。")
        lose_len += 1
    print("勝利数=",str(win_len),"敗北数=",str(lose_len),"あいこ数",str(equals_len))
    next = input("もう一度じゃんけんをしますか？y or n (default n) ")
    if next == "y":
        continue
    else:
        break
