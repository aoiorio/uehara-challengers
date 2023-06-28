import blackjack
from character import *
from abc import ABCMeta,abstractmethod

class PluginBase(metaclass=ABCMeta):

    def __init__(self,game: "blackjack.BlackJack"):
        self._game = game

    @abstractmethod
    def game_start(self) -> None:
        raise NotImplementedError()
    @abstractmethod
    def game_end(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def player_blackjack(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def player_win(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def player_draw(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def player_lose(self) -> None:
        raise NotImplementedError()


class NormalPlugin(PluginBase):

    def __init__(self, game: "blackjack.BlackJack"):
        super().__init__(game)

    def game_start(self) -> None:
        pass

    def game_end(self) -> None:
        continued = input("もう一回しますか？ y or n (default n): ")
        if continued == "y":
            self._game.start()

    def player_blackjack(self) -> None:
        pass

    def player_win(self) -> None:
        pass

    def player_draw(self) -> None:
        pass

    def player_lose(self) -> None:
        pass

class FivesPlugin(PluginBase):
    def __init__(self, game: "blackjack.BlackJack"):
        super().__init__(game)
        self.__wins = 0
        self.__loses = 0

    def game_start(self) -> None:
        print(f"You win = {self.__wins} , lose = {self.__loses}")
        print(f"あと{5-self.__wins}勝すればあなたの勝ちです!")
        print(f"そして{5-self.__loses}負するとあなたは負けます")

    def game_end(self) -> None:
        if self.__wins == 5:
            print("5回勝利したので終わりです")
            quit()
        if self.__loses == 5:
            print("5回敗北したので終わりです")
            quit()
        print("あと" + str(5-self.__wins) + "勝してください")
        self._game.start()

    def player_blackjack(self) -> None:
        self.__wins += 1
        print(f"{self.__wins}回目の勝利です！")

    def player_win(self) -> None:
        self.__wins += 1
        print(f"{self.__wins}回目の勝利です！")

    def player_draw(self) -> None:
        pass

    def player_lose(self) -> None:
        self.__loses += 1
        print(f"{self.__loses}回目の敗北です！")

class MoneyPlugin(PluginBase):
    def __init__(self, game: "blackjack.BlackJack"):
        super().__init__(game)
        self.__money = 10000


    def game_start(self) -> None:
        if self.__money == 0:
            print("あなたは金なしです！又のご来園を")
            quit()
        print(f'現在の所持金: {self.__money} 円')
        while True:
            bet = mod.get_int("何円掛けますか？ (一円以上): ")
            if 1 > bet:
                print("一円以上からしか掛けられません！")
                continue
            if bet > self.__money:
                print(f"所持金 {self.__money} 以上は掛けられません!")
                continue
            self.__bet = bet
            self.__money -= bet
            break

    def game_end(self) -> None:
        print(f"あなたの所持金は{self.__money}円です")
        continued = input("もう一回しますか？ y or n (default n): ")
        if continued == "y":
            self._game.start()

    def player_blackjack(self) -> None:
        print(str(self.__bet*1.5)+"円勝ちです")
        self.__money += self.__bet*2.5

    def player_win(self) -> None:
        print(f"{self.__bet}円勝ちです")
        self.__money += self.__bet*2

    def player_draw(self) -> None:
        print(f"ドローなので掛金{self.__bet}円が戻ってきました")
        self.__money += self.__bet

    def player_lose(self) -> None:
        print(f"{self.__bet}円失いました")
