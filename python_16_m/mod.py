import random
from enum import Enum
from typing import cast

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
    map = dict(zip([i for i in range(1,length+1)], [hand.get_hand() for hand in array]))
    while True:
        number = get_int(str(map) + "から選んでください: ")
        if number in map:
            return array[number-1]


class Hand(Enum):
    Rock = "グー"
    Paper = "パー"
    Scissors = "チョキ"

    def __init__(self,string: str) -> None:
        self.__hand = string

    def get_hand(self) -> str:
        return self.__hand
    
    # 0があいこで、1が勝ち、2が負け です。
    def diff(self, other:"Hand") -> int:
        number = 0
        hand = self.get_hand()
        enemy = other.get_hand()
        if self == other:
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
        return number

class RSPGame():
    hands = [Hand.Rock,Hand.Paper,Hand.Scissors]

    def __init__(self) -> None:
        self.__win_len = 0
        self.__lose_len = 0
        self.__equals_len = 0

    def start(self):

        while True:
            print("じゃんけん")
            hand = cast(Hand,select_list(RSPGame.hands))
            enemy = random.choice(RSPGame.hands)
            print("あなたは",hand.get_hand(),"を出しました。")
            print("相手は",enemy.get_hand(),"をしました。")
            number = hand.diff(enemy)
            if number == 0:
                print("あいこです。")
                self.__equals_len += 1
            elif number == 1:
                print("あなたの勝ちです。")
                self.__win_len += 1
            else:
                print("あなたの負けです。")
                self.__lose_len += 1
            print("勝利数=",str(self.__win_len),"敗北数=",str(self.__lose_len),"あいこ数",str(self.__equals_len))
            next = input("もう一度じゃんけんをしますか？y or n (default n) ")
            if next == "y":
                continue
            else:
                break
