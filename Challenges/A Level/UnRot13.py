#programming challenge 57

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
    
print(f"Encrypted: {Result}")

Decoded = ""

for i in Result:
    if i.isupper():
        if ord(i) < 78:
            Decoded += chr(ord(i) + 13)
        else:
            Decoded += chr(ord(i) - 13)
    elif i.islower():
        if ord(i) < 110:
            Decoded += chr(ord(i) + 13)
        else:
            Decoded += chr(ord(i) - 13)
    else: Decoded += i

print(f"Decoded: {Decoded}")