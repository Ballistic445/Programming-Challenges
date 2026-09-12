#programming challenge 34
import random

def Choose(Choices):
    while True:
        out = input(f"Enter either rock, paper, scissors, lizard or spock: ")
        out = out.lower()
        if out in Choices:
            return out

Results = {"rock":["scissors", "lizard"], "paper":["rock", "spock"], "scissors":["paper", "lizard"], 
            "lizard":["paper", "spock"], "spock":["scissors", "rock"]}
Choices = ["rock", "paper", "scissors", "lizard", "spock"]

com = random.choice(Choices)
Player = Choose(Choices)

print(f"computer chose {com}")
print(f"player chose {Player}")

if com in Results[Player]:
    print("Player wins")
elif Player in Results[com]:
    print("computer wins")
else: 
    print("it's a draw")