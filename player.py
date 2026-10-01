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


p = Player(10)
