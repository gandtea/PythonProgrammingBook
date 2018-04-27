# Chapter 9, Challenge 4
# Create a simple adventure game using objects, where a player can travel
# between various, connected locations.

import games, random, grammar

class NW_Player(object):
    """ A New Worlds Player """

    def __init__(self, name, location = None):
        self.name = name
        locations = []
        for i in NW_World.LOCAL_LINKS.keys():
            locations.append(i)
        location = random.choice(locations)
        self.location = location
        
        print("A new player", self.name.title(), "has arisen from the ground"
              " of", self.location)

    def __str__(self):
        rep = self.name.title() + "'s location is "
        rep += self.location
        return rep

    def move(self, new_location):
        print(self.name, "has moved from", self.location, "to", new_location)
        self.location = new_location

    def say_hi(self, players):
        players_in_location = []
        for player in players:
            if player.location == self.location:
                players_in_location.append(player)
        for player in players_in_location:
            print(self.name.title(), "says hi to", player.name.title())        


class NW_World(object):
    """ A New World location """
    LOCAL_LINKS = {'Andromeda':['Europa', 'Gaia', 'Pluto', 'Poseidon'],
                   'Europa':['Andromeda', 'Gaia'],
                   'Gaia':['Andromeda', 'Europa', 'Poseidon'],
                   'Luna':['Rosa'],
                   'Pluto':['Andromeda', 'Rosa'],
                   'Poseidon':['Andromeda', 'Gaia', 'Rosa'],
                   'Rosa':['Luna', 'Pluto', 'Poseidon']}

    def __init__(self, location, links):
        self.location = location
        self.links = links

    def __str__(self):
        rep = self.location + ' is linked to:\n'
        rep += grammar.comma_and(self.links)
        rep +='\n'
        return rep

# make a list of all players to run in say_hi()
class NW_Game(object):
    """ A New World Game """
    def __init__(self, names):
        self.players = []
        self.worlds = [] # us this with create_worlds
        for name in names:
            player = NW_Player(name)
            self.players.append(player)
          
# when input 'want to move' - show locations of where can move to due to links
# when input 'stay in same place', 
    def instructions(self, player):
        print("\n", player.name.title(), ", you're in ", player.location,
              """. What would you like to do?

Please choose an option:
0 - Drift off into space, never to return
1 = Move location
2 - Stay where you are
3 - Exit game (for all players)

"""
              , sep = "")

    def create_worlds(self):
        """ Create worlds """
        worlds = []
        for location, links in NW_World.LOCAL_LINKS.items():
            worlds.append(NW_World(location, links))
        for world in worlds:
            print(world)
        self.worlds = worlds

    def play(self, players):
        """ Play game """
        choice = None
        while choice != 3:
            sp = self.players[:]
            for player in self.players:
                self.instructions(player)
                choice = games.ask_number("Choice: ", 0, 4)
                if choice == 0:
                    sp.remove(player)
                    print(player.name,
                          "floats away into space, never to return.")
                elif choice == 1:
                    moving = self.move(player)
                    if moving == True:
                        self.say_hi(player)
                elif choice == 2:
                    print("You are in a fabulous location. Good choice.")
                else:
                    choice = 3
                    break
            self.players = sp[:]
            if self.players == []:
                print("\nEveryone has drifted off into space! "
                      "Good byyyyyyyeeeeee!")
                break

    def move(self, player):
        """ Move worlds """
        for world in self.worlds:
            if world.location == player.location:
                print("\n", player, sep = "")
                print("You can travel to:")
                i = 0
                for link in world.links:
                    print(i, ": ", link, sep="")
                    i += 1
                print(i, ": Scrap that, I want to stay in the same place!")
                move_choice = games.ask_number("Choice: ", 0, i+1)
                if move_choice != i:
                    player.location = world.links[move_choice]
                    print("""\n-------> moving worlds -------->\n""")
                    print("New location of ", player.name, ": ", player.location,
                          sep="")
                    moving = True
                else:
                    moving = False
                break

        return moving

    def say_hi(self, player):
        """ Greet other players on same world """
        same_location = []
        for other_player in self.players:
            if other_player != player:
                if other_player.location == player.location:
                    same_location.append(other_player)
        greet_local_op = grammar.comma_and(same_location)
        if same_location != []:
            print(player.name.title(), " greets ", greet_local_op,
                  " on ", player.location, sep="")
                
def main():
    names = []
    players = games.ask_number('how many players? 1-7: ', 1, 7+1)
    print()
    for player in range(players):
        name = input('Enter player name: ')
        names.append(name)
    print()
    game = NW_Game(names)
    print()
    game.create_worlds()

    game.play(players)

main()
input("\n\nPress enter to exit. ")
