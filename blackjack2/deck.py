from card import Card
from random import shuffle


class Deck:
    RANK_VALUE = {
        'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
        '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10
    }
    SUITS = ['Diamonds', 'Hearts', 'Spades', 'Clubs']

    def __init__(self, number_decks=1):
        self.number_decks = number_decks
        self.hopper = self.generate_deck()
        self.shuffle()

    def generate_deck(self):
        decks = []
        for i in range(self.number_decks):
            for s in self.SUITS:
                for r, v in self.RANK_VALUE.items():
                    decks.append(Card(s, r, v))
        return decks

    def shuffle(self):
        shuffle(self.hopper)

    def deal_card(self):
        return self.hopper.pop(0)


if __name__ == '__main__':
    deck = Deck()
    for c in deck.hopper:
        print(c)
    print(deck.hopper)