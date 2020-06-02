# Call-Bridge Card Game
# © Soumyajit Sinha | update entry : 31-May-2020
import time
import random

DHSC = ('D', 'H', 'S', 'C')

class player(object):
    """Player"""
    def __init__(self, name):
        self.name= name
        self.stack = []
        self.flag = 0
        self.call = 0
        self.score = 0
        self.points = 0


    def joincardtostack(self, card):
        self.stack.append(card)

    def calculatescore(self):
        if self.points<self.call:
            self.score = self.score + ((-1)*self.call)
        else:
            self.score = self.score + (self.call) + ((self.points - self.call)/10)

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
    DECKnum = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    DECKcolor = ['Diamond', 'Hearts', 'Spades', 'CLub']
    DECK = []
    for i in DECKcolor:
        for j in DECKnum:
            card = i+' '+j
            DECK.append(card)

    return  DECK

def startplayer(candidate, DECK):
    for i in range(0, 13):
        DECK, card = drawcard(DECK)
        candidate.joincardtostack(card)
    return DECK

def drawcard(deck):
    position = random.randrange(len(deck))
    card=deck[position]
    deck=deck[:position] + deck[(position+1):]
    return deck, card


def play():

    DHSC = ('D', 'H', 'S', 'C')
    totalplayers =[]

    gamechoice = None
    while gamechoice not in (1, 2, 3, 4):
        gamechoice = int(input("""
        What kind of match do you want to play?
        press 1 : Easy (5 Matches)
        press 2: Intermediate (10 Matches)
        Press 3: Hard (15 Matches)
        Press 4: Quickie (1 Match)\n"""))
        if gamechoice not in (1, 2, 3, 4):
            print("Please choose the game type, in 1, 2, 3 or 4.")

    playernow = player(name)
    totalplayers.append(playernow)

    for i in range(1,4):
        playername = input("What is name of the Player :\n")
        playernow = player(playername)
        totalplayers.append(playernow)


    if gamechoice == 1:
        gamechoice = 5
    elif gamechoice ==2:
        gamechoice = 10
    elif gamechoice == 3:
        gamechoice = 20
    elif gamechoice == 4:
        gamechoice = 1


    for match in range (0, gamechoice):
        print("\n------------\n------------\nM A T C H", (match+1))
        if ((match+4)%4) == 0:
            Trump = 'Diamond'
        elif ((match+4)%4) == 1:
            Trump = 'Hearts'
        elif ((match+4)%4) == 2:
            Trump = 'Spades'
        elif ((match+4)%4) == 3:
            Trump = 'Clubs'

        print("For this match, the TRUMP CARD will be", Trump)

        instruction()

        TOTALDECK = newdeck()
        for i in range (0, 4):
            TOTALDECK = startplayer(totalplayers[i], TOTALDECK)

        #place call
        for i in range(0, 4):
            print("\nOk, so player, ", totalplayers[i].name, "Here is your deck :\n", totalplayers[i].stack)
            call = None
            while call not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11):
                call = int(input("What call do you want to place? (1-11):\n"))
                if call not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11):
                    print("Please make call in range (1 to 11)")

            totalplayers[i].call = call
            print("Player ", totalplayers[i].name, ". You have made a call of ", totalplayers[i].call, "\n")

        playerstarter = 0
        for i in range(0, 13):
            print("\nRound ", (i+1))
            game = []
            playerstarter = playround(game, totalplayers, playerstarter, Trump)


        for i in range(0, 4):
            totalplayers[i].stack = []
            totalplayers[i].calculatescore()
            print("\nPlayer ", totalplayers[i].name, "scored : ", totalplayers[i].score, " in this match ", (match+1), "\n")


    displaywinner(totalplayers)


def displaywinner(totalplayers):
    highscore = 0
    for i in range(0,4):
        if totalplayers[i].score> highscore:
            score = totalplayers[i].score
            winnername = totalplayers[i].name

    print("\n-------------------------------------------\n--------------------------------\n---------------------------------\n", winnername, ", W O N . . . . with a score of ", score, "\n")


def instruction():
    print("""
    RULE FOR THE GAME
    A > K > Q > J > 10 > 9 > 8 > 7 > 6 > 5 > 4 > 3 > 2   in terms of value
    The Player initially makes a Call, i.e the expected number of wins in a match
    For Each Round the Starter Player (Winner of the previous round) selects the COLOUR TYPE of the Card.
    Every Other Player needs to give cards matching with the Card Type.
    Card with the highest value, sets the winner of the round.
    If the Players dont have Card of same type, They Can Use Cards of TRUMP type.
    Any TRUMP card has always more value than other regular Card types.
    If Two or more player happen to give TRUMP CARDs then, 
    Trump Card with higher value is considered winning card.
    
    Let's Start this match !!\n
    """)

def playround(game, totalplayers, playerstarter, trump):
    playerindex = (playerstarter+4)%4
    #player gives card
    card = starterpullcard(totalplayers, playerindex)
    game.append(card)
    print("\t\tCARDS of This Round, on the Table :- ", game)

    playerindex = (playerindex+5)%4
    #player gives card
    card = pullcard(totalplayers, playerindex, trump, game)
    game.append(card)
    print("\t\tCARDS of This Round, on the Table :- ", game)


    playerindex = (playerindex+5)%4
    #player gives card
    card = pullcard(totalplayers, playerindex, trump, game)
    game.append(card)
    print("\t\tCARDS of This Round, on the Table :- ", game)

    playerindex = (playerindex+5)%4
    #player gives card
    card = pullcard(totalplayers, playerindex, trump, game)
    game.append(card)
    print("\t\tCARDS of This Round, on the Table :- ", game)

    #find the winnerindex (playerstarter + gamewinnerindex)
    gamewinnerindex = findwinner(game, trump)
    winnerindex = ((playerstarter + gamewinnerindex + 4)%4)
    print("\nFor this Round, the winner is ", totalplayers[winnerindex].name, "\n Prepare for next round")
    totalplayers[winnerindex].points = totalplayers[winnerindex].points + 1
    #winnerindex in game = playerstarter
    playerstarter = winnerindex

    return playerstarter


