import random

win_num = 0
lose_num = 0

while True:
    # 自分の手
    print("じゃんけん")
    hand = input("グーかチョキかパーを選んで入力してください：")
    # 敵の手
    enemy_hand = random.randrange(1, 4)
    if enemy_hand == 1:
        enemy_hand = "グー"
    elif enemy_hand == 2:
        enemy_hand = "チョキ"
    elif enemy_hand == 3:
        enemy_hand = "パー"
    print("敵の手は" + enemy_hand + "です")
    # 勝敗
    if enemy_hand == "グー" and hand == "パー":
        print("あなたの勝ち！")
        win_num += 1
    elif enemy_hand == "グー" and hand == "チョキ":
        print("あなたの負け！")
        lose_num += 1
    elif enemy_hand == "パー" and hand == "チョキ":
        print("あなたの勝ち！")
        win_num += 1
    elif enemy_hand == "パー" and hand == "グー":
        print("あなたの負け！")
        lose_num += 1
    elif enemy_hand == "チョキ" and hand == "グー":
        print("あなたの勝ち！")
        win_num += 1
    elif enemy_hand == "チョキ" and hand == "パー":
        print("あなたの負け！")
        lose_num += 1
    else:
        print("あいこです！")
    print("合計勝利数: " + str(win_num) )
    print("合計敗北数: " + str(lose_num))
    print("勝率は" + str(win_num / (win_num + lose_num)) + "%です")
    go = input("もう一度じゃんけんをしますか？　はい or いいえ: ")
    if go == "はい":
        continue
    elif go == "いいえ":
        break
