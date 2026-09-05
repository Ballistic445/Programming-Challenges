#programming challenge 3

def Compare(a, b):
    if a == b: return "a"
    else: return a > b
    
x = int(input("Enter a number: "))
y = int(input("enter another number: "))

if Compare(x, y) == True:
    print(f"{x} is bigger")
elif Compare(x, y) == False:
    print(f"{y} is bigger")
else: print("both numbers are equal")