from random import choice

class Card:
    suits = ["Spade", "Heart", "Diamond", "Club"]
    ranks = {
        "A": 1, "2": 2, "3": 3, "4": 4, "5": 5,
        "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
        "J": 10, "Q": 10, "K": 10 }

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self._get_value()

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def _get_value(self):
        return self.ranks[self.rank]

class CardGame(Card):

    def __init__(self, players, cards_per_player):
        self.players = players
        self.cards_per_player = cards_per_player


    def _create_deck(self):
        self.suits = Card.suits
        self.ranks = Card.ranks

    def _deal_cards(self):
        self.deck = [None] * self.players
        self.decks = {}

        for i in range(self.cards_per_player):
            for j in range(self.players):
                self.suit = choice(self.suits)
                self.rank = choice(list(self.ranks))

                self.deck[j] = [self.suit, self.rank]
            self.decks[i] = self.deck
        return self.decks


    def display_hands(self):
        return self._deal_cards()
    
cardGame = CardGame(4, 5)
display_hands = cardGame.display_hands()
print(display_hands)