#programming challenge 62

import datetime

def Choose(Message, Length: list):
    while True:
        out = input(f"{Message}\n>")
        out = out.lower()
        if out.isnumeric() and len(out) in Length:
            return out

def Convert(Months, ):
    MonthsToDays = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    out = 0
    for i in range(1, Months):
        out += MonthsToDays[i]
    return out

Days = 0

birthday = datetime.date(int(Choose("Enter Year of birthday", [4])), int(Choose("Enter Month of birthday", [1, 2])), int(Choose("Enter Day of birthday", [1, 2])))
YearDifference = datetime.datetime.now().year - birthday.year
MonthDifference = Convert(datetime.datetime.now().month) - Convert(birthday.month)
DayDifference = datetime.datetime.now().day - birthday.day

Days += YearDifference * 365
Days += DayDifference
Days += MonthDifference

print(f"\nYou are {Days} days old.")
