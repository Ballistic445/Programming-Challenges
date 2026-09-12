#programming challenge 39
import random

class Suit:
    Values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    def __init__(self, Suit):
        self.suit = Suit
        HasBeenPlayed = [False for i in self.Values]
        self.Values = [list(i) for i in zip(self.Values, HasBeenPlayed)]
        
    def DisplayCard(self, ValueIndex):
        print(f"{self.Values[ValueIndex][0]} of {self.suit}")
        
def Choose(Choices):
    while True:
        out = input(f"Higher or lower? (H/L)\n> ")
        out = out.lower()
        if out in Choices:
            return out
        
def ChooseCard():
    while True:
        Suit = random.choice(Deck)
        Value = random.randint(0, len(Suit.Values) - 1)
        if Suit.Values[Value][1] == False:
            Suit.Values[Value][1] = True
            return Suit, Value

def ResetDeck(Deck):
    for i in Deck:
        for j in i.Values:
            j[1] = False
            
def CardsCanBePlayed(Deck):
    for i in Deck:
        for j in i.Values:
            if j[1] == False:
                return True
    return False

Hearts = Suit("Hearts")
Spades = Suit("Spades")
Clubs = Suit("Clubs")
Diamonds = Suit("Diamonds")

Deck = [Hearts, Spades, Clubs, Diamonds]

LastSuit, LastValue = ChooseCard()
LastSuit.DisplayCard(LastValue)
points = 0

while True:
    Result = ""
    
    if not CardsCanBePlayed(Deck):
        print("Deck has been cleared. \n+10 points. \nResetting deck...")
        points += 10
        ResetDeck(Deck)
    
    Selection = Choose(["h", "l"])
    SelectedSuit, SelectedValue = ChooseCard()
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

print(f"Congrats!\nYou got {points} points!")