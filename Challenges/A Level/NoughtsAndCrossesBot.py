#programming challenge 65
import math
from sys import exit
import random

class Player:
    Index = 0
    def __init__(self, name, icon):
        self.Name = name
        self.Icon = icon

    def Replace(self, Grid):
        if Grid[math.ceil(self.Index / 3) - 1][(self.Index % 3) - 1] == "-":
            Grid[math.ceil(self.Index / 3) - 1][(self.Index % 3) - 1] = self.Icon
            return Grid, True
        else:
            print("Space already entered")
            return Grid, False

def Choose(Message, Choices):
    while True:
        out = input(f"{Message}\n>")
        out = out.lower()
        if out in Choices:
            return out

def WinCondition(Grid, CurrentPlayer, TurnCount):
    for i in range(len(Grid)):
        if [CurrentPlayer.Icon for i in range(3)] == Grid[i]:
            return True
        elif Grid[0][i] == CurrentPlayer.Icon and Grid[1][i] == CurrentPlayer.Icon and Grid[2][i] == CurrentPlayer.Icon:
            return True
    if Grid[0][0] == CurrentPlayer.Icon and Grid[1][1] == CurrentPlayer.Icon and Grid[2][2] == CurrentPlayer.Icon:
        return True
    elif Grid[0][2] == CurrentPlayer.Icon and Grid[1][1] == CurrentPlayer.Icon and Grid[2][0] == CurrentPlayer.Icon:
        return True
    elif TurnCount >= 9:
        print("It's a draw!")
        exit()
    else: return False
    
def DisplayGrid(Grid):
    for i in range(len(Grid)):
        for j in Grid[i]:
            print(f"{j}    ", end = "")
        print("\n")   
   
ReferenceGrid = [[j + (3 * i) + 1 for j in range(3)] for i in range(3)]   
print("Reference:")
DisplayGrid(ReferenceGrid)
print("\n")

VsSetting = Choose("Do you want to play against the bot? (y/n)", ["y", "n"])

Grid = [["-" for j in range(3)] for i in range(3)]
P1 = Player("Player 1", "X")
if VsSetting == "y":
    P2 = Player("Computer", "O")
else:
    P2 = Player("Player 2", "O")

GameCompleted = False
Turn = 0
CurrentPlayer = ""
DisplayGrid(Grid)
while not GameCompleted:
    Valid = False
    Turn += 1
    if Turn % 2 != 0:
        CurrentPlayer = P1
    else: 
        CurrentPlayer = P2
    print(f"\nCurrent turn: {CurrentPlayer.Name}")
    
    while Valid == False:
        if CurrentPlayer == P2 and VsSetting == "y":
            CurrentPlayer.Index = random.randint(1, 9)
        else:
            CurrentPlayer.Index = int(Choose("Enter a number (1-9)", [str(i) for i in range(1, 10)]))
        Grid, Valid = CurrentPlayer.Replace(Grid)
    DisplayGrid(Grid)
    GameCompleted = WinCondition(Grid, CurrentPlayer, Turn)
    
print(f"{CurrentPlayer.Name} Wins!")