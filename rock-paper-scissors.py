# Rock Paper Scissors by ZetlexDK#0001

# Needs to be in Desktop for restart to work.

import os
import random

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


robotanswerlist = ["Rock", "Paper", "Scissors"]

input("Press ENTER to start!")
clearConsole()

print("Rock, paper, scissors?")
answer = input("Answer: ")
clearConsole()

print("You: " + str(answer))
print("Robot:", end = " "), print(random.choice(robotanswerlist))
print("")
print("Play Again?")
restart = input("Y / N: ")

if restart == "Y" or "y":
    path = "Desktop\Rock-paper-scissors.py"
    os.system("python " + path)

if restart == "N" or "n":
    clearConsole()
    exit()