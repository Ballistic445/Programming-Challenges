#programming challenge 46
from random import randint

def GenerateCode(Length: int):
    Code = []
    for i in range(Length):
        while True:
            Num = randint(0, 9)
            if Num not in Code:
                break
        Code.append(Num)
    return Code
        
print(GenerateCode(4))