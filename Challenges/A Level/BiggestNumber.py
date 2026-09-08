BiggestNumber = 0

while True:
    num = int(input("Enter a number: "))
    if num > BiggestNumber:
        BiggestNumber = num
    elif num == 0:
        break

print(f"Biggest number entered: {BiggestNumber}")