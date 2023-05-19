"""
A script that lets you throw any amount of dice using the random module.
The way it's programmed is, it generates the first throw by default and then checks whether or not you can/want to throw more dice.
"""

import random
import time


def roll():
    "Roll dice!"

    # Variables
    throw = f"Threw a "
    exep = "One it is."
    stopped = False

    # Default throw
    t = 0
    die = random.randint(1, 6)
    t += die
    throw += str(die)
    dice_thrown = 1

    a = input("How many dice are we playing? >")

    # Checks for valid integer input
    try:
        num = int(a)
    except ValueError:
        print(exep)
        stopped = True

    # Throws extra if input is valid and also higher than 1
    if not stopped and num > 1:
            for _ in range(num-1):
                dice = random.randint(1, 6)
                t += dice
                throw += f" and a {dice}"
                dice_thrown += 1

            throw += f" ({t} total)!"

    if dice_thrown == 1:
        hand = "Threw a die..."
    else:
        hand = "Threw dice..."

    input("Ready? >")
    print(hand)
    time.sleep(random.randint(1,4))
    print("Clack!")
    time.sleep(1)
    print("Rolling..")
    time.sleep(random.randint(1,4))
    print(f"{throw}")
    time.sleep(2)

    b = input("Roll again? >")
    if b == "no":
        print("No dice\n")
        exit()

    print("\n")
    roll()


if __name__ == "__main__":
    roll()
