#A level Programming challenge 12

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
else: print("invalid values. \nTurf should be larger than 0m^2")