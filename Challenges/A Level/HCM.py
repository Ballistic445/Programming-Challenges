#programming challenge 26

def Compare(a, b):
    if a == b: return "a"
    else: return a > b

def Factors(num, factors):
    NumRange = 0    
    for i in range(1, NumRange):
        if num % i == 0:
            factors.append(i)
    return factors

x = int(input("Enter a number: "))
FactorsX = []

y = int(input("Enter another number: "))
FactorsY = []