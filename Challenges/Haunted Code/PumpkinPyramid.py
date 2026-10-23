#haunted code challenge 1.2

def Draw(spaces: int, X: int):
    result = ""
    for i in range(spaces):
        result += "  "
    for i in range(X):
        result += "*"
        result += " "
    return str(result)

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
            
Size = int(input("Enter how many layers you want the pyramid to be: "))
Equilateral(Size)