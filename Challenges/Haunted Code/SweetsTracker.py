#haunted code challenge 2.1

def AddRecord():
    Name = input("Enter Name: ")
    Count = 0
    while True:
        Count = input("Enter number of sweets: ")
        if Count.isdigit():
            break
    with open("/workspaces/OCR-Programming-Challenges/Challenges/Haunted Code/SweetsTracker.txt", "a") as Records:
        pass