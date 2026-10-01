from player import Player


class Dealer(Player):
    def should_hit(self):
        if self.calculate_score() < 17:
            return True

        return False