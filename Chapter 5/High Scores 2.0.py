# High Scores 2.0
# Demonstrates nested sequences

scores =[]

choice = None
while choice != "0":
    
    print("""
\tHigh Scores 2.0

\t0 - Quit
\t1 - List Scores
\t2 - Add a Score
          """
          )
    choice = input("\nChoice: ")
    print()

    # exit
    if choice == "0":
        print("Goodbye!")

    # display high-score table
    elif choice == "1":
        print("High Scores:")
        print("NAME\tSCORE")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)

    # add a score
    elif choice == "2":
        name = input("What is the player's name?: ") 
        score = int(input("What score did they get?: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]   # Keep only top 5 scores

    # some unknown choice
    else:
        print("Sorry, but", choice, "isn't a valid choice.")

input("\n\nPress enter to exit.")
