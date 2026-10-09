#programming challenge 47 + 48
from random import randint
from sys import exit

def GenerateCode(Length: int):
    Code = []
    for i in range(Length):
        while True:
            Num = str(randint(0, 9))
            if Num not in Code:
                break
        Code.append(Num)
    return Code

def Convert(List: list):
    out = ""
    for i in List:
        out += i
        out += " "
    return out
        
Attempts = 0
Code = GenerateCode(4)
HiddenCode = ["-" for i in Code]
print(f"Computer has generated a {len(Code)} digit code. guess the code.")
print("You may only guess one digit at a time.\n")

CodeSolved = False
while not CodeSolved:
    Guess = "b"
    Attempts += 1
    print(f"Attempt {Attempts}:")
    print(Convert(HiddenCode))
    while not Guess.isdigit():
        Guess = input("Enter a number: ")
    if Guess in Code:
        print("Your guess is in the code.")
        for i in range(len(Code)):
            if Guess == Code[i]:
                HiddenCode[i] = Guess
    else:
        print("Your guess is not in the code.")
    if "-" not in HiddenCode:
        CodeSolved = True
    elif Attempts >= 15:
        print("Too many attempts. You lose.")
        exit()

print(Convert(HiddenCode))
print("Congrats! You Win!")