#Programming challenge 51

class Team():
    def __init__(self, Name, GoalsScored):
        self.Name = Name
        self.GoalsScored = GoalsScored
        
def AskNum(Message):
    Num = "b"
    while not Num.isnumeric():
        Num = input(Message)
    return int(Num)

def Compare(a, b):
    if a == b: return "a"
    else: return a > b

HomeTeam = Team(input("Enter the name of the Home Team\n>"), AskNum("How Many goals did they score?\n> "))
AwayTeam = Team(input("Enter the name of the Away Team\n>"), AskNum("How Many goals did they score?\n> "))

if Compare(AwayTeam.GoalsScored, HomeTeam.GoalsScored) == True:
    print(f"{AwayTeam.Name} beat {HomeTeam.Name} by {AwayTeam.GoalsScored - HomeTeam.GoalsScored} goals.")
elif Compare(AwayTeam.GoalsScored, HomeTeam.GoalsScored) == "a":
    print(f"{HomeTeam.Name} drew with {AwayTeam.Name}")
else:
    print(f"{HomeTeam.Name} beat {AwayTeam.Name} by {HomeTeam.GoalsScored - AwayTeam.GoalsScored} goals.")