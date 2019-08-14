# WHAT FATE LIES BETWEEN YOU AND YOUR DESIRED PERSON| Version 1.0
# Entertainmet purpose.
# © Soumyajit Sinha | update entry : 14-08-2019

#random expriment

# input- names, 'play'
# ouput- story , asking (play again? OR exit?)

import random  #to make the probability game

def play():
    print("Ok,", name, "do you want to play FATE BETWEEN YOU AND YOUR DESIRED PERSON| Version 1.0 again?")
    decission = input("""
     1. type 'Play' (case sensitive) to play.
     2. press anything else to EXIT
        """)
    if (decission == 'Play'):
        num = random.randint(1, 20)

        if (num == 1):
            print(partner, "and ", name, "will have random and wild sex like dogs every now and then.")
        elif (num == 2):
            print(partner, "and", name, "will 2\n")
        elif (num == 3):
            print(partner, "and", name, "will 3\n")
        elif (num == 4):
            print(partner, "and", name, "will 4\n")
        elif (num == 5):
            print(partner, "and", name, "will 5\n")
        elif (num == 6):
            print(partner, "and", name, "will 6\n")
        elif (num == 7):
            print(partner, "and", name, "will 7\n")
        elif (num == 8):
            print(partner, "and", name, "will 8\n")
        elif (num == 9):
            print(partner, "and", name, "will 9\n")
        elif (num == 10):
            print(partner, "and", name, "will 10\n")
        elif (num == 11):
            print(partner, "and", name, "will 11\n")
        elif (num == 12):
            print(partner, "and", name, "will 12\n")
        elif (num == 13):
            print(partner, "and", name, "will 13\n")
        elif (num == 14):
            print(partner, "and", name, "will 14\n")
        elif (num == 15):
            print(partner, "and", name, "will 15\n")
        elif (num == 16):
            print(partner, "and", name, "will 16\n")
        elif (num == 17):
            print(partner, "and", name, "will 17\n")
        elif (num == 18):
            print(partner, "and", name, "will 18\n")
        elif (num == 19):
            print(partner, "and", name, "will 19\n")
        elif (num == 20):
            print(partner, "and", name, "will 20\n")
        else:
            print("")


        play()
    else:
        print("Thank you. BYE, ", name)


print("""Hi! This a model for FATE BETWEEN YOU AND YOUR DESIRED PERSON| Version 1.0 .
      created by SOUYMYAJIT SINHA
      """)
name = input("what is your name?\n")
partner = input("What is the name of your Desired person?\n")

num = random.randint(1, 20)

if (num == 1):
    print(partner, "and ", name, "will have random and wild sex like dogs every now and then.\n")
elif (num == 2):
    print(partner, "and", name, "will 2\n")
elif (num == 3):
    print(partner, "and", name, "will 3\n")
elif (num == 4):
    print(partner, "and", name, "will 4\n")
elif (num == 5):
    print(partner, "and", name, "will 5\n")
elif (num == 6):
    print(partner, "and", name, "will 6\n")
elif (num == 7):
    print(partner, "and", name, "will 7\n")
elif (num == 8):
    print(partner, "and", name, "will 8\n")
elif (num == 9):
    print(partner, "and", name, "will 9\n")
elif (num == 10):
    print(partner, "and", name, "will 10\n")
elif (num == 11):
    print(partner, "and", name, "will 11\n")
elif (num == 12):
    print(partner, "and", name, "will 12\n")
elif (num == 13):
    print(partner, "and", name, "will 13\n")
elif (num == 14):
    print(partner, "and", name, "will 14\n")
elif (num == 15):
    print(partner, "and", name, "will 15\n")
elif (num == 16):
    print(partner, "and", name, "will 16\n")
elif (num == 17):
    print(partner, "and", name, "will 17\n")
elif (num == 18):
    print(partner, "and", name, "will 18\n")
elif (num == 19):
    print(partner, "and", name, "will 19\n")
elif (num == 20):
    print(partner, "and", name, "will 20\n")
else:
    print("")
play()
