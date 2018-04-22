# Chapter 8, Challenge 4
# Critter Farm Caretaker
# A few virtual pet to take care for

import random

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        hunger = random.randint(0,5)
        self.hunger = hunger
        boredom = random.randint(0,5)
        self.boredom = boredom

    def __str__(self):
        line = "Critter object\n"
        line += "Name: " + self.name + "\n"
        line += "Hunger level: " + str(self.hunger) + "\n"
        line += "Boredom level: " + str(self.boredom) + "\n"
        line += "Total unhappiness level: " + str(self.boredom + self.hunger) + "\n"
        return line

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = 'happy'
        elif 5 <= unhappiness <= 10:
            m = 'OK'
        elif 11 <= unhappiness <= 15:
            m = 'frustrated'
        else:
            m = 'mad'
        return m

    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time()

    def eat(self, food = 4):
        print("Brrruppp. Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print("Wheeee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    crit1_name = input("What do you want to name your 1st critter?: ")
    crit2_name = input("What do you want to name your 2nd critter?: ")
    crit3_name = input("What do you want to name your 3rd critter?: ")
    crit1 = Critter(crit1_name)
    crit2 = Critter(crit2_name)
    crit3 = Critter(crit3_name)
    
    choice = None
    while choice != '0':
        print("""\t\tCritter Caretaker

        0 - Quit
        1 - Listen to your critters
        2 - Feed your critters
        3 - Play with your critters\n""")

        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Goodbye.")

        # listen to your critter
        elif choice == "1":
            print(crit1_name, "says:")
            crit1.talk()
            print(crit2_name, "says:")
            crit2.talk()
            print(crit3_name, "says:")
            crit3.talk()

        # feed your critter
        elif choice == "2":
            food = int(input("How much food would you like to give? Give value "
                         "between 1 and 6: "))
            while not (food <= 6 and food >= 1):
                print("That was an invalid choice.")
                food = int(input("How much food would you like to give? Give value "
                         "between 1 and 6: "))
            crit1.eat()
            crit2.eat()
            crit3.eat()

        # play with your critter
        elif choice == "3":
            fun = int(input("How long would you like to play? Give value "
                         "between 1 and 6: "))
            while not (fun <= 6 and fun >= 1):
                print("That was an invalid choice.")
                fun = int(input("How long would you like to play? Give value "
                         "between 1 and 6: "))
            crit1.play()
            crit2.play()
            crit3.play()

        elif choice == "4":
            print(crit1)
            print(crit2)
            print(crit3)

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
("\n\nPress the enter key to exit.")
