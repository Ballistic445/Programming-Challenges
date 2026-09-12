#programming challenge 35
import random

def EnterValue(Lower, Upper):
    while True:
        out = int(input(f"\nGuess the number (between {Lower} and {Upper}): "))
        if out >= Lower and out <= Upper:
            return out

Num = random.randint(1, 1000)
Tries = 0

print("Computer has chosen a number between 1 and 1000 inclusive. guess that number")

while True:
    guess = EnterValue(1, 1000)
    if guess > Num:
        print("number is lower than guess")
    elif guess < Num:
        print("number is greater than guess")
    else: break
    Tries += 1
    
print(f"Congratulations!\nYou took {Tries} tries to guess the number.")