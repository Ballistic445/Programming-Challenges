#A level Programming challenge 13. continuation from challenge 12

#init variables
pi = 3.14159
Length = float(input("enter length of garden: "))
Width = float(input("enter Width of garden: "))
Radius = float(input("Enter radius of flower bed: "))

#calculations
CircleArea = pi * Radius * Radius
RectArea = Length * Width
TurfArea = RectArea - CircleArea

#print result
print("\n")
if TurfArea > 0:
    print(f"Total area of turf required: {TurfArea}m^2")
    
    #calculate costs
    TurfCost = TurfArea * 1.2
    GrassCost = TurfArea * 0.2 + 60
    
    #print costs
    print(f"Cost of turf: £{TurfCost}")
    print(f"Cost of grass: £{GrassCost}")
    
    #determine which is cheaper
    if TurfCost < GrassCost:
        print("Turf is cheaper to install")
    elif GrassCost < TurfCost:
        print("Grass is cheaper to install")
    else: print("both are equal cost to install")
    
else: print("invalid values. \nTurf should be larger than 0m^2")