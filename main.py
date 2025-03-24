#OCR programming challenges
import random

#__MASTERMIND__

#validate input
def validate(item, CodeLength):
    if len(item) != CodeLength:
        print("ERROR: Guess length not equal to codeword length")
        return False
    try: ItemInt = int(item)
    except ValueError:
        print("ERROR: invalid type")
        return False
    return True

#generte code
CodeLength = 4
code = []
for i in range(CodeLength):
    code.append(str(random.randint(0, 9)))

print(code)
tries = 0
#game loop
while True:
    tries += 1
    CorrectVals = 0

    print(f"TURN {tries}:\n")
    #validate input
    ValidInput = False
    while not ValidInput:
        Guess = input("Enter your guess for the Codeword: ")
        ValidInput = validate(Guess, CodeLength)
    
    #check for how many values are correct
    for i in range(CodeLength):
        if Guess[i] == code[i]:
            CorrectVals += 1

    #output result of turn
    print(f"You got {CorrectVals} values correct.\n")