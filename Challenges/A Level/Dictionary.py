#programming challenge 53

def Lookup(Word):
    with open("/workspaces/OCR-Programming-Challenges/Challenges/A Level/dictionary.txt", "r") as Dictionary:
        return Word in [i.replace("\n", "") for i in Dictionary.readlines()]
    
if Lookup(input("Enter a word: ")):
    print("Your word is in the dictionary :)")
else:
    print("Your word is not in the dictionary :(")