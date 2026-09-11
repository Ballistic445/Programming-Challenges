#programming challenge 28

Sentence = input("Enter a sentence: ")

NumOfWords = 0
WaitForNextWord = True
for i in Sentence:
    if i == " ":
        WaitForNextWord = False
    elif i.isascii() and not WaitForNextWord:
        NumOfWords += 1
        WaitForNextWord = True   
        
print(f"There are {NumOfWords} words in this sentence.")