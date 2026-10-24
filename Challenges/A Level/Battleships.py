#Programming challenge 66
import math

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
            
def ChooseShip(Choices):
    print("Choose the ship you want to place down:")
    for i in Choices:
        print(f"- {i.Name} (length {i.Length})")
    while True:
        out = input(f"\n>")
        out = out.lower()
        for i in range(len(Choices)):
            if out == Choices[i].Name.lower():
                return Choices[i]
        
def Choose(Message, Choices):
    while True:
        out = input(f"{Message}\n>")
        out = out.lower()
        if out in Choices:
            return out

def FillerText():
    for i in range(30):
        print("-----------------------------------------------------------------------")

class Ship():
    def __init__(self, Name, Length):
        self.Name = Name
        self.Length = Length
        self.Position = []
        
class Player():
    def __init__(self, Name):
        self.Name = Name
        self.Grid = InitGrid()
        self.AttackGrid = InitGrid()
        self.Destroyer = Ship("Destroyer",2)
        self.Submarine = Ship("Submarine",3)
        self.Cruiser = Ship("Cruiser", 3)
        self.Battleship = Ship("Battleship", 4)
        self.Carrier = Ship("Carrier", 5)
        self.Ships = [self.Destroyer, self.Submarine, self.Cruiser, self.Battleship, self.Carrier]
        self.UnplacedShips = self.Ships
    
    def CheckShipStatus(self):
        for i in self.Ships:
            Destroyed = True
            for j in i.Position:
                if self.Grid[j[0]][j[1]] == "H":
                    Destroyed = False
            if Destroyed:
                print(f"{i.Name} Destroyed!")
                self.Ships.remove(i)
        
    def DisplayGrid(self):
        print("   ", end = "")
        for i in self.Grid:
            for j in i:
                print(f"{j}  ", end = "")
            print()
            
    def DisplayGrids(self):
        CombinedGrid = []
        for i in range(len(self.Grid)):
            CombinedGrid.append([])
            RowSize = len(self.Grid[i]) + len(self.AttackGrid[i])
            for j in range(RowSize):
                if j > RowSize / 2:
                    CombinedGrid[i].append(self.Grid[i][j % math.ceil(RowSize / 2)])
                else:
                    CombinedGrid[i].append(self.AttackGrid[i][j % math.ceil(RowSize / 2)])
        print("   ", end = "")
        for i in range(len(CombinedGrid)):
            for j in range(len(CombinedGrid[i])):
                if j % 11 == 0 and j != 0 and i != 0:
                    print("       ", end = "")
                elif j % 10 == 0 and i == 0 and j != 0:
                    print("         ", end = "")
                print(f"{CombinedGrid[i][j]}  ", end = "")
            print()
            
    def PlaceShip(self, SelectedShip, Orientation: str, Coordinate):
        if Orientation == "h":
            for i in range(SelectedShip.Length):
                try:
                    if self.Grid[Coordinate[0]][Coordinate[1] + i] != "-":
                        print("\nInvalid Placement as it overlaps with other ships. \n")
                        return 0
                except IndexError:
                    print("Invalid placement as the Ship Goes past the border. \n")
                    return 0
            for i in range(SelectedShip.Length):
                self.Grid[Coordinate[0]][Coordinate[1] + i] = "H"
                SelectedShip.Position.append([Coordinate[0], Coordinate[1] + i])
        elif Orientation == "v":
            for i in range(SelectedShip.Length):
                try:
                    if self.Grid[Coordinate[0] + i][Coordinate[1]] != "-":
                        print("\nInvalid Placement as it overlaps with other ships. \n")
                        return 0
                except IndexError:
                    print("Invalid placement as the Ship Goes past the border. \n")
                    return 0
            for i in range(SelectedShip.Length):
                self.Grid[Coordinate[0] + i][Coordinate[1]] = "H"
                SelectedShip.Position.append([Coordinate[0] + i, Coordinate[1]])
        self.UnplacedShips.remove(SelectedShip)
        
P1 = Player("Player 1")
P2 = Player("Player 2")

#place ships
for i in range(2):
    if i % 2 == 0:
        CurrentPlayer = P1
    else:
        CurrentPlayer = P2
    print(f"{CurrentPlayer.Name}:")
    while len(CurrentPlayer.UnplacedShips) > 0:
        CurrentPlayer.DisplayGrid()
        SelectedShip = ChooseShip(CurrentPlayer.UnplacedShips)
        Orientation = Choose("Enter the orientation you want (Horizontal: h, Vertical: v): ", ["h", "v"])
        Choice = ChooseCoordinate("Enter the coordinates of The ship you want to place (Ship goes from that coordinate down/right):")
        Index = [ord(Choice[0]) % 64, int(Choice[1])]
        CurrentPlayer.PlaceShip(SelectedShip, Orientation, Index)
    CurrentPlayer.DisplayGrid()
    print("\nThis is Your Board.\n")
    input("Press ENTER to advance.   ")
    CurrentPlayer.Ships = [CurrentPlayer.Destroyer, CurrentPlayer.Submarine, CurrentPlayer.Cruiser, CurrentPlayer.Battleship, CurrentPlayer.Carrier]

#main game loop
Count = 0
while True:
    if Count % 2 == 0:
        CurrentPlayer = P1
        OpponentPlayer = P2
    else:
        CurrentPlayer = P2
        OpponentPlayer = P1
    print(f"\n\nCurrent Player: {CurrentPlayer.Name}")
    CurrentPlayer.DisplayGrids()
    while True:
        Choice = ChooseCoordinate("Enter the coordinates of your attack:")
        Index = [ord(Choice[0]) % 64, int(Choice[1])]
        if OpponentPlayer.Grid[Index[0]][Index[1]] == "-":
            CurrentPlayer.AttackGrid[Index[0]][Index[1]] = "O"
            OpponentPlayer.Grid[Index[0]][Index[1]] = "O"
            break
        elif OpponentPlayer.Grid[Index[0]][Index[1]] == "H":
            CurrentPlayer.AttackGrid[Index[0]][Index[1]] = "X"
            OpponentPlayer.Grid[Index[0]][Index[1]] = "X"
            break
        else:
            print("Space already entered.")
    Count += 1
    CurrentPlayer.DisplayGrids()
    OpponentPlayer.CheckShipStatus()
    if len(OpponentPlayer.Ships) == 0:
        print(f"\n\n{CurrentPlayer.Name} Wins!!!")
        break
    input("Press ENTER to advance.   ")
    FillerText()
    input("Swap to the next player, then press ENTER to advance.   ")