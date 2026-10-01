class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

        if self.rank in ['Jack', 'Queen', 'King']:
            self.value = 10
        elif self.rank == 'Ace':
            self.value = 11
        else:
            self.value = int(rank)

    def __str__(self):
        return f'{self.rank} of {self.suit}'

