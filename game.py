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
        self.game_over_status = "Game in progress"
        self.blackjack = False
        self.dealer_action = False

    def __str__(self):
        printed_text = f"Player Money: {self.player.money}"
        printed_text += f"\nPlayer Bet: {self.player.bet}"
        printed_text += "\nPlayer hand: "
        for c in self.player.hand:
            printed_text += f"{c} | "


        printed_text += f"\nPlayer score: {self.player.calculate_score()}"


        printed_text += "\nDealer hand: "
        for c in self.dealer.hand:
            printed_text += f"{c} | "

        printed_text += f"\nDealer score: {self.dealer.calculate_score()}"
        printed_text += f"\nGame over: {self.game_over}"
        printed_text += f"\nGame over status: {self.game_over_status}"

        return printed_text

    def start_round(self, bet):
        self.validate_bet(bet)

        self.game_over = False
        self.game_over_status = "Game in progress"
        self.blackjack = False
        self.dealer_action = False

        self.deck.create_deck()
        self.deck.shuffle()

        self.player.clear_hand()
        self.dealer.clear_hand()

        self.player.bet = bet
        self.player.money -= bet

        for _ in range(2):
            self.player.add_card(self.deck.draw_card())
            self.dealer.add_card(self.deck.draw_card())

        if self.has_blackjack():
            self.blackjack = True
            self.dealer_action = True

        self.game_over = self.check_game_over()

    def check_game_over(self):
        return self.player.calculate_score() > 21 or (self.dealer.calculate_score() >= 17 and self.dealer_action)

    def validate_bet(self, bet):
        if bet <= 0:
            raise ValueError("Bet must be greater than zero.")
        elif bet > self.player.money:
            raise ValueError("Not enough money.")

    def has_blackjack(self):
        return len(self.player.hand) == 2 and self.player.calculate_score() == 21

    def determine_winner(self):

        player_score = self.player.calculate_score()
        dealer_score = self.dealer.calculate_score()

        self.game_over = True

        if player_score == dealer_score:
            self.player.money += self.player.bet
            self.game_over_status = "Draw!"

        elif self.blackjack and player_score != dealer_score:
            self.player.money += 2.5 * self.player.bet
            self.game_over_status = "BLACKJACK!!!"

        elif player_score > 21:
            self.game_over_status = "Player Bust!"

        elif dealer_score > 21:
            self.player.money += 2 * self.player.bet
            self.game_over_status = "Dealer Bust!"

        elif player_score > dealer_score:
            self.player.money += 2 * self.player.bet
            self.game_over_status = "Player Won!"

        elif player_score < dealer_score:
            self.game_over_status = "Dealer Won!"

    def dealer_turn(self):
        self.dealer_action = True

        while self.dealer.calculate_score() < 17:
            self.dealer.add_card(self.deck.draw_card())

        self.game_over = self.check_game_over()
        self.determine_winner()

    def hit(self):
        if self.game_over or self.dealer_action:
            return

        self.player.add_card(self.deck.draw_card())

        self.game_over = self.check_game_over()

        if self.game_over:
            self.determine_winner()

    def stand(self):
        if self.game_over:
            return

        self.dealer_turn()


bj = BlackjackGame()
bj.start_round(50)
print(bj)
print("-----------------------------")
bj.hit()
print(bj)
print("-----------------------------")
bj.stand()
print(bj)
print("-----------------------------")


