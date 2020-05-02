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
     1. type 'Play' (case sensitive) to try again.
     2. press anything else to EXIT
        """)
    if (decission == 'Play'):
        num = random.randint(1, 5)

        if (num == 1):
            print(partner, "and ", name, "will be making world tour in next decade.\n")
        elif (num == 2):
            print(partner, "and", name, "will be arrested in next 5 years.\n")
        elif (num == 3):
            print(partner, "and", name, "will win a lottery in next 3 years.\n")
        elif (num == 4):
            print(partner, "and", name, "will be sentenced to death, for a serious crime.\n")
        elif (num == 5):
            print(partner, "and", name, "will own a mansion in next 10 years.\n")
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

num = random.randint(1, 5)

if (num == 1):
    print(partner, "and ", name, "will be making world tour in next decade.\n")
elif (num == 2):
    print(partner, "and", name, "will be arrested in next 5 years.\n")
elif (num == 3):
    print(partner, "and", name, "will win a lottery in next 3 years.\n")
elif (num == 4):
    print(partner, "and", name, "will be sentenced to death, for a serious crime.\n")
elif (num == 5):
    print(partner, "and", name, "will own a mansion in next 10 years.\n")
else:
    print("")

play()
