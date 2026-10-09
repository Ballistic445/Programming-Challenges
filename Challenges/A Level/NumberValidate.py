#programming challenge 18

ans = input("enter a number: ")
ans.replace(".", "", 1)
if ans.isnumeric():
    print("Your number is indeed a number.")
elif ans.lower() == "a number":
    print("smartass.")
else:
    print("this is not a number you silly billy.")
