#Programming challenge 15

Password = input("Enter password: ")
Score = 0
SymbolsPresent = False
NumbersPresent = False
LettersPresent = False

if len(Password) >= 8:
    Score += 2
elif len(Password) >= 5:
    Score += 1
       
for i in Password:
    if i.isalpha(): LettersPresent = True
    elif i.isnumeric(): NumbersPresent = True
    else: SymbolsPresent = True
    
if SymbolsPresent: Score += 1
if NumbersPresent: Score += 1
if LettersPresent: Score += 1

Score -= 1

if Score == 4: print("STRONG")
elif Score <= 2: print("WEAK")
else: print("MEDIUM")