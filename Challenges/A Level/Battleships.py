#Programming challenge 66

def InitGrid():
    Grid = [["-" for j in range(10)] for i in range(10)]
    Count = ord("A")
    for i in Grid:
        i.insert(0, chr(Count))
        Count += 1
    Grid.insert(0, [i + 1 for i in range(10)])
    return Grid

def ChooseCoordinate(Message):
    while True:
        out = input(f"{Message}\n>")
        out = out.upper()
        if len(out) <= 3 and len(out) > 1:
            out = (out[0], out[1:])
            try:
                if (ord(out[0]) >= 65 and ord(out[0]) <= 74) and (int(out[1]) >= 1 and int(out[1]) <= 10):
                    return out
            except ValueError:
                pass
        
class Ship():
    def __init__(self, Name, Length):
        self.Name = Name
        self.Length = Length
        
class Player():
    Destroyer = Ship("Destroyer",2)
    Submarine = Ship("Destroyer",3)
    Cruiser = Ship("Cruiser", 3)
    Battleship = Ship("Battleship", 4)
    Carrier = Ship("Carrier", 5)
    def __init__(self, Name):
        self.Name = Name
        self.Grid = InitGrid()
        
    def DisplayGrid(self):
        print("   ", end = "")
        for i in self.Grid:
            for j in i:
                print(f"{j}  ", end = "")
            print()
        
P1 = Player("Player 1")
P2 = Player("Player 2")

Count = 0
while True:
    if Count % 2 == 0:
        CurrentPlayer = P1
        OpponentPlayer = P2
    else:
        CurrentPlayer = P2
        OpponentPlayer = P1
    print(f"Current Player: {CurrentPlayer.Name}")
    CurrentPlayer.DisplayGrid()
    Choice = ChooseCoordinate("Enter the coordinates of your attack:")
    Index = [ord(Choice[0]) % 64, int(Choice[1])]
    if CurrentPlayer.Grid[Index[0]][Index[1]] != "X":
        CurrentPlayer.Grid[Index[0]][Index[1]] = "X"
    else:
        print("Space already entered.")
    Count += 1
    CurrentPlayer.DisplayGrid()
    input("Press ENTER to advance to the next player.   ")