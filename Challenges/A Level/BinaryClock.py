#programming challenge 61

import datetime

def ConvertToBin(Num):
    BinValues = [32, 16, 8, 4, 2, 1]
    Binary = ["  " for i in BinValues]
    for i in range(len(BinValues)):
        if Num - BinValues[i] >= 0:
            Binary[i] = " X"
            Num -= BinValues[i]
    return Binary

def ListToStr(List: list):
    out = ""
    for i in List:
        out += i
        out += "  "
    return out

TimeStamp = datetime.datetime.now()
Times = ["       32", "16", " 8", " 4", " 2", " 1"]

print(ListToStr(Times))
print(f"Hours  {ListToStr(ConvertToBin(TimeStamp.hour + 1))}")
print(f"Mins   {ListToStr(ConvertToBin(TimeStamp.minute))}")
print(f"Secs   {ListToStr(ConvertToBin(TimeStamp.second))}")


