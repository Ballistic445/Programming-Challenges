#programming challenge 41 + 42

HexDigits = {"A":10, "B":11, "C":12, "D":13, "E":14, "F":15}
x = input("Enter a hexadecimal number: ")
Hex = 0
mult = 1

for i in range(len(x) - 1, -1, -1):
    try: Hex += int(x[i]) * mult
    except ValueError:
        Hex += HexDigits[x[i].upper()] * mult
    mult *= 16

print(Hex)
Bin = bin(Hex)
print(f"Binary: {Bin}")