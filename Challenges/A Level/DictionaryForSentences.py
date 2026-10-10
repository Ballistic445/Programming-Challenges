#programming challenge 54

def Lookup(Word):
    with open("/workspaces/OCR-Programming-Challenges/Challenges/A Level/dictionary.txt", "r") as Dictionary:
        return Word in [i.replace("\n", "") for i in Dictionary.readlines()]
    
Sentence = input("Enter a Sentence: ").split(" ")
for i in Sentence:
    if Lookup(i):
        print(f"{i} is in the dictionary :)")
    else:
        print(f"{i} is not in the dictionary :(")