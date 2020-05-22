# Jumble up Game
# © Soumyajit Sinha | update entry : 1-May-2020

import random

def makeitplay():
    print("\nWanna play ?")
    decide = input("""1. type 'Y' / 'y' to play.
2. press anything else to EXIT
""")
    decide=decide.lower()
    if (decide == 'y'):
        play()
        makeitplay()
    else:
        print('Bye', name, '. Thanks for playing.')



def play():
    WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone", "tale", "late", "teal")
    word = random.choice(WORDS)
    correct = word
    jumble = ""
    while word:
        position = random.randrange(len(word))
        jumble+=word[position]
        word=word[:position] + word[(position+1):]

    print("The jumbled word is -", jumble)

    flag=0

    while flag <3:
        flag = 0
        guess = input("\nYour guess : \n")
        guess = guess.lower()
        for i in WORDS:
            if guess==i:
                flag=flag+1
        if (len(guess)==len(correct)):
            flag=flag+1
        countercheck=0
        for j in guess:
            if j in correct:
                countercheck=countercheck+1
        if countercheck==len(correct) and countercheck==len(guess):
            flag=flag+1



    if flag>2:
        print("Absolutely correct! That's a correct word possible from the given letters.")






print("""Hi! This a model for The-Jumble-Game| Version 1.0 .
      created by SOUMYAJIT SINHA | CGEC CSE 34900118020
      """)
name = input("what is your name?\n")
print("           Hello", name, """\nThe rules are as follows -
Unscramble the letters to make a word
""")
makeitplay()

