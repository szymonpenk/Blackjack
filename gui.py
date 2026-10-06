import tkinter as tk

from game import BlackjackGame
from settings import *

class BlackjackGUI:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()

        self.root.title("Blackjack")
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.resizable(False, False)

        self.create_widgets()

        self.root.mainloop()

    def create_widgets(self):
        tk.Label(self.root, text="Dealer").grid(row=0, column=0)

        tk.Label(self.root, text="As").grid(row=2, column=0)
        tk.Label(self.root, text="Ac").grid(row=2, column=1)

        tk.Label(self.root, text="Ks").grid(row=6, column=0)
        tk.Label(self.root, text="Ad").grid(row=6, column=1)

        tk.Label(self.root, text="Money: 450").grid(row=8, column=0)
        tk.Label(self.root, text="Bet: 50").grid(row=8, column=5)

        tk.Label(self.root, text="Player").grid(row=10, column=0)

        tk.Button(self.root, text="HIT", width=22).grid(row=12, column=0)
        tk.Button(self.root, text="STAND", width=22).grid(row=12, column=1)
        tk.Button(self.root, text="DOUBLE", width=22).grid(row=12, column=2)
        tk.Button(self.root, text="SPLIT", width=22).grid(row=12, column=3)


