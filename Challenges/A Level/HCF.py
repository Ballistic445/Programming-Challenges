#programming challenge 26

def Compare(a, b):
    if a == b: return "a"
    else: return len(a) > len(b)

def Factors(num):
    factors = []
    NumRange = int(num / 2 + 1)    
    for i in range(1, NumRange):
        if num % i == 0:
            factors.append(i)
    factors.append(num)
    return factors

def FindHCF(LargerList, SmallerList):
    for i in range(len(SmallerList) - 1, 0, -1):
        if SmallerList[i] in LargerList:
            return SmallerList[i]
    

x = int(input("Enter a number: "))
FactorsX = Factors(x)

y = int(input("Enter another number: "))
FactorsY = Factors(y)

Result = 0

if Compare(FactorsX, FactorsY) == True:
    Result = FindHCF(FactorsX, FactorsY)
else:
    Result = FindHCF(FactorsY, FactorsX)
    
print(f"Highest common factor: {Result}")