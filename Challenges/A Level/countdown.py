import time

count = int(input("Enter countdown: "))
while count > 0:
    print(count)
    count -= 1
    time.sleep(1)
print("BLAST OFF!")