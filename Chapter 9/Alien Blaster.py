# Alien Blaster
# Demonstrates object interaction

class Player(object):
    """A player in a shooter game."""
    def blast(self, enemy):
        print("The player blasts an enemy.\n")
        enemy.die()

class Alien(object):
    """An alien in a shooter game."""
    def die(self):
        print("I died.")  
# main

hero = Player()
invader = Alien()
hero.blast(invader)

input("\n\nPress enter to exit.")
