num = int(input("Enter a number: "))
factors = ""
NumRange = int(num / 2)

for i in range(1, NumRange):
    if num % i == 0:
        factors += f"{str(i)}, "

factors += f"{num}"
print(f"Factors of {num}: {factors}")