#programming challenge 58

Sentence = input("Enter a sentence: ")
Result = ""
for i in Sentence:
    if i.isalpha():
        Result += "*"
    else:
        Result += i
        
print(Result)