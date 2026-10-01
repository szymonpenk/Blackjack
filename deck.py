import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = []

    def create_deck(self):
        self.cards = [Card(suit, rank) for suit in ["Clubs", "Diamonds", "Hearts", "Spades"] for rank in [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop(random.randint(0,len(self.cards)-1))