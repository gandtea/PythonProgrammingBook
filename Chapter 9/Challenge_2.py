# Chapter 9, Challenge 2
# Write a one-card version of the game war, where each player gets a single
# card and the player with the highest card wins.

# Requires cards and games modules

import cards, games

# Create a Gamewar_Card class that has a value associated to the card.
class Gamewar_Card(cards.Card):
    """ A Gamewar Card. """

    @property
    def value(self):
        v = Gamewar_Card.RANKS.index(self.rank) + 1
        # Ace is the highest ranking card, so make its value > the king.
        if v == 1:  
            v = 14
        return v

class Gamewar_Deck(cards.Deck):
    """ A Gamewar Deck. """
    def populate(self):
        for suit in Gamewar_Card.SUITS:
            for rank in Gamewar_Card.RANKS:
                self.cards.append(Gamewar_Card(rank, suit))
        

# Create a Gamewar_Hand class that can print the name of the player & the card.
class Gamewar_Hand(cards.Hand):
    """ A Gamewar Hand."""
    def __init__(self, name):
        super(Gamewar_Hand, self).__init__()
        self.name = name
    
    def __str__(self):
        rep = self.name + ":\t" + super(Gamewar_Hand, self).__str__()
        return rep

# Hand needs a value!
    @property
    def value_hand(self):
        for card in self.cards:
            val = card.value
            return val

# Create a class which sets up the deck and has a method for dealing cards to
# the players and a method for checking who has won.

class Gamewar(object):
    """ A game of Game War. """
    def __init__(self, names):

        self.players = []
        for name in names:
            player = Gamewar_Hand(name)
            self.players.append(player)
        
        self.deck = Gamewar_Deck()
        self.deck.populate()
        self.deck.shuffle()

    def play(self):

        if len(self.deck.cards) < len(self.players):
            self.deck.clear()
            self.deck.populate()
            self.deck.shuffle()
        
        self.deck.deal(self.players)
        for player in self.players:
            print(player)

# Determines the winner.
        winners = [] # may be more than one winner.
        max_score = 0
        for player in self.players:
            if max_score < player.value_hand:
                max_score = player.value_hand
        for player in self.players:
            score = player.value_hand
            if score == max_score:
                winners.append(player)
        
        print("\nThe lucky winner(s):")
        for winner in winners:
            print(winner)

        for player in self.players:
            player.clear()
        
# main

# Welcome the players to the game.
print("Welcome to the War Game!\n\n")

# How many players between 1 and 10?
numberofplayers = games.ask_number("How many players would you like to play? 2-52: ", 2, 52)

print()
# Get the names of the players
names = []
for i in range(numberofplayers):
    name = input("Enter player name: ")
    names.append(name)

game = Gamewar(names)

want_to_play = "y"

while want_to_play == "y":
    game.play()
    print()
    want_to_play = games.ask_yes_no('Want to play again? y/n: ')

input('Press enter to exit')
