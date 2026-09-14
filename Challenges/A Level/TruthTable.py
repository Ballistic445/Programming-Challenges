#programming challenge 43

a = False
b = False

def Choose(Choices):
    while True:
        out = input(f"choose a logic gate (and, or, not)\n> ")
        out = out.lower()
        if out in Choices:
            return out

def LogicGate(Operator):
    Range = range(1, 5)
    if Operator == "not":
        Range = range(1, 3)
    for i in Range:
        if i >= 3:
            a = "True"
        else: a = "False"
        if i % 2 == 0:
            b = "True"
        else: b = "False"
        
        if Operator == "and":
            print(f"{a} and {b} is {a and b}")
        elif Operator == "or":
            print(f"{a} or {b} is {a or b}")
        else:
            print(f"not {b} is {not b}")
        
LogicGate(Choose(["and", "or", "not"]))