#Programming challenge 10

def Draw(spaces: int, X: int):
    result = ""
    for i in range(spaces):
        result += " "
    for i in range(X):
        result += "X"
    return str(result)

spaces = int(input("enter how many spaces: "))
Xs = int(input("enter how many Xs: "))
print(Draw(spaces, Xs))