class Hand:
    def __init__(self, name, money):
        self.name = name
        self.hand = []
        self.hand_value = 0
        self.bet = 0
        self.money = money

    def take_card(self, card):
        self.hand.append(card)
        self.score_hand()
        if self.hand_value <= 21:
            return False
        return True

    def score_hand(self):
        self.hand_value = 0
        ace = False
        for c in self.hand:
            if c.value == 1:
                ace = True
            self.hand_value += c.value
        if ace and self.hand_value + 10 <= 21:
            self.hand_value += 10

    def take_money(self, amt):
        self.money += amt

    def bet_amt(self, amt):
        if self.money - amt > 0:
            self.bet = amt
            self.money -= amt
            return amt
        else:
            return 0

    def clear_hand(self):
        self.bet = 0
        self.hand = []
        self.hand_value = 0

    def __str__(self):
        string = ''
        if self.hand:
            for c in self.hand:
                string += '| {} |'.format(c)
            return string
        return '||  ||'

    def __repr__(self):
        return self.__str__()


class DealerHand(Hand):
    def __init__(self):
        super().__init__("Dealer", 10000000000000000)

    def dealer_turn(self, deck):
        while self.hand_value <= 16:
            bust = self.take_card(deck.deal_card())
            if bust:
                break


if __name__ == '__main__':
    from card import Card

    h1 = Hand('Test1', 1000)
    h2 = Hand('Test2', 2000)
    ace = Card('Hearts', 'Ace', 1)
    ten = Card('Hearts', '10', 10)
    two = Card('Hearts', '2', 2)
    eight = Card('Hearts', '8', 8)
    h1.take_card(ace)
    h1.take_card(ace)
    h1.take_card(ten)
    h1.take_card(ten)
    h1.score_hand()
    print(h1)
    print(h2)

    # h1.take_card(two)
    # h1.score_hand()
    # print(h1.hand_value)
