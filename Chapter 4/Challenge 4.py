# Chapter 4, Challenge 4
# Create a game where the computer picks a random word and the player has to guess that word. 
# The computer tells the player how many letters are in the word. 
# Then the player gets five chances to ask if a letter is in the word. 
# The computer can only respond with "yes" or "no". 
# Then, the player must guess the word.

import random

print("\t\t'GUESS THE COLOUR GAME!'. \nGuess the colour after "
      "choosing 5 different letters. \nGood luck!\n\n")

words = ('purple', 'black', 'blue', 'turquoise', 'pink', 'yellow', 'green',\
         'white', 'brown', 'orange', 'grey', 'peach')

choice = random.randrange(len(words))
chances = 5
word = words[choice]

print("The length of the word I've chosen is ", len(word))

while chances > 0:
    letter_guess = input("\nWhat letter would you like to guess? ")
    chances = chances - 1
    if letter_guess in word:
        print("That letter is in the word!")
    else:
        print("Nope, not that letter.")

guess = input("\nWhat colour would you like to guess? ")

if guess.lower() == word:
    print("Congratulations! You got it!")
else:
    print("Ah, bummer. You got it wrong. The word was ", word, ".", sep="")

input("\n\nPress enter to exit")
