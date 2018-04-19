# Chapter 5, Challenge 3

# Write a Who's Your Daddy? program that lets the user enter the name of a male
# and produces the name of his father. Allow the user to add, replace, and
# delete son-father pairs.

sf = {'tom cruise':'antony hopkins', 'boris becker':'tin tin'}
son = ''
father = ''
choice = None

while choice != "0":
    print("""\n\nWould you like to:

0 - Exit
1 - View the Son-Father pairs
2 - Add a Son-Father pair
3 - Replace a Son-Father pair
4 - Delete a Son-Father pair
""")
    choice = input("Which option would you like to choose? ")
    if choice == "1":
        if sf == {}:
            print("The database is empty right now, why don't you add some!")
            continue
        else:
            for son, father in sf.items():
                print(son.title(), "is", father.title(), "'s son.")
    elif choice == "2":
        son = input("Who is the son? ")
        son = son.lower()
        if son in sf:
            print("That son already exists! Try replacing the son instead.")
            continue
        father = input("Who is the father? ")
        father = father.lower()
        sf[son] = father
        print("\n", son.title(), "is", father.title(), "'s son.")
    elif choice == "3":
        sorf = input("Do you know the son or father?: ")
        sorf = sorf.lower()
        while sorf != "son" and sorf != "father":
            print("Sorry, please write 'son' or 'father'")
            sorf = input("Do you know the son or father?: ")
            sorf = sorf.lower()
        if sorf == "son":
            son = input("Who is the son? ")
            son = son.lower()
            if son in sf.keys():
                print("This current father is", sf[son].title())
                father = input("Who would you like to replace him with?: ")
                father = father.lower()
                sf[son] = father
                print("The father of", son.title(), "is now", father.title())
            elif son not in sf.keys():
                print("That son doesn't exist. Why don't you try adding him?")
                continue
        if sorf == "father":
            father = input("Who is the dad? ")
            father = father.lower()
            if father in sf.values():
                for son, dad in sf.items(): # find correct father in sf 
                    if dad == father:
                        print("The current son is", son.title())
                        del sf[son] 
                        son = input("Who would you like to replace him with?: ")
                        sf[son] = father
                        print(son.title(), " is ", father.title(), "'s son.")
                        break
            elif father not in sf.values():
                print(father, "doesn't exist. Why don't you try adding him?")
    elif choice == "4":
        son = input("Who is the son? ")
        son = son.lower()
        if son not in sf:
            print(son, "doesn't exist! Perhaps you already deleted them.")
            continue
        else:
            print(son.title(), "and", sf[son].title(), "have been deleted.")
            del sf[son]
    else:
        print("Sorry, that's not a valid choice.")
            
print("\nThanks for playing!")
input("\n\nPress enter to exit.")
