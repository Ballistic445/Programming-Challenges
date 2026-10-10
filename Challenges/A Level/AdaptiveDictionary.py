#programming challenge 55

def Lookup(Word):
    with open("/workspaces/OCR-Programming-Challenges/Challenges/A Level/dictionary.txt", "r") as Dictionary:
        return Word in [i.replace("\n", "") for i in Dictionary.readlines()]
    
def AddToDictionary(Word):
    WordList = []
    with open("/workspaces/OCR-Programming-Challenges/Challenges/A Level/dictionary.txt", "r") as Dictionary:
        WordList = [i.replace("\n", "") for i in Dictionary.readlines()]
    IsInserted = False
    for i in range(len(WordList) - 1):
        for j in range(len(Word) - 1):
            if ord(Word[j]) < ord(WordList[i][j]):
                WordList.insert(i, Word)
                IsInserted = True
                break
            elif ord(Word[j]) > ord(WordList[i][j]):
                break
        if IsInserted:
            break
    with open("/workspaces/OCR-Programming-Challenges/Challenges/A Level/dictionary.txt", "w") as Dictionary:
        Dictionary.writelines([i + "\n" for i in WordList])
    
def Choose(Message, Choices):
    while True:
        out = input(f"{Message}\n>")
        out = out.lower()
        if out in Choices:
            return out

Sentence = input("Enter a Sentence: ").split(" ")
for i in Sentence:
    if Lookup(i):
        print(f"'{i}' is in the dictionary :)")
    else:
        print(f"'{i}' is not in the dictionary :(")
        Choice = Choose("Would you like to add this word to the dictionary? (y/n)", ["y", "n"])
        if Choice == "y":
            AddToDictionary(i)
            print("word added to dictionary.")
        else: print("word not added to dictionary")
        