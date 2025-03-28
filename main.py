import Mastermind
import Averages

games = ["M", "A"]
print("""2 games so far:
- Mastermind (Enter M to play)
- Average calculator (Enter A to play)\n""")

def validate(item, Games):
    if item.upper() not in Games:
        print("ERROR: Invalid input.")
        return False
    return True

valid = False
while not valid:
    choice = input("Enter either M or A (mastermind, average calc):  ")
    valid = validate(choice, games)


if choice.upper() == "M":
    Mastermind.LoadMastermind()
elif choice.upper() == "A":
    Averages.LoadAverages()