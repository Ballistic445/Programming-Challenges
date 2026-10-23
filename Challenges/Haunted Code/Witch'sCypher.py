#Haunted code challenge 1.4

PlainText = input("Enter a sentence: ")
CipherKey = int(input("How many characters do you want this shifted by:"))
CipherText = ""
for i in PlainText:
    CipherText += chr(ord(i) + CipherKey)
print(f"Encrypted: {CipherText}")
