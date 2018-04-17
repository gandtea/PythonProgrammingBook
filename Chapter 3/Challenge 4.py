# Computer guesses number game

import random

# The computer asks what numbers to guess between and use the limits
# for the computer to select min and max numbers of random number generation.
high = int(input("What is the highest number I should guess to? "))
low = int(input("What is the lowest number I should guess to? "))


actual = True
# while guess is incorrect:

while actual:
# edit the upper and lower limits of the random number gen.
    guess = random.randint(low, high)
    print("\nMy guess is ", guess)
    actual = input("\nIs my number correct? Y or N? ")
    if actual.title() == 'Y':
        print("Yey! I got it right!")
        break
    hORl = input("Should I guess higher or lower? H or L? ")
    if hORl.title() == 'H' or hORl.title() == 'Higher':
        low = guess + 1
    elif hORl.title() == 'L' or hORl.title() == 'Lower':
        high = guess - 1

input("\n\nPress the enter key to exit.")
