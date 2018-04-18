# Chapter 4, Challenge 3
# Word Jumble, with hints and points
# Improve "Word Jumble" so that each word is paired with a hint. 
# The player should be able to see the hint if he or she is stuck. 
# Add a scoring system that rewards players who solve a jumble without asking for a hint.

import random

WORDS = ("purple", "jumble", "easy", "difficult", "answer", "xylophone")
HINTS = ("colour", "game", "not difficult", "not easy", "???", "instrument")

# pick one word randomly from the sequence
index = random.randint(0,len(WORDS))
word = WORDS[index]
hint = HINTS[index]

# create a variable to uses later to see if the guess is correct
correct = word

# create a variable so the hint only gets given once
given_hint = False

# create a jumbled version of the word
jumble = ''
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# start the game
print(
"""
        Welcome to Word Jumble with hints!

    Unscramble the letters to make a word.
You'll be offered a hint:
         if you use it, you'll get fewer points.
(Press the enter key at the prompt to quit.)
"""
)
print("The jumble is:", jumble)

guess = input("Your guess?: ")

while guess != correct and guess != "":
    print("Sorry, that's not it.\n")
    if given_hint == False:
        want_hint = input("Do you want a hint? y or n: ")
        if want_hint.lower() == "y" or want_hint.lower() == "yes":
            print("Your hint is:", hint)
            given_hint = True
    guess = input("Your guess: ")
    guess = guess.lower()
    
if guess == correct:
    print("That's it! You guessed it!\n")
    if given_hint == False:
        print("You scored the maximum 10 points!")
    else:
        print("You scored 5 points instead of 10 because you used the hint.")
    
print("Thanks for playing.")

input("\n\nPress the enter key to exit.")
