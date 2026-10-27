#haunted code challenge 2.4

def Choose(Message, Choices):
    while True:
        out = input(f"{Message}\n>")
        out = out.lower()
        if out in Choices or out.isdigit():
            return out

Costumes = {}
Iter = 0
print("Give the following costumes a score.")
while True:
    Iter += 1
    i = Choose(f"Costume {Iter}: ", ["end"])
    if i == "end":
        break
    else:
        Costumes[Iter] = i

print("\nScores:")
for i in Costumes.keys():
    print(f"Costume {i}: {Costumes[i]}")