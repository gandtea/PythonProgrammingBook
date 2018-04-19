# Chapter 5, Challenge 2
# Write a CharacterCreate Program for a role-playing game.
# The player should be given a pool of 30 points to spend on four attributes:
    # Strength, Health, Wisdom, and Dexterity
# The player should be able to spend points from the pool on any attribute
# and should also be able to take points from an attribute and put them back
# in the pool.

print("""
            CHARACTER CREATOR PROGRAM

You have 30 points in a pool to spend as you wish on the attributes:
    Strength, Health, Wisdom, Dexterity.
If you choose to, you can then take points from an attribute and put them back
in the pool.
"""
      )

attributes = {'strength':0, 'health':0, 'wisdom':0, 'dexterity':0}
pool = 30
spend  = None
choice = None

choice_sentence = """
\n\nWhat would you like to do?
0 - Exit
1 - Spend points on an attribute
2 - Put points into pool
"""

attribute_list = """\tStrength
\tHealth
\tWisdom
\tDexterity
"""

while choice != "0":
    print("\nYour character has the following attributes:")
    for attribute, points in attributes.items():
        print("\t",attribute.title(), ":  \t ", points, sep = "")
    print("\nThere are ", pool, " points in the pool.", sep="")
    print(choice_sentence)
    choice = input("Choice: ")
    while choice != "0" and choice != "1" and choice != "2":
        print("Invalid choice")
        print(choice_sentence)
        choice = input("Choice: ")
    while choice == "1": # spend points on an attribute
        if pool == 0: # no points to spend
            print("Sorry, you don't have enough points. Try putting some points"
                  "in the pool")
            break
        print("\nYou have ", pool, " points left in pool.", sep="")
        print("\nWhich attribute would you like to add to?")
        print(attribute_list)
        att_to_change = input("Attribute to change: ")
        while (att_to_change.title() != "Strength" and
            att_to_change.title() != "Health" and
            att_to_change.title() != "Wisdom" and
            att_to_change.title() != "Dexterity"):
            print("That is an invalid choice.")
            print("Which attribute would you like to add to?")
            print(attribute_list)
            att_to_change = input("Attribute to change: ")
        else:
            points = int(input("How many points would you like to spend?: "))
            while points > pool:
                print("That's too many points. You have", pool, "to spend")
                points = int(input("How many points would you like to spend?: "))
        attributes[att_to_change] += points
        pool -= points
        print("\nYour attributes")
        for attribute, points in attributes.items():
            print("\t", attribute.title(), ":  \t", points, sep="")
        if pool == 0:
            print("\nYou've spent all your points.")
            choice = None
            break
        another_change = input("Want to change another attribute? Yes or No: ")
        while another_change.title() != "Yes" and another_change.title() != "No":
            print("That's an invalid choice.")
            another_change = input("Want to change another attribute? Yes or No: ")
        if another_change.title() == "No":
            break

    while choice == "2": # add points to pool
        if pool == 30: # pool already full
            print("\nSorry, you have no points in your attributes."
                  "\nTry adding some points to your attributes first.")
            break
        print("\nWhich attribute would you like to take points out of?")
        for attribute, points in attributes.items():
            print(attribute.title(), ":\t", points, sep="")
        att_to_change = input("Choice: ")
        while (att_to_change.title() != "Strength" and
        att_to_change.title() != "Health" and
        att_to_change.title() != "Wisdom" and
        att_to_change.title() != "Dexterity"):
            print("\nThat is an invalid choice.")
            print("\nWhich attribute would you like to take points out of?")
            for attribute, points in attributes.items():
                print(attribute.title(), ":\t", points, sep="")
            att_to_change = input("Choice: ")
        while attributes[att_to_change] == 0:
            # no points can be removed
            print("You don't have any points in that attribute.")
            att_to_change = input("Choice: ")
            while (att_to_change.title() != "Strength" and
        att_to_change.title() != "Health" and
        att_to_change.title() != "Wisdom" and
        att_to_change.title() != "Dexterity"):
                print("That is an invalid choice.")
                print("Which attribute would you like to take points out of?")
                att_to_change = input("Choice: ")
        points = int(input("\nHow many points would you like to remove?: "))
        while points > attributes[att_to_change]:
            # not enough points in attribute
            print("Sorry, that's too many points! You only have",
                  attributes[att_to_change], "in", att_to_change)
            points = int(input("\nHow many points would you like to remove?: "))
        print("OK!")
        pool += points
        attributes[att_to_change] -= points
        print("You now have ", pool, " points left in your pool.", sep="")
        another_change = input("\nWant to change another attribute? Yes or No: ")
        while another_change.title() != "Yes" and another_change.title() != "No":
            print("That's an invalid choice.")
            another_change = input("Want to change another attribute? Yes or No: ")
        if another_change.title() == "No":
            break
            
print("Goodbye")

input("\n\nPress enter to exit.")
