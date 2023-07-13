import random

class Card:
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    ranks = {
        "Ace": 1, "2": 2, "3": 3, "4": 4, "5": 5,
        "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
        "Jack": 10, "Queen": 10, "King": 10
    }

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self._get_value()

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def _get_value(self):
        return self.ranks[self.rank]


class CardGame:
    def __init__(self, players, cards_per_player):
        self.players = players
        self.cards_per_player = cards_per_player
        self.deck = self._create_deck()
        self.hands = self._deal_cards()

    def _create_deck(self):
        deck = []
        for suit in Card.suits:
            for rank in Card.ranks:
                card = Card(suit, rank)
                deck.append(card)
        return deck

    def _deal_cards(self):
        hands = []
        for _ in range(self.players):
            random.shuffle(self.deck)
            hand = []
            for j in range(self.cards_per_player):
                hand.append(self.deck[j])
            hands.append(hand)
        return hands

    def display_hands(self):
        for i, hand in enumerate(self.hands):
            print(f"Player {i+1} Hand:")
            for card in hand:
                print(card)
            print()


# ゲームの設定
players = 100 # プレイヤー数
cards_per_player = 3  # 1人あたりのカード数

# ゲームの開始
game = CardGame(players, cards_per_player)
game.display_hands()