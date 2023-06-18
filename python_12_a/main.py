import random

# (1)
class RPSGame:
    def __init__(self, win_num, lose_num):
        self.win_num = win_num
        self.lose_num = lose_num

    def handsign(self, ene, hand):
        #勝敗
        if ene == "グー" and hand == "パー":
            print("あなたの勝ち！")
            self.win_num += 1
        elif ene == "グー" and hand == "チョキ":
            print("あなたの負け！")
            self.lose_num += 1
        elif ene == "パー" and hand == "チョキ":
            print("あなたの勝ち！")
            self.win_num += 1
        elif ene == "パー" and hand == "グー":
            print("あなたの負け！")
            self.lose_num += 1
        elif ene == "チョキ" and hand == "グー":
            print("あなたの勝ち！")
            self.win_num += 1
        elif ene == "チョキ" and hand == "パー":
            print("あなたの負け！")
            self.lose_num += 1
        else:
            print("あいこです！")

# (2)
class Enemy_Hand:
    def __init__(self, other):
        self.other = other
    def enemy_hand(self):
        
        if self.other == 1:
            self.other = "グー"
        elif self.other == 2:
            self.other = "チョキ"
        elif self.other == 3:
            self.other = "パー"
        print(self.other)

result = RPSGame(0, 0)
while True:
    # (3)
    print("じゃんけん！！")
    # ランダムな数字を獲得
    num = random.randrange(1, 4)
    enemy = Enemy_Hand(num)
    # (4)
    yours = input("グー or チョキ or パー を入力してください: ")
    # (5)
    enemy.enemy_hand()
    # (6)
    result.handsign(enemy.other, yours)
    # (7)
    print("あなたは今、" + str(result.win_num) + "回勝っています！")
    # (8)
    if result.win_num >= 3:
        print("3勝しました！！")
        break
        
