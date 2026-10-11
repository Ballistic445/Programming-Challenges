#programming challenge 56

Sentence = input("Enter a sentence: ")
Result = ""
for i in Sentence:
    if i.isupper():
        if ord(i) >= 78:
            Result += chr(ord(i) - 13)
        else:
            Result += chr(ord(i) + 13)
    elif i.islower():
        if ord(i) >= 110:
            Result += chr(ord(i) - 13)
        else:
            Result += chr(ord(i) + 13)
    else: Result += i
    
print(Result)