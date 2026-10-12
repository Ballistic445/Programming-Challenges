#programming cheallenge 59

Sentence = input("Enter a sentence: ").lower()
Letter = ""

while True:
    Letter = input("Enter a letter: ").lower()
    if len(Letter) != 1:
        print("not a letter")
    elif not Letter.isalpha():
        print("not a letter")
    else: break

Located = ""

for i in range(len(Sentence)):
    if Letter in Sentence[i]:
        Located += f"{str(i)} "
        
print(Located)