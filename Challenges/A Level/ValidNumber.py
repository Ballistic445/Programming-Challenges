#programming challenge 40

def Validate(num: str):
    NumOfDots = 0
    NumOfDashes = 0
    for i in num:
        if i == ".":
            NumOfDots += 1
        elif i == "-":
            NumOfDashes += 1
        elif not i.isdigit():
            return False
    if NumOfDots > 1 or NumOfDashes > 1:
        return False
    else:
        return True
    
if Validate(input("Enter a valid number: ")):
    print("Your number is a valid number")
else: print("invalid.")