class Card:
    def __init__(self, suit, rank, value=0):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return '{} of {}'.format(self.rank, self.suit)

    def __repr__(self):
        return '{}-{}'.format(self.rank[0], self.suit[0])


if __name__ == '__main__':
    c1 = Card('Hearts', 'Ace', 1)
    print(c1.value)

