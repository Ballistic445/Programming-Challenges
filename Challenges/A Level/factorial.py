#Programming challenge 25

num = int(input("Enter a number: "))
out = 1
for i in range(1, num + 1):
    out *= i
    
print(f"factorial of {num}: {out}")