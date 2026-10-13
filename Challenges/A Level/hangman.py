#programming challenge 60
import random
from sys import exit

def ChooseChar():
    while True:
        Letter = input("Enter a letter: ").lower()
        if len(Letter) != 1:
            print("not a letter")
        elif not Letter.isalpha():
            print("not a letter")
        else: return Letter
        
def Convert(List: list):
    out = ""
    for i in List:
        out += i
        out += " "
    return out

GameState = ["""

_|________
    """, """

 | 
 |     
 |      
 |      
_|_______
    """, """

 |/      
 |      
 |      
 |      
_|_______
    """, """
__________
 |/      
 |      
 |      
 |        
_|_______
    """, """
__________
 |/      |
 |      
 |      
 |        
_|_______
    """, """
__________
 |/      |
 |      (_)
 |      
 |       
_|_______
    """, """
__________
 |/      |
 |      (_)
 |      /|\\
 |        
_|_______
    """, """
__________
 |/      |
 |      (_)
 |      /|\\
 |      / \ 
_|_______
    """]

SelectedWord = ""
Completed = []

with open("/workspaces/OCR-Programming-Challenges/Challenges/A Level/hangman.txt", "r") as Hangman:
    SelectedWord = random.choice(Hangman.readlines())
    #print(SelectedWord)
    for i in range(len(SelectedWord) - 1):
        Completed.append("-")

IncorrectLetters = []

while len(IncorrectLetters) < 8:
    print(GameState[len(IncorrectLetters)])
    print(f"Incorrect letters: {Convert(IncorrectLetters)}")
    GuessedCorrectly = False
    print(Convert(Completed))
    if "-" not in Completed:
        print("Congrats! You win!")
        exit()
    while True:    
        Letter = ChooseChar()
        if Letter in IncorrectLetters or Letter in Completed:
            print("Already guessed.")
        else: break
    for i in range(len(SelectedWord)):
        if Letter == SelectedWord[i]:
            Completed[i] = Letter
            GuessedCorrectly = True
    if not GuessedCorrectly:
        print("incorrect.")
        IncorrectLetters.append(f"{Letter}")
    else: print("Correct!")
    
print(f"The word was {SelectedWord}")