# Chapter 4, Challenge 2
# Create a program that gets a message from the user and then prints it out
# backwards.

word = input("What word do you want to print backwards? ")
backwards = ""

for i in word:
    backwards = i + backwards
    
print(backwards)

input("Press enter to exit")
