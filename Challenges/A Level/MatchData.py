#programming challenge 52

class Team():
    Goals = 0
    def __init__(self, Name, MatchHistory: list):
        self.Name = Name
        self.MatchHistory = MatchHistory
        
    def DisplayMatchHistory(self):
        print("Match history: ")
        for i in self.MatchHistory:
            print(f"> {i[0]} {i[1]} - {i[2]} {i[3]}")
    
def AskNum(Message):
    Num = "b"
    while not Num.isnumeric():
        Num = input(Message)
    return int(Num)

def Choose(Message, Choices):
    while True:
        out = input(f"{Message}\n>")
        out = out.lower()
        if out in Choices:
            return out

def Compare(a, b):
    if a == b: return "a"
    else: return a > b

def FindTeam(TeamsList, Team):
    for i in range(len(TeamsList)):
        if Team == TeamsList[i].Name:
            return i
    return "0"

def EnterTeamData(TeamName, TeamsList):
    SelectedTeam = FindTeam(TeamsList, TeamName)
    if SelectedTeam == "0":
        TeamsList.append(Team(TeamName, []))
        SelectedTeam = TeamsList[-1]
    else:
        SelectedTeam = TeamsList[SelectedTeam]
    SelectedTeam.Goals = AskNum("How many goals did they score?\n>")
    return SelectedTeam
            

TeamsList = []

while True:
    Choice = Choose("What would you like to do?\n- Enter a match result (1)\n- view teams (2)\n", ["1", "2"])
    if Choice == "1":
        HomeTeam = EnterTeamData(input("Enter the name of the home team: ").lower(), TeamsList)
        AwayTeam = EnterTeamData(input("Enter the name of the Away team: ").lower(), TeamsList)
        HomeTeam.MatchHistory.append([HomeTeam.Name, HomeTeam.Goals, AwayTeam.Goals, AwayTeam.Name])
        AwayTeam.MatchHistory.append([HomeTeam.Name, HomeTeam.Goals, AwayTeam.Goals, AwayTeam.Name])
    elif Choice == "2" and len(TeamsList) > 0:
        SelectedTeam = Choose("Enter the name of the team you want to see:", [i.Name for i in TeamsList]) 
        SelectedTeam = TeamsList[FindTeam(TeamsList, SelectedTeam)]
        SelectedTeam.DisplayMatchHistory()
    else: print("No teams entered")