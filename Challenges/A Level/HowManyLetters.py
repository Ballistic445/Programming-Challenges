#programming challenge 27
Sentence = input("Enter a sentence: ")

NumOfLetters = 0
for i in Sentence:
    if i.isalpha():
        NumOfLetters += 1
        
print(f"There are {NumOfLetters} letters in this sentence.")