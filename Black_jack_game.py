# Black Jack Card Game
# © Soumyajit Sinha | update entry : 30-May-2020
import time
import random

def drawcard(deck):
    position = random.randrange(len(deck))
    card=deck[position]
    deck=deck[:position] + deck[(position+1):]
    return deck , card

def addtotal(stack):
    total=0
    for i in stack:
        if (i[-1]) in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
            total =total+1
        elif (i[-1]) in ('J', 'Q', 'K'):
            total = total+10
        elif (i[-1]) == 'A':
            a = total+11
            b =total+1
            if a <=21 and (21-a)<(21-b):
                total = a
            elif a > 21:
                total = b
            else:
                total = b

    return total

def nextplayerindex(totalplayers, numberofplayers, playerindex):
    if totalplayers[((playerindex+1+numberofplayers)%numberofplayers)].flag ==0:
        return ((playerindex+1+numberofplayers)%numberofplayers)
    elif totalplayers[((playerindex+1+numberofplayers)%numberofplayers)].flag == 1:
        print('Player ', totalplayers[((playerindex+1+numberofplayers)%numberofplayers)].name, 'has LOST, and had been eliminated.')
        return nextplayerindex(totalplayers, numberofplayers, (playerindex +1))




class player(object):
    """Player"""
    def __init__(self, name):
        self.name= name
        self.stack = []
        self.flag = 0

    def joincardtostack(self, card):
        self.stack.append(card)

    def displaycards(self):
        time.sleep(0.3)
        print("The cards hold by\n", self.name, ": ", self.stack, "| Total : ", addtotal(self.stack))
    def markplayer(self):
        if addtotal(self.stack)>=21:
            self.flag = 1

def askcard():
    confirm = None
    while confirm != 'y':
        time.sleep(0.3)
        confirm = input("You need to draw a card. Confirm (press Y)\n").lower()
        if confirm != 'y':
            time.sleep(0.3)
            print("please confirm")


def role(khiladi, DECK):
    time.sleep(0.3)
    print("Now its the turn for :", khiladi.name)
    khiladi.displaycards()
    if not addtotal(khiladi.stack) > 21:
        askcard()
        DECK, card = drawcard(DECK)
        khiladi.joincardtostack(card)
        khiladi.displaycards()
    else:
        time.sleep(0.3)
        print("Player ", khiladi.name, "has last and had been eliminated.")
    khiladi.markplayer()

    return DECK


def makeitplay():
    time.sleep(0.5)
    print("\nWanna play ?")
    decide = input("""1. type 'Y' / 'y' to play.
2. press anything else to EXIT
""")
    decide=decide.lower()
    if (decide == 'y'):
        play()
        makeitplay()
    else:
        print('Bye. Thanks for playing.')

def newdeck():
    DECKnum = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    DECKcolor = ['Diamond', 'Hearts', 'Spades', 'CLub']
    DECK = []
    for i in DECKcolor:
        for j in DECKnum:
            card = i+j
            DECK.append(card)

    return  DECK



def play():

    DECK = newdeck()
    numberofplayers = None
    while numberofplayers not in range(2,8):
        numberofplayers = int(input("No. of players? (2-7)"))
        if numberofplayers not in range(2,8):
            time.sleep(0.3)
            print("Please select the number of players, in the range 2-7\n")
    instructions()
    totalplayers = []
    playernow = player(name)
    DECK, card = drawcard(DECK)
    playernow.joincardtostack(card)
    DECK, card = drawcard(DECK)
    playernow.joincardtostack(card)
    totalplayers.append(playernow)
    for i in range(2, (numberofplayers+1)):
        playername = input("Name of the player : \n")
        playernow = player(playername)
        DECK, card = drawcard(DECK)
        playernow.joincardtostack(card)
        DECK, card = drawcard(DECK)
        playernow.joincardtostack(card)
        totalplayers.append(playernow)


    playerindex = 0
    WIN = False
    while WIN != True:
        DECK = role(totalplayers[playerindex], DECK)
        playerreference = playerindex
        playerindex = nextplayerindex(totalplayers, numberofplayers, playerindex)
        if len(DECK) == 0:
            time.sleep(0.3)
            print("DECK expired, providing a new DECK.")
            DECK = newdeck()
        elif playerreference == playerindex:
            time.sleep(0.3)
            print(totalplayers[playerreference].name, "Has WON this round.")
            WIN = True
        else:
            WIN = False


def instructions():
    print("""
    Each player starts with 2 cards.
    All numbered cards holds the score 1 each
    ALL J, Q, K hold the score 10 each
    Ace holds Score 11 or 1 as the game requires or proceeds, and advantages the player.
    
    The players tries to keep the score lower than 21.
    If the Score reaches 21 or more, the player is eliminated.
    The Last player existing is the Winner.
    
    So, lets play !!!""")



print("""Hi! This a model for The Black Jack Card Game| Version 1.0 .
      created by SOUMYAJIT SINHA | CGEC CSE 34900118020
      """)
time.sleep(0.5)
name = input("what is your name?\n")
makeitplay()
