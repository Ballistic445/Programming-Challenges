#programming challenge 11

#draw function from previous challenge
def Draw(spaces: int, X: int):
    result = ""
    for i in range(spaces):
        result += "  "
    for i in range(X):
        result += "X"
        result += " "
    return str(result)

#draw a square
def Square(Size: int):
    for i in range(Size):
        print(Draw(3, Size))

#draw a triangle
def Triangle(Length: int):
    for i in range(Length):
        print(Draw(3, i + 1))

#draw an equilateral triangle. can also invert
def Equilateral(Size: int, IsInverted = False):
    Indent = Size + 2
    if IsInverted:
        Indent = 3
    for i in range(0, Size * 2, 2):
        if not IsInverted:
            print(Draw(Indent, i + 1))
            Indent -= 1
        else:
            print(Draw(Indent, Size * 2 - 1))
            Indent += 1
            Size -= 1
        
            
#Draw a diamond
def Diamond(Size: int):
    Equilateral(Size)
    print(Draw(2, Size * 2 + 1))
    Equilateral(Size, True) 

#asks user for inputs
Select = int(input("Enter a shape: \n1. Square \n2. Triangle \n3. Equilateral \n4. Diamond \n\n>")) 
Size = int(input("\n Enter size of shape: "))

#creates shape according to user input
if Select == 1: Square(Size)
elif Select == 2: Triangle(Size)
elif Select == 3: Equilateral(Size)
elif Select == 4: Diamond(Size - 1)
else: print("\nInvalid shape selection.\nPlease enter a number according to desired shape.")