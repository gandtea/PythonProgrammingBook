# Chapter 2, Challenge 3
# Write a Tipper program where the user enters a restaurant bill total. 
# The program should then display two amounts: a 15 percent tip and a 20 percent tip.

total = int(input("How much is your total? "))
print("Please tip either 15% - £", 0.15 * total, \
      " or 20% - £", 0.2 * total, sep='')

input("\n\nPress the enter key to exit.")
