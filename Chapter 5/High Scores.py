# High Scores
# Demonstrates list methods

scores =[]

choice = None

while choice != "0":
    
    print(
        """
\tHigh Scores

\t0 - Exit
\t1 - Show Scores
\t2 - Add a Score
\t3 - Remove a Score
\t4 - Sort Scores
    """)
    choice = input("Choice: ")
    print()

    # exit
    if choice == "0":
        print("Goodbye!")

    # list high-score table
    elif choice == "1":
        print("High Scores:")
        for score in scores:
            print(score)

    # add a score
    elif choice == "2":
        score = int(input("What score did you get?: "))
        scores.append(score)

    # remove a score
    elif choice == "3":
        score = int(input("Which score would you like to remove?: "))
        if score in scores:
            scores.remove(score)
        else:
            print(score, "isn't in the high scores list.")

    # sort scores
    elif choice == "4":
        scores.sort(reverse=True)

    # some unknown choice
    else:
        print("Sorry, but", choice, "isn't a valid choice.")

input("\n\nPress enter to exit.")

        
