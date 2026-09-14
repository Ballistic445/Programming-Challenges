#programming challenge 44

a = False
b = False

def Choose(Choices):
    while True:
        out = input(f"choose a logic gate (and, or, not, xor, nand, nor)\n> ")
        out = out.lower()
        if out in Choices:
            return out

def LogicGate(Operator):
    Range = range(1, 5)
    if Operator == "not":
        Range = range(1, 3)
    for i in Range:
        if i >= 3:
            a = True
        else: a = False
        if i % 2 == 0:
            b = True
        else: b = False
        
        if Operator == "and":
            print(f"{a} and {b} is {a and b}")
        elif Operator == "or":
            print(f"{a} or {b} is {a or b}")
        elif Operator == "xor":
            print(f"Exclusively {a} or {b} is {a ^ b}")
        elif Operator == "nand":
            print(f"not {a} and {b} is {not(a and b)}")
        elif Operator == "nor":
            print(f"not {a} or {b} is {not(a or b)}")
        else:
            print(f"not {b} is {not b}")
        
LogicGate(Choose(["and", "or", "not", "xor", "nand", "nor"]))