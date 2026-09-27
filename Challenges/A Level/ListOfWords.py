#programming challenge 45

def Compare(Str1, Str2):
    for i in range(len(Str1)):
        if ord(Str1[i].lower()) > ord(Str2[i].lower()):
            return False
    return True

ListOfWords = []
IsOrdered = True

while True:
    ListOfWords.append(input("Enter a word: "))
    if ListOfWords[-1].lower() == "stop":
        break
    if IsOrdered:
        try: 
            IsOrdered = Compare(ListOfWords[-2], ListOfWords[-1])
        except IndexError:
            pass
        
print(f"List is ordered: {IsOrdered}")