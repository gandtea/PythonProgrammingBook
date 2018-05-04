# Computer guesses number game
# Write the pseudocode for a program where the player and the computer trade places in the number guessing game. 
# That is, the player picks a random number between 1 and 100 that the computer has to guess. 
# Before you start, think about how you guess. 
# If all goes well, try coding the game.

# Pseudocode
# Computer asks what numbers to guess between
# While the computer has not guessed correctly
    # Computer guesses a number between these numbers
    # Player tells computer whether it has guessed correctly
        # If guesses correctly, computer celebrates and stops program
    # Player tells computer whether the number is higher or lower
    # The computer changes its guess range accordingly

import random

high = int(input("What is the highest number I should guess to? "))
low = int(input("What is the lowest number I should guess to? "))

# while guess is incorrect:
guessed_incorrectly = True

while guessed_incorrectly:
# edit the upper and lower limits of the random number gen.
    guess = random.randint(low, high)
    print("\nMy guess is ", guess)
    is_comp_correct = input("\nIs my number correct? Y or N? ")
    if is_comp_correct.title() == 'Y':
        print("Yey! I got it right!")
        guessed_incorrectly = False
    else:
        hORl = input("Should I guess higher or lower? H or L? ")
        if hORl.title() == 'H' or hORl.title() == 'Higher':
            low = guess + 1
        elif hORl.title() == 'L' or hORl.title() == 'Lower':
            high = guess - 1

input("\n\nPress the enter key to exit.")
