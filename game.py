from deck import Deck
from player import Player
from dealer import Dealer
from settings import *


class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player = Player(STARTING_MONEY)
        self.dealer = Dealer()
        self.game_over = False

    def start_round(self):
        self.deck.create_deck()
        self.deck.shuffle()

        self.player.clear_hand()
        self.dealer.clear_hand()

        for _ in range(2):
            self.player.add_card(self.deck.draw_card())
            self.dealer.add_card(self.deck.draw_card())


bj = BlackjackGame()
bj.start_round()

for card in bj.player.hand:
    print(card)

for card in bj.dealer.hand:
    print(card)

print()

for card in bj.deck.cards:
    print(card)