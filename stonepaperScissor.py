# To mimic the stone paper scissor game.
# © Soumyajit Sinha | update entry : 02-01-2020

# cases involved:-
# 1. p>st
# 2. st>sc
# 3. sc>p

# input- choice, 'play'
# ouput- numbers displayed , asking (play again? OR exit?)

import random

def game():
    comp= ((random.randint(0,20))%3)
    choice=((int(input("""\nWHAT IS YOUR INPUT
    1. Rock 2. Paper 3. Scissor\n""")))%3)

    option=number(comp)
    print('\nThe computer genrated : ', option)
    option=number(choice)
    print('Your choice was : ', option)

    if (choice==comp):
        print("\nDRAW")
    else:
        if (comp==1):
            if (choice==2):
                print("You WON")
            else:
                print("you LOST")
        elif (comp==2):
            if (choice==0):
                print("You WON")
            else:
                print("you LOST")
        elif (comp==0):
            if (choice==1):
                print("You WON")
            else:
                print("you LOST")
        else:
            print("olaoalalal")
    user=(input("""DO you Want to play Again?\nPress Y/y\n"""))
    if (user=='Y' or user=='y'):
        game()
    else:
        print("Bye bye!")

def number(x):
    if (x==1):
        return 'Rock'
    elif (x==2):
        return 'Paper'
    elif (x==0):
        return 'Scissor'
    else:
        print("olaola")



print("""Hi, this a virtual Stone Paper Scissor game, created by Soumyajit Sinha.\nLets Play.\n""")
game()
