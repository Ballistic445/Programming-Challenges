#Programming challenge 30

old = 0
new = 1

print("enter 'x' to exit program")
n = input("\n[start program]")
print(f"{old}\n")
print(f"{new}\n")
while True:
    Placeholder = new
    new += old
    old = Placeholder
    print(new)
    if input("").lower() == "x":
        break