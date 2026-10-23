#haunted code challenge 1.3

trick = 0
treat = 0

for j in range(20):
    for i in range(100):
        if i % 15 == 0: 
            print("Trick and treat")
            trick += 1
            treat += 1
        elif i % 3 == 0:
            print("trick")
            trick += 1
        elif i % 5 == 0:
            print("treat")
            treat += 1
            
print(f"amount of tricks: {trick}")
print(f"amount of treats: {treat}")