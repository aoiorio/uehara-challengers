# 【ルール】
# 対戦方法：DealerとPlayerの1対1の対戦ゲーム
#   i）Playerに2枚のカードを配る（一枚は表示・もう一枚は表示しない）
#   ⅱ）Dealerにも2枚カードを配る（Playerと同様）
#   ⅲ）Playerは、両方のカードを確認する。　
#       合計数値が16より小さい　→　もう一枚必ず引く
#       合計数値が16以上　　　　→　引く(hit)［もう一枚もらう］か引かない（stand）
#                                を決めてコールする。
#       hitのコールの限り、カードを引き続ける
#   ⅳ）Playerが終了後、ディーラも同様にカードを引く
#   ⅴ）同時に開いて21に近いほうが勝ち
#   21の場合はBLACK JACKと表示
#   ※  K・Q・Jは10とカウントする。Aは1または11を選択することが出来る
#   ※ カードが21を超えてしまうと、その時点で負けとなる。
#   ※ 最初に配られた2枚のカードが　”Aと10点札”　で21点が完成していた場合は
#    『BLACK JACK』となりその時点で勝ちとなる。
#   ※ 配当がある場合は、配当は3 to 2（1.5倍）となる。
#   ただし、カジノディーラーもブラックジャックだった場合は引き分けとなる。


# 【拡張機能】
#   1）どちらかが5勝したほうが勝ちで、ゲーム終了とする。
#   2）配当（持ち金をかけられるようにする）
import random

def convert(cards:list) -> int:
    total = 0
    ones = 0
    for card in cards:
        match card:
            case 'K' | 'Q' | 'J':
                total += 10
                continue
        num = int(card)
        if num == 1:
            ones += 1
        else:
            total += num
    for _ in range(ones):
        ones -=1
        if total >= 11:
            total += 1
        elif ones == 0:
            total += 11
        elif (10-ones) >= total:
            total += 11
        else:
            total += 1
    return total

class Player():

    def __init__(self) -> None:
        self.cards = []

    def print(self,show:bool):
        print(self.get_name(),"の手札",end=": ")
        for i,v in enumerate(self.cards):
            if show:
                print(v if i != 0 else "#",end=" ,")
            else:
                print(v,end=" ,")
        if show:
            print()
        else:
            print("合計値:",self.get_number())

    def get_name(self) -> str:
        return "プレイヤー"

    def hit(self,card:str):
        self.cards.append(card)

    def get_number(self):
        return convert(self.cards)    

class Dealer(Player):
    def get_name(self) -> str:
        return "ディーラー"
        
class BlackJack():
    def arg_init(self):
        self.tiles:list[str] = []
        for _ in range(4):
            self.tiles.extend(["1","2","3","4","5","6","7","8","9","10","K","Q","J"])
        self.player = Player()
        self.dealer = Dealer()
        for human in [self.player,self.dealer]:
            for _ in range(2):
                self.hit(human)

    def start(self):
        self.arg_init()
        print("===== BLACK JACK START =====")
        player = self.player
        dealer = self.dealer
        player.print(False)
        dealer.print(True)
        print("=====プレイヤー=====")
        while True:
            # while True:
            #     if 16 <= player.get_number():
            #         break
            #     self.hit(player)
            # ここで16未満は16以上まで引く
            string = input("==hitしますか？ h or s (default s): ")
            if string == "h":
                self.hit(player)
                player.print(False)
                dealer.print(True)
                num = player.get_number()
                if num > 21:
                    print("=== あなたのバースト! 負けです!")
                    dealer.print(False)
                    return
                if num == 21:
                    print("!! BLACK JACK !!")
                    break
                continue
            print("=====ディーラー====")
            break
        dealer.print(False)
        if dealer.get_number() < 17:
            print("===ディーラーがカードを引きます===")
            while True:
                if dealer.get_number() >= 17:
                    break
                self.hit(dealer)
                dealer.print(False)
        print("===勝敗===")
        num_d = dealer.get_number()
        num_p = player.get_number()
        if num_d > 21:
            print("ディーラーがバーストしました")
            print("あなたの勝ちです")
        elif num_d == num_p:
            print("引き分けです")
        elif num_d > num_p:
            print("あなたの負けです")
        else:
            print("あなたの勝ちです")
            
    def hit(self,human:Player):
        human.hit(self.tiles.pop(random.randint(0,len(self.tiles)-1)))

BlackJack().start()
