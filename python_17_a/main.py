marks = ["Spade", "Heart", "Diamond", "Club"]
numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
cards = {}

# for number in numbers:
#     for mark in marks:
#         cards[number] = mark # todo [mark]を指定すると、ずっと同じmarkになってしまうので、次の値が新しいkeyで更新されない
# # print(cards) # cardでも同じ

# cards = {shape: mark for shape, mark in zip(marks, numbers)}

class Card:
    
    def __init__(self, ranks):
        self.__ranks = ranks
    def dic(self):
        for m in marks:
            for n in numbers:
                if n == "A":
                    self.__ranks['1'] = m
                elif n == "J" or n == "Q" or n == "K":
                    self.__ranks[10] = m
                else:
                    self.__ranks[n] = m
        

    def _get_value(self):
        return self.__ranks
    

card = Card(cards)
card.dic()
print(card._get_value())