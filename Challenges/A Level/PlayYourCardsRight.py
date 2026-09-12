#programming challenge 37
import random

class Suit:
    Values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    def __init__(self, Suit):
        self.suit = Suit
        
    def DisplayCard(self, ValueIndex):
        print(f"{self.Values[ValueIndex]} of {self.suit}")
        
def Choose(Choices):
    while True:
        out = input(f"Higher or lower? (H/L)\n> ")
        out = out.lower()
        if out in Choices:
            return out
    
Hearts = Suit("Hearts")
Spades = Suit("Spades")
Clubs = Suit("Clubs")
Diamonds = Suit("Diamonds")

Deck = [Hearts, Spades, Clubs, Diamonds]

LastSuit = random.choice(Deck)
LastValue = random.randint(0, len(LastSuit.Values))
LastSuit.DisplayCard(LastValue)
points = 0

while True:
    Result = ""
    
    Selection = Choose(["h", "l"])
    SelectedSuit = random.choice(Deck)
    SelectedValue = random.randint(0, len(SelectedSuit.Values))
    SelectedSuit.DisplayCard(SelectedValue)
    
    if SelectedValue > LastValue:
        Result = "h"
    elif SelectedValue < LastValue:
        Result = "l"
        
    if Selection == Result:
        print("Correct")
    elif SelectedValue == LastValue:
        print("result is a draw. keep going")
    else:
        print("Incorrect.")
        break
    
    points += 1
    LastSuit = SelectedSuit
    LastValue = SelectedValue

print(f"Congrats!\nYou guessed {points} cards correctly!")