#programming challenge 23 (expanded upon)

import random
import time

def EnterValue(Lower, Upper):
    while True:
        out = int(input(f"Enter a number between {Lower} and {Upper}: "))
        if out >= Lower and out <= Upper:
            return out

def BoolFlip(x: bool):
    return not x

Count = EnterValue(20, 30)
ComputerTurn = False
GameContinue = True
print("Determining who starts... ")
time.sleep(0.5)
if random.randint(0, 1) == 1:
    print("\nComputer starts!")
    ComputerTurn = True
else:
    print("\nPlayer starts!")

while GameContinue:
    if ComputerTurn == True:
        CurrentCount = Count
        print("\nComputer turn:")
        x = 3
        for i in range(Count -3, Count + 1):
            if i % 4 == 1:
                Count -= x
                break
            x -= 1
        if Count == CurrentCount:
            Count -= random.randint(1, 3)
    else:
        Count -= EnterValue(1, 3)
    print(f"\nCurrent count: {Count}")
    if Count <= 0:
        break
    ComputerTurn = BoolFlip(ComputerTurn)
    
if ComputerTurn:
    print("You win! congrats")
else:
    print("You lose. Git gud")