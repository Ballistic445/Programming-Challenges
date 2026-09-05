#programming challenge 4
def Compare(a, b):
    if a == b: return "a"
    else: return a > b

x = float(input("enter a number: "))
y = float(input("enter another number: "))
result = 0

if Compare(x, y) == True: 
    result = x / y
else:
    result = y / x
    
print(f"divided result is {result}.")