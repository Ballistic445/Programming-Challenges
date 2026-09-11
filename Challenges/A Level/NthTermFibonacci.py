#programming challenge 31

old = 0
new = 1

num = int(input("enter an nth term: "))

for i in range(2, num):
    Placeholder = new
    new += old
    old = Placeholder
    
print(f"Term {num}: {new}")