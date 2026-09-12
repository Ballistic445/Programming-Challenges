#programming challenge 32
import random

results = {"rock":"scissors", "paper":"rock", "scissors":"paper"}
choices = ["rock", "paper", "scissors"]

bot1 = random.choice(choices)
bot2 = random.choice(choices)

print(f"bot 1 chose {bot1}")
print(f"bot 2 chose {bot2}")

if results[bot1] == bot2:
    print("bot 1 wins")
elif results[bot2] == bot1:
    print("bot 2 wins")
else: 
    print("it's a draw")