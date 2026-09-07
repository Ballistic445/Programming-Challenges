#programming challenge 18

ans = input("enter a number: ")
ans = ans
if ans.isnumeric():
    print("Your number is indeed a number.")
elif ans.isalnum():
    print("this is not a number you silly billy.")
elif ans.lower() == "a number":
    print("smartass.")
elif "." in ans:
    print("b")

