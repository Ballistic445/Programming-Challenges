#programming challenge 21

def Compare(a, b):
    if a == b: return "a"
    else: return a > b
    
x = int(input("enter a number: "))
y = int(input("enter another number: "))

if Compare(x, y) == True:
    if x % y == 0:
        print(f"{y} is a factor of {x}")
    else:
        print(f"{y} is not a factor of {x}")
else:
    if y % x == 0:
        print(f"{x} is a factor of {y}")
    else:
        print(f"{x} is not a factor of {y}")
    

    