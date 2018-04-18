class Card:
    def __init__(self, rank, suit, value=0):
        self.rank = rank
        self.suit = suit
        self.value = value

    def __str__(self):
        return '{} of {}'.format(self.rank, self.suit)

    def __repr__(self):
        return '{}-{}'.format(self.rank[:1], self.suit[:1])


if __name__ == '__main__':
    c1 = Card('Ace', 'Hearts', 1)
    c2 = Card('2', 'Clubs', 2)
    print(c1)
    print(c2)
