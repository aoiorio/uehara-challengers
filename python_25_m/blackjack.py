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
                print("SELECT FIVES MODE")
                self.__plugin: "PluginBase" = FivesPlugin(self)
            case "m":
                print("SELECT MONEY MODE")
                self.__plugin: "PluginBase" = MoneyPlugin(self)
            case _:
                print("SELECT NORMAL MODE")
                self.__plugin: "PluginBase" = NormalPlugin(self)
        self.start()

    def arg_init(self):
        self.__tiles:list[str] = []
        for _ in range(4):
            self.__tiles.extend(["1","2","3","4","5","6","7","8","9","10","K","Q","J"])
        self.__player = Player()
        self.__dealer = Dealer()
        for human in [self.__player,self.__dealer]:
            for _ in range(2):
                self.hit(human)

    def start(self):
        self.arg_init()
        print("======== BLACK JACK START ========")
        self.__plugin.game_start()
        player = self.__player
        dealer = self.__dealer
        print("=====CARDS=====")
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
            self.__plugin.player_draw()
        elif num_p > 21:
            print("バースト負けです!")
            self.__plugin.player_lose()
        elif num_d > 21:
            print("ディーラーがバーストしました")
            print("あなたの勝ちです")
            self.__plugin.player_win()
        elif num_d == num_p:
            print("引き分けです")
            self.__plugin.player_draw()
        elif num_d > num_p:
            print("あなたの負けです")
            self.__plugin.player_lose()
        else:
            if num_p == 21:
                print("BLACKJACKでの勝ちです")
                self.__plugin.player_blackjack()
            else:
                print("あなたの勝ちです")
                self.__plugin.player_win()
        print("======== BLACK JACK END ========")
        time.sleep(1)
        self.__plugin.game_end()
            
    def hit(self,human:Player):
        human.hit(self.__tiles.pop(random.randint(0,len(self.__tiles)-1)))
