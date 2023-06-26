import random
import time
from character import *
from plugin import *

class BlackJack():
    def __init__(self) -> None:
        print("n NORMAL: 普通のBLACKJACKをプレイします")
        print("f FIVES: 五勝するまで終われま戦")
        print("m MONEY: 配当できるようになります")
        select = input("[n] or [f] or [m] (default n): ")
        match select:
            case "f":
                print("555555 FIVES MODE 555555")
                self.plugin: "PluginBase" = FivesPlugin(self)
            case "m":
                print("%%%%%% MONEY MODE %%%%%%%")
                self.plugin: "PluginBase" = MoneyPlugin(self)
            case _:
                print("nnnnnn NORMAL MODE nnnnnnn")
                self.plugin: "PluginBase" = NormalPlugin(self)
        self.start()

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
        print("======== BLACK JACK START ========")
        self.plugin.game_start()
        player = self.player
        dealer = self.dealer
        player.print(False)
        dealer.print(True)
        time.sleep(1)
        print("=====プレイヤー=====")
        if player.get_number() == 21:
            print("==!! BLACK JACK !!==")
        else:
            while True:
                string = input("== hitしますか？ h or s (default s): ")
                if string == "h":
                    self.hit(player)
                    player.print(False)
                    dealer.print(True)
                    num = player.get_number()
                    if num > 21:
                        print("== あなたのバースト! ==")
                        break
                    if num == 21:
                        print("==!! BLACK JACK !!==")
                        break
                    time.sleep(1)
                    continue
                break
        print("=====ディーラー====")
        time.sleep(1)
        dealer.print(False)
        if dealer.get_number() < 17:
            print("==ディーラーがカードを引きます==")
            while True:
                time.sleep(1)
                if dealer.get_number() >= 17:
                    break
                self.hit(dealer)
                dealer.print(False)
        print("=====勝敗=====")
        time.sleep(1)
        num_d = dealer.get_number()
        num_p = player.get_number()
        if num_p > 21 and num_d > 21:
            print("どちらもバーストです！引き分け")
            self.plugin.player_draw()
        elif num_p > 21:
            print("バースト負けです!")
            self.plugin.player_lose()
        elif num_d > 21:
            print("ディーラーがバーストしました")
            print("あなたの勝ちです")
            self.plugin.player_win()
        elif num_d == num_p:
            print("引き分けです")
            self.plugin.player_draw()
        elif num_d > num_p:
            print("あなたの負けです")
            self.plugin.player_lose()
        else:
            if num_p == 21:
                print("BLACKJACKでの勝ちです")
                self.plugin.player_blackjack()
            else:
                print("あなたの勝ちです")
                self.plugin.player_win()
        print("======== BLACK JACK END ========")
        time.sleep(1)
        self.plugin.game_end()
            
    def hit(self,human:Player):
        human.hit(self.tiles.pop(random.randint(0,len(self.tiles)-1)))
