# Chapter 6, Challenge 3
# Modify the new version of Guess My Number you created in the last challenge so that 
# the program's code is in a function called main(). Don't forget to call main() so
# that you can play the game.


import random

def ask_number(question, low, high, step = 1):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high, step):
        print("Guess between", low, "and", high) # added this to help player
        response = int(input(question))
    return response

def main():
    print("\tWelcome to 'Guess My Number'!")
    print("\nI'm thinking of a number between 1 and 100.")
    print("Try to guess it in as few attempts as possible.\n")

    # set the initial values
    the_number = random.randint(1, 100)
    low = 1
    high = 100
    guess = ask_number("Take a guess: ", low, high) 
    tries = 1

    # guessing loop
    while guess != the_number:
        if guess > the_number:
            print("Lower...")
            high = guess # player guessed too high, so high variable changed
        else:
            print("Higher...")
            low = guess # player guess too low, so low variable changed

        guess = ask_number("Take a guess: ", low, high)
        tries += 1

    print("You guessed it! The number was", the_number)
    print("And it only took you", tries, "tries!\n")


main()
input("\n\nPress the enter key to exit.")
