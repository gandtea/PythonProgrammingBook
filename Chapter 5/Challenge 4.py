# Chapter 5, Challenge 4

# Improve the Who's Your Daddy? program by adding a choice that lets the user
# enter a name and get back a grandfather. Your program should still only use
# one dictionary of son-father pairs. Make sure to include several
# generations in your dictionary so that a match can be found.

sf = {'tom cruise':'antony hopkins', 'boris becker':'tin tin', 'tin tin':'colin dean',
      'sam potts':'simon potts', 'simon potts':'david potts'}
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
5 - Find a Grandfather
""")
    choice = input("Which option would you like to choose? ")
    if choice == "1":
        if sf == {}:
            print("\nThe database is empty right now, why don't you add some!")
            continue
        else:
            for son, father in sf.items():
                print(son.title(), "is", father.title(), "'s son.")
    elif choice == "2":
        son = input("\nWho is the son? ")
        son = son.lower()
        if son in sf:
            print("That son already exists! Try replacing the son instead.")
            continue
        father = input("Who is the father? ")
        father = father.lower()
        sf[son] = father
        print("\n", son.title(), "is", father.title(), "'s son.")
    elif choice == "3":
        sorf = input("\nDo you know the son or father?: ")
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
                print(father, "doesn't exist as a father . Why don't you try adding him?")
    elif choice == "4":
        son = input("\nWho is the son? ")
        son = son.lower()
        if son not in sf.keys():
            print(son, "doesn't exist as a son! Perhaps you already deleted them.")
            continue
        else:
            print(son.title(), "and", sf[son].title(), "have been deleted.")
            del sf[son]
    elif choice == '5':
        son = input("\nWho is the grandson? ")
        son = son.lower()
        if son not in sf.keys():
            print(son.title(), "doesn't exist as a son! Why don't you try adding him?")
        else:
            dad = sf[son]
            if dad not in sf.keys():
                print("Although", son.title(), "is in our dictionary,", 
                      dad.title(), "is not as a son \nwhich is needed to find"
                      " a grandpa! Why don't you add him?")
            else:
                print(sf[dad].title(), " is ", son.title(), "'s Grandad.", sep="")
    else:
        print("Sorry, that's not a valid choice.")
            
print("\nThanks for playing!")
input("\n\nPress enter to exit.")
