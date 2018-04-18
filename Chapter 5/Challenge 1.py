# Chapter 5, Challenge 1

# Create a program that prints a list of words in a random order.
# The program should print all the words and not repeat any.

import random
words = ['word1', 'word2', 'hate', 'bronchitis', 'blue']

for i in range(len(words)):
    word = random.choice(words)
    print(word)
    words.remove(word)

input("\n\nPress enter to exit.")
