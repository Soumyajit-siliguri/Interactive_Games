
# © Soumyajit Sinha | update entry : 02-05-2020
#hangman game
import random
import time

def play():
    count = 1
    HANGMAN=(
        """
        __________
        |        |
        |
        |
        |
        |
        |
        |
        |
        |
        |
        ______________
        """,
        """
        __________
        |        |
        |        O
        |
        |
        |
        |
        |
        |
        |
        |
        ______________
        """,
        """
        __________
        |        |
        |        O
        |       -+-
        |
        |
        |
        |
        |
        |
        |
        ______________
        """,
        """
        __________
        |        |
        |        O
        |       -+-
        |
        |
        |
        |
        |
        |
        |
        ______________
        """,
        """
        __________
        |        |
        |        O
        |      /-+-
        |     /
        |
        |
        |
        |
        |
        |
        ______________
        """,

        """
        __________
        |        |
        |        O
        |      /-+-|
        |     /    |
        |
        |
        |
        |
        |
        |
        ______________
        """,
        """
        __________
        |        |
        |        O
        |      /-+-|
        |     /  | |
        |        |
        |
        |
        |
        |
        |
        ______________
        """,
        """
        __________
        |        |
        |        O
        |      /-+-|
        |     /  | |
        |        |
        |
        |
        |
        |
        |
        ______________
        """,
         """
        __________
        |        |
        |        O
        |      /-+-|
        |     /  | |
        |        |
        |       /
        |      /
        |     /
        |    
        |
        ______________
        """,
        """
        __________
        |        |
        |        O
        |      /-+-|
        |     /  | |
        |        |
        |       / |
        |      /  |
        |     /   |
        |    
        |
        ______________
        YOU LOST
        """)

    Words=("OVERUSED", "CREAMPIE", "WARRIORS", "ABSOLUTE", "FESTIVAL", "ADDICTED", "DISTRESS")

    time.sleep(0.5)
    print("Start guessing...")
    time.sleep(0.5)
    word = Words[random.randint(0,6)]
    #print(word)
    guesses =[]
    turns = 11
    hold = ["_","_","_","_","_","_","_","_"]
    while turns>0 :
        guess= input("Guess the letter.")[0]
        guesses.append(guess)
        flag=0
        for a in word:
            if guess==a:
                flag=flag+1
        if flag==0:
            print(HANGMAN[(10-turns+1)], "\nWrong guess, this letter doesnt exist in the word.")
        j=0
        for a in word:
            for b in guesses:
                if b==a:
                    hold[j]=b
            j=j+1
        print("The word guessed so far is = ", hold)
        flag2=0
        for c in hold:
            if c=="_":
                flag2=flag2+1
        if flag2 == 0:
            print("---YOU WON---\nYes, the word was ", word )
            break
        turns=turns-1
    flag3=0
    for c in hold:
        if c=="_":
            flag3=flag3+1
    if flag3 != 0:
        print("THE CHARACTER DIED", HANGMAN[9], "\nThe word was ", word)



def makeitplay():
    print("\nWanna play ?")
    decide = input("""
        1. type 'Y' (case sensitive) to play.
        2. press anything else to EXIT
        """)
    if (decide == 'Y'):
        play()
        makeitplay()
    else:
        print("Bye. Thanks for playing.")



print("""Hi! This a model for The-Hangman-Game| Version 1.0 .
      created by SOUMYAJIT SINHA | CGEC CSE 34900118020
      """)
name = input("what is your name?\n")
print("hello", name, """\nThe rules are as follows -
The is a word, you have to guess
PLAY WITH CAPSLOCK ON
WITH EACH LETTER YOU FAIL TO GUESS, THE PERSON GETS MORE CLOSER TO BE HANGED...!!!""")
makeitplay()
