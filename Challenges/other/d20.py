import random

#rolls the dice
def d20():
    return random.randint(1, 20)

#checks for if resultis even
def IsEven(num):
    if num % 2 == 0:
        return "Result is even"
    else: return "Result is odd"

#output sequence
roll = d20()
print(roll)
print(IsEven(roll))
