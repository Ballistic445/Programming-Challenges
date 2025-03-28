#OCR programming challenges
import random

def LoadMastermind():
    #__MASTERMIND__
    #validate input (function)
    def validate(item, CodeLength):
        if len(item) != CodeLength:
            print("ERROR: Guess length not equal to codeword length")
            return False
        try: ItemInt = int(item)
        except ValueError:
            print("ERROR: invalid type")
            return False
        return True

    #difficulty choice
    difficulties = {"easy": 4, "hard": 5}
    print("__MASTERMIND__\n")
    while True:
        In = input("""CHOOSE A DIFFICULTY
    - Easy :)
    - Hard >:)
                
    Enter: """)
        if In.lower() == "easy" or In.lower() == "hard":
            break
        else:
            print("ERROR: Invalid input. Please try again")
            

    #generte code
    CodeLength = difficulties[In.lower()]
    code = []
    for i in range(CodeLength):
        code.append(str(random.randint(0, 9)))

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
        if CorrectVals == CodeLength:
            print("Correct!")
            break

        #output result of turn
        print(f"You got {CorrectVals} values correct.\n")

    #show results
    print(f"You took {tries} attempts to crack the code.")
    