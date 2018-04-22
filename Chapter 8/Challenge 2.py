# Chapter 8, Challenge 2
# Television simulator
# User can enter a channel number and raise or lower the volume

# Create a class television.
# Attributes of the television:
    # Channel number
    # Volume

# Methods for the television:
    # Change channel within allowed limits (enter a number).
    # Change volume within allowed limits (up and down by user).


class Tele(object):
    """A virtual Television"""

    def __init__(self, channel, volume):
        self.channel = channel
        print("Channel:", self.channel)
        self.volume = volume
        print("Volume:", self.volume)

    def chngchan(self, chan_choice):
        self.channel = chan_choice
        print("Channel:", self.channel)

    def chngvol(self, vol_up_down):
        if vol_up_down == 'up':
            if self.volume < 10:
                self.volume += 1
                print("Volume at", self.volume)
            elif self.volume == 10:
                print("Volume at maximum level.")
        elif vol_up_down == 'down':
            if self.volume > 0:
                self.volume -= 1
                print("Volume at", self.volume)
            elif self.volume == 0:
                print("Volume at lowest level.")

def tryint(sentence):
    inttry = input(sentence)
    while True:
        try:
            isinteger = int(isinteger)
            if isinteger > 1 and isinteger < 99:
                return isinteger
            else:
                print("Choice was not between 1 and 99")
                isinteger = input(sentence)
        except ValueError:
            print("Choice was not a number")
            isinteger = input(sentence)

def updown(sentence):
    vol_ud = input(sentence)
    while not (vol_ud == "up" or "down"):
        print("Choice invalid.")
        vol_ud = input(sentence)
    return vol_ud

def main():
    while True:
        print("""Remote control choices:

            0 to change channel
            1 to change volume 
            2 to turn television off.""")
        choice = input("Choice: ")
        while not (choice == '0' or choice == '1' or choice == '2'):
            print("Invalid choice.")
            print("""Remote control choices:

            0 to change channel
            1 to change volume 
            2 to turn television off.""")
            choice = input("Choice: ")
        if choice == '0':
            channel_choice = 'What channel would you like to change to? 0 - 99: '
            chan_choice = tryint(channel_choice)
            television.chngchan(chan_choice)
        elif choice == '1':
            volume_updown = "Press (type) 'up' or 'down': "
            vol_updown = updown(volume_updown)
            television.chngvol(vol_updown)
        elif choice == '2':
            break
# main
television = Tele(1, 3)
main()

input("Press enter to exit")
