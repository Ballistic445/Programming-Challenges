#programming challenge 36
import random

class Suit:
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    def __init__(self, Suit):
        self.suit = Suit
        
    def DisplayCard(self, Value):
        print(f"{Value} of {self.suit}")
    
Hearts = Suit("Hearts")
Spades = Suit("Spades")
Clubs = Suit("Clubs")
Diamonds = Suit("Diamonds")

Deck = [Hearts, Spades, Clubs, Diamonds]
SelectedSuit = random.choice(Deck)
SelectedSuit.DisplayCard(random.choice(SelectedSuit.values))