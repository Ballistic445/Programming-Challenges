#haunted code challenge 2.1

def AddRecord():
    Name = input("Enter Name: ")
    Count = 0
    while True:
        Count = input("Enter number of sweets: ")
        if Count.isdigit():
            break
    with open("/workspaces/OCR-Programming-Challenges/Challenges/Haunted Code/SweetsTracker.txt", "a") as Records:
        Records.write(f"{Name} {Count}\n")
        
def ReadRecords():
    with open("/workspaces/OCR-Programming-Challenges/Challenges/Haunted Code/SweetsTracker.txt", "r") as Records:
        Items = [i.split(" ") for i in Records.readlines()]
        SweetsList = [int(i[1]) for i in Items] 
        for i in Items:
            print(f"{i[0]}: {i[1]}")
        return SweetsList
   
def FindBiggestNumber(NumsList):
    BiggestNumber = 0
    for i in NumsList:
        if i > BiggestNumber:
            BiggestNumber = i
    return BiggestNumber
    
AddRecord()
SweetsList = ReadRecords()
BiggestNumber = FindBiggestNumber(SweetsList)
print(f"Highest sweets count: {BiggestNumber}")