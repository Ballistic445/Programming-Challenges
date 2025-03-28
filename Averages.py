#OCR programming challenges

#__AVERAGES__
def LoadAverages():
    print("__AVERAGES__\n")
    print("Enter numbers until you want to execute the calculation or quit the program")

    #validate function
    def validate(item):
        if item == "quit":
            print("Quitting program...")
            return "q"
        elif item == "exe":
            print("Execute algorithm initiated.")
            return "e"   
        try: ItemInt = int(item)
        except ValueError:
            print("ERROR: invalid type")
            return 
        return ItemInt

    #enter values until further action is done
    values = []
    status = ""
    ShouldRepeat = True
    while ShouldRepeat:
        num = input(f"Enter number{len(values)}: ")
        num = validate(num)
        values.append(num)
        if num == "q" or num == "e":
            values.pop()
            status = num
            ShouldRepeat = False

    if status == "e":
        total = 0
        for i in values:
            total += i
        avg = total / len(values)
        print(f"average: {avg}")