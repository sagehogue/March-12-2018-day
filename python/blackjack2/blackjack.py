from deck import Deck
from hand import Hand, DealerHand
import os
import time

class BlackJack:
    def __init__(self, num_decks=6):
        self.players = self.get_players()
        self.dealer = DealerHand()
        self.deck = Deck(num_decks)
        self.initial_deal()
        self.run()

    def get_players(self):
        players = []
        num = int(input('How many players are there?: '))
        for i in range(num):
            players.append(Hand(input('Player {}, what is your name?: '.format(i + 1)),
                                int(input('How much money are do you have?: '))))
        return players

    def initial_deal(self):
        for two in range(2):
            for i in self.players:
                i.take_card(self.deck.deal_card())
            self.dealer.take_card(self.deck.deal_card())

    def find_wins(self):
        response = {'win': [], 'push': []}
        for p in self.players:
            if self.dealer.hand_value < p.hand_value <= 21:
                response['winners'].append(p)
            elif p.hand_value == self.dealer.hand_value:
                response['push'].append(p)
            return response

    def run(self):
        while True:
            for p in self.players:
                while True:
                    # os.system('cls' if os.name == 'nt' else 'clear')
                    print('*' * 50)
                    print(self.dealer.name)
                    print(self.dealer)
                    print('*' * 50)
                    print('*' * 50)
                    print(p)
                    print(p.hand_value)
                    query = input("{} do you wish to (h)it or (s)tay?: ".format(p.name)).lower()
                    if query == 'h':
                        bust = p.take_card(self.deck.deal_card())
                        print(p.hand_value)
                        print(bust)
                        if bust:
                            print('{} busted!'.format(p.name))
                            time.sleep(1)
                            break
                    elif query == 's':
                        break
                    else:
                        print('I did not understand that.')

            self.dealer.dealer_turn(self.deck)
            print(self.find_wins())


if __name__ == '__main__':
    blackjack = BlackJack()
