#programming challenge 33
import random

def Choose(Choices):
    while True:
        out = input(f"Enter either rock, paper or scissors: ")
        out = out.lower()
        if out in Choices:
            return out

Results = {"rock":"scissors", "paper":"rock", "scissors":"paper"}
Choices = ["rock", "paper", "scissors"]

com = random.choice(Choices)
Player = Choose(Choices)

print(f"computer chose {com}")
print(f"player chose {Player}")

if Results[Player] == com:
    print("Player wins")
elif Results[com] == Player:
    print("computer wins")
else: 
    print("it's a draw")