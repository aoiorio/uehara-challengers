import mod

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
        return mod.convert(self.cards)    

class Dealer(Player):
    def get_name(self) -> str:
        return "ディーラー"
