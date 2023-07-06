marks = ["Spade", "Heart", "Diamond", "Club"]
numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
cards = {}

for number in numbers:
    for mark in marks:
        cards.setdefault(number, mark) # todo [mark]を指定すると、ずっと同じmarkになってしまうので、次の値が新しいkeyで更新されない
print(cards) # cardでも同じ

# cards = {shape: mark for shape, mark in zip(marks, numbers)}

class Card:
    ranks = {}
    def dic(self):
        print("some stuff")