#programming challenge 24

num = int(input("Enter a number: "))
factors = []
NumRange = int(num / 2 + 1)

for i in range(1, NumRange):
    if num % i == 0:
        factors.append(i)

factors.append(num)
if len(factors) == 2:
    print("Your number is a prime")
else:
    print("Your number is not prime")