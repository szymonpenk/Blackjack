from card import Card


class Player:
    def __init__(self, money = 0):
        self.hand = []
        self.money = money
        self.bet = 0

    def add_card(self, card):
        self.hand.append(card)

    def calculate_score(self):
        values = [card.value for card in self.hand]
        values.sort()

        score = 0
        for value in values:
            score += value

            if score > 21 and value == 11:
                score -= 10

        return score

    def clear_hand(self):
        self.hand = []

    def has_blackjack(self):
        return len(self.hand) == 2 and self.calculate_score() == 21


p = Player(10)