def findwinner(game, trump):

    trumpcount = 0
    for i in game:
        if i[0] == trump[0]:
            trumpcount = trumpcount+1


    if game[0][0] == game[1][0] == game[2][0] == game[3][0]:
        highest = 0
        gamewinnerindex = None
        for i in range(0, 4):
            if assignvalue(game[i][-1]) > highest:
                highest = assignvalue(game[i][-1])
                gamewinnerindex = i

    elif trumpcount>0:
        highest = 0
        gamewinnerindex = None
        for i in range(0, 4):
            if game[i][0] == trump[0]:
                if assignvalue(game[i][-1]) > highest:
                    highest = assignvalue(game[i][-1])
                    gamewinnerindex = i

    elif trumpcount == 0:
        highest = 0
        gamewinnerindex = None
        for i in range(0, 4):
            if game[0][0] == game[i][0]:
                if assignvalue(game[i][-1]) > highest:
                    highest = assignvalue(game[i][-1])
                    gamewinnerindex = i

    return gamewinnerindex

def assignvalue(x):
    if x == '2':
        x = 2
    elif x == '3':
        x = 3
    elif x == '4':
        x = 4
    elif x == '5':
        x = 5
    elif x == '6':
        x = 6
    elif x == '7':
        x = 7
    elif x == '8':
        x = 8
    elif x == '9':
        x = 9
    elif x == '0':
        x = 10
    elif x == 'J':
        x = 11
    elif x == 'Q':
        x = 12
    elif x == 'K':
        x = 13
    elif x == 'A':
        x = 14

    return x

def starterpullcard(totalplayers, playerindex):
    print("\nPlayer",totalplayers[playerindex].name, "presently you have the following cards :-\n", totalplayers[playerindex].stack)
    stackindex = None
    while stackindex not in range(0, len(totalplayers[playerindex].stack)):
        stackindex = int(input("Which card index you want to place? (indexing starts from 0)\n"))
        if stackindex not in range(0, len(totalplayers[playerindex].stack)):
            print("Index not valid. choose again")

    card=totalplayers[playerindex].stack[stackindex]
    totalplayers[playerindex].stack=totalplayers[playerindex].stack[:stackindex] + totalplayers[playerindex].stack[(stackindex+1):]
    return card


def pullcard(totalplayers, playerindex, trump, game):
    print("\nPlayer",totalplayers[playerindex].name, "presently you have the following cards :-\n", totalplayers[playerindex].stack)

    stackindex, card = check(totalplayers, playerindex, trump, game)
    totalplayers[playerindex].stack=totalplayers[playerindex].stack[:stackindex] + totalplayers[playerindex].stack[(stackindex+1):]
    return card

def check(totalplayers, playerindex, trump, game):
    count = 0
    for i in totalplayers[playerindex].stack:
        if i[0] == game[0][0]:
            count = count+1

    if count>0:
        stackindex = None
        while stackindex not in range(0, len(totalplayers[playerindex].stack)):
            stackindex = int(input("Which card index you want to place? (indexing starts from 0)\n"))
            if stackindex not in range(0, len(totalplayers[playerindex].stack)):
                print("Index not valid. choose again")

        card=totalplayers[playerindex].stack[stackindex]
        if card[0] != game[0][0]:
            print("The Game is played with '", game[0][0], "'. Please select other card.\n")
            stackindex, card = check(totalplayers, playerindex, trump, game)
    elif count == 0:
        print("Since you dont have card of same colour, you can choose a TRUMP Card.\n")
        trumpcount = 0
        for i in totalplayers[playerindex].stack:
            if i[0] == trump[0]:
                trumpcount = trumpcount+1

        if trumpcount>0:
            stackindex = None
            while stackindex not in range(0, len(totalplayers[playerindex].stack)):
                stackindex = int(input("Which card index you want to place? (indexing starts from 0)\n"))
                if stackindex not in range(0, len(totalplayers[playerindex].stack)):
                    print("Index not valid. choose again")

            card = totalplayers[playerindex].stack[stackindex]
            if card[0] != trump[0]:
                print("YOu have Trump Cards. Please Select from those.\n")
                stackindex, card = check(totalplayers, playerindex, trump, game)

        elif trumpcount == 0:
            print("You neither have Trump Card nor Any Card of Same colour. Select Any Card\n")
            stackindex = None
            while stackindex not in range(0, len(totalplayers[playerindex].stack)):
                stackindex = int(input("Which card index you want to place? (indexing starts from 0)\n"))
                if stackindex not in range(0, len(totalplayers[playerindex].stack)):
                    print("Index not valid. choose again")

            card = totalplayers[playerindex].stack[stackindex]

    return stackindex, card






print("""Hi! This a model for The Call-Bridge Card Game| Version 1.0 .
      created by SOUMYAJIT SINHA | CGEC CSE 34900118020
      """)
time.sleep(0.5)
name = input("what is your name?\n")
makeitplay()
