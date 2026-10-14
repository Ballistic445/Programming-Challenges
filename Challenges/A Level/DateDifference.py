#programming challenge 63

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

print("First date:")
Date1 = datetime.date(int(Choose("Enter Year:", [4])), int(Choose("Enter Month:", [1, 2])), int(Choose("Enter Day:", [1, 2])))
print("Second date:")
Date2 = datetime.date(int(Choose("Enter Year:", [4])), int(Choose("Enter Month:", [1, 2])), int(Choose("Enter Day:", [1, 2])))

YearDifference = Date1.year - Date2.year
MonthDifference = Convert(Date1.month) - Convert(Date2.month)
DayDifference = Date1.day - Date2.day

Days += YearDifference * 365
Days += DayDifference
Days += MonthDifference

if Days < 0:
    Days *= -1

print(f"\nDifference between dates in days: {Days}")
