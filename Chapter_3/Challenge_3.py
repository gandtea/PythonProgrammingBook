# Chapter 3, Challenge 3
# Guess My Number with fixed number of tries
# Modify the Guess My Number game so that the player has a limited number of guesses. 
# If the player fails to guess in time, the program should display an appropriately chastising message.

import random

print("\tWelcome to 'Guess My Number in 8 tries'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.")
print("You have 8 tries to get it right!\n")

# set the initial values
the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1

# guessing loop
while guess != the_number and tries < 8:
    if guess == the_number:
        break
    print("You've had ", tries, " try/tries so far! Only ", 8 - tries, " try/tries left!")
    if guess > the_number:
        print("Lower...\n")
    else:
        print("Higher...\n")
    tries += 1
    guess = int(input("Take a guess: "))

if guess == the_number:
    print("\nYou guessed it! The number was", the_number)
    print("And it only took you", tries, "tries!")
else:
    print("You ran out of tries, you suck!")
    print("The number was", the_number)

input("\n\nPress the enter key to exit.")
