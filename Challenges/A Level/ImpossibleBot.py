#programming challenge 23 (expanded upon)

import random
import time

#repeatedly asks user to enter value until value is valid
def EnterValue(Lower, Upper):
    while True:
        out = int(input(f"Enter a number between {Lower} and {Upper}: "))
        if out >= Lower and out <= Upper:
            return out

#returns opposite of entered boolean
def BoolFlip(x: bool):
    return not x

ImpossibleBot = False
setting = input("Do you want to play against the Easy bot? (y/n) \n>")
if setting.lower() == "n":
    print("Playing impossible bot...\n")
    ImpossibleBot = True
else:
    print("Playing easy bot...\n")

#init values
Count = EnterValue(20, 30)
ComputerTurn = False
GameContinue = True

#random selection of who starts
print("Determining who starts... ")
time.sleep(0.5)
if random.randint(0, 1) == 1:
    print("\nComputer starts!")
    ComputerTurn = True
else:
    print("\nPlayer starts!")

#game loop
while GameContinue:
    if ComputerTurn == True:
        CurrentCount = Count
        print("\nComputer turn:")
        x = 3
        #if the bot can reduce the number to one more than a factor of 4 it will
        if ImpossibleBot == True:
            for i in range(Count -3, Count + 1):
                if i % 4 == 1:
                    Count -= x
                    break
                x -= 1
        #if it can't it just reduces by random. This is the only option for easy mode
        if Count == CurrentCount:
            Count -= random.randint(1, 3)
    #user enters a value between 1 and 3
    else:
        Count -= EnterValue(1, 3)
    print(f"\nCurrent count: {Count}")
    #checks if game needs to stop
    if Count <= 0:
        break
    ComputerTurn = BoolFlip(ComputerTurn)
    
#checks who wins
if ComputerTurn:
    print("You win! congrats")
else:
    print("You lose. Git gud")