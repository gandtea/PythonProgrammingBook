# Chapter 3, Challenge 2
# Flip A Coin program
# Write a program that flips a coin 100 times and then tells you the number of heads and tails.

import random

count = 0
heads = 0
tails = 0

while count != 100:
    count += 1
    flip = random.randint(1,2)
    if flip == 1:
        heads += 1
    else:
        tails += 1

print("Total heads flipped: ", heads)
print("Total tails flipped: ", tails)

input("\n\nPress the enter key to exit.")
