# Chapter 3, Challenge 1
# Fortune Cookies Generator 
# Write a program that simulates a fortune cookie. 
# The program should display one of five unique fortunes, at random, each time it's run.

import random

print("This fortune cookie generator will tell you your fortune.\n")

fortune = random.randint(1,5)

fortune1 = "You will be hungry 1 hour from now."
fortune2 = "Some fortune cookies contain no fortune."
fortune3 = "You will learn how to use the random generator."
fortune4 = "If you haven't alread, you will eat a fortune cookie."
fortune5 = "You will be truly happy for the rest of your life."

if fortune == 1:
    print(fortune1)
elif fortune == 2:
    print(fortune2)
elif fortune == 3:
    print(fortune3)
elif fortune == 4:
    print(fortune4)
else:
    print(fortune5)

input("\n\nPress the enter key to exit.")
