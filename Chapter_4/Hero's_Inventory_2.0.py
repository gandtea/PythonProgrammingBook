# Hero's Inventory 2.0
# Demonstrates tuples

# create a tuple with some items and display with a for loop
inventory = ("sword",
             "armour",
             "shield",
             "healing potion")
print("Your items:")
for item in inventory:
    print("\t", item)

input("\nPress the enter key to continue.")

# get the length of a tuple
print("\nYou have", len(inventory), "items in your possesion.")

input("\nPress the enter key to continue.")

# test for membership with in
if "healing potion" in inventory:
    print("You will live to fight another day.")

# display one item through an index
index = int(input("\nEnter the index number for an item in inventory: "))
print("\nAt index", index, "is", inventory[index])

# display a slice
start = int(input("\nEnter the index number to begin a slice: "))
finish = int(input("Enter the index number to end the slice: "))
print("inventory[", start, ":", finish, "] is", end = " ")
print(inventory[start:finish])

input("\nPress the enter key to continue.")

# concatenate two tuples
chest = ("gold", "gems")
print("\nYou find a chest. It contains:")
print(chest)
print("\nYou add the contents of the chest to your inventory.")
inventory += chest
print("Your inventory is now:")
print(inventory)

input("\n\nPress the enter key to exit.")
