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
        self.blackjack = False

    def start_round(self, bet):
        self.deck.create_deck()
        self.deck.shuffle()

        self.player.clear_hand()
        self.dealer.clear_hand()

        self.player.bet = bet
        self.player.money -= bet

        for _ in range(2):
            self.player.add_card(self.deck.draw_card())
            self.dealer.add_card(self.deck.draw_card())

        if self.player.calculate_score() == 21:
            self.blackjack = True
            

    def determine_winner(self):
        player_score = self.player.calculate_score()
        dealer_score = self.dealer.calculate_score()

        self.game_over = True

        if player_score > 21:
            pass

        elif dealer_score > 21 or player_score > dealer_score:
            self.player.money += 2 * self.player.bet

        elif player_score < dealer_score:
            pass

        elif player_score == dealer_score:
            self.player.money += self.player.bet






bj = BlackjackGame()
bj.start_round()

for card in bj.player.hand:
    print(card)

for card in bj.dealer.hand:
    print(card)

print()

for card in bj.deck.cards:
    print(card)