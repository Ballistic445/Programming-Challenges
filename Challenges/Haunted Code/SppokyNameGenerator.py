#Haunted Code challenge 1.1

def Choose(Message, Choices):
    while True:
        out = input(f"{Message}\n>")
        out = out.lower()
        if out in Choices:
            return out

PrefixDict = {"a":"apple", "b":"bamboozling", "c":"condescending", "d":"dark", "e":"ethan", "f":"frightening", "g":"ghastly", "h":"hallowed", "i":"inspirational(but spooky)", "j":"josh", "k":"kool", "l":"light", "m":"michael", "n":"naughty", "o":"omnissian", "p":"petrifying", "q":"quaint", "r":"rowdy", "s":"sad", "t":"terrifying", "u":"unbelievable", "v":"vexing", "w":"weary", "x":"xanthous", "y":"yes", "z":"zombified"}
MonthDict = {"january":"the trickster", "february":"the amazing", "march":"the terrific", "april":"ghost", "may":"screecher", "june":"zombie", "july":"pumpkin", "august":"child", "september":"skeleton", "october":"edgelord", "november":"ghost", "december":"reindeer"}
print(f"{PrefixDict[Choose("Enter letter of first name: ", [i for i in PrefixDict.keys()])]} {MonthDict[Choose("Enter birth month: ", [i for i in MonthDict.keys()])]}")