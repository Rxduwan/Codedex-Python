import random

# Pre-Defined Variables

p1 = 0
cpu = random.randint(1, 3)


# Program Intro

print(f"\n===================\nRock Paper Scissors Lizard Spock\n===================\n")


# Player input

p1 = int(input(f"1) ✊\n2) ✋\n3) ✌️\n4) 🦎\n5) 🖖\nPick a number: "))

while p1 != 1 and p1 != 2 and p1 != 3 and p1 != 4 and p1 != 5:
    p1 = int(input(f"\nUh-Oh! Thats not a valid input please try again7\n1) ✊\n2) ✋\n3) ✌️\n4) 🦎\n5) 🖖\nPick a number: "))


# Printing CPU and Player Selection

if p1 == 1:
    print(f"\nYou Chose: ✊")
elif p1 == 2:
    print(f"\nYou Chose: ✋")
elif p1 == 3:
    print(f"\nYou Chose: ✌️")
elif p1 == 4:
    print(f"\nYou Chose: 🦎")
elif p1 == 5:
    print(f"\nYou Chose: 🖖")

if cpu == 1:
    print("CPU Chose: ✊")
elif cpu == 2:
    print("CPU Chose: ✋")
elif cpu == 3:
    print("CPU Chose: ✌️")
elif cpu == 4:
    print("CPU Chose: 🦎")
elif cpu == 5:
    print("CPU Chose: 🖖")


# Win-Lose-Draw Check

if cpu == p1:
    print("You Drew!")
elif cpu == 2 and p1 == 3:
    print("You Win!")
elif cpu == 1 and p1 == 2:
    print("You Win!")
elif cpu == 4 and p1 == 1:
    print("You Win!")
elif cpu == 5 and p1 == 4:
    print("You Win!")
elif cpu == 3 and p1 == 5:
    print("You Win!")
elif cpu == 4 and p1 == 3:
    print("You Win!")
elif cpu == 2 and p1 == 4:
    print("You Win!")
elif cpu == 5 and p1 == 2:
    print("You Win!")
elif cpu == 1 and p1 == 5:
    print("You Win!")
elif cpu == 3 and p1 == 1:
    print("You Win!")
else:
    print("You Lose!")

