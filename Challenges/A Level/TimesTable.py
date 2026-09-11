#programming challenge 29

Vertical = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Horizontal = Vertical

for i in Horizontal:
    line = ""
    for j in Vertical:
        line += str(j * i) + " "
    print(line)