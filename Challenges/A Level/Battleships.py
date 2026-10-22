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

class Ship():
    def __init__(self, Name, Length):
        self.Name = Name
        self.Length = Length
        self.Lives = Length
        
class Player():
    def __init__(self, Name):
        self.Name = Name
        self.Grid = InitGrid()
        self.Destroyer = Ship("Destroyer",2)
        self.Submarine = Ship("Submarine",3)
        self.Cruiser = Ship("Cruiser", 3)
        self.Battleship = Ship("Battleship", 4)
        self.Carrier = Ship("Carrier", 5)
        self.Ships = [self.Destroyer, self.Submarine, self.Cruiser, self.Battleship, self.Carrier]
        self.UnplacedShips = self.Ships
        
    def DisplayGrid(self):
        print("   ", end = "")
        for i in self.Grid:
            for j in i:
                print(f"{j}  ", end = "")
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

#main game loop
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