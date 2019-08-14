# Dice Rolling Simulator
# To mimic the rolling of dice from (1-6) randomly.
# © Soumyajit Sinha | update entry : 14-08-2019

# cases involved:-
# 1. random experiment for 1 dice
# 2. random experiment for 2 dices
# 3. random expriment for 'n' number of dices (limited b/w 1-25)

# input- number of dices, 'play'
# ouput- numbers displayed , asking (play again? OR exit?)
### shows error of non-termination if number of die are asked, after the value is given beyond range



import random  #to make the probability game

def askdice ():
    dice_number = int(input("How many die you want? (limit- 1 to 25)\n"))
    if (dice_number<0 or dice_number>25):
        print("Not within the range")
        askdice()
    else:
        return (dice_number)

def game():
    print("\t", random.randint(1, 6))

def conduct():
    print("lets play")
    dice_number = askdice()
    print("\nTHE READINGS OF DICE ARE AS FOLLOWS")
    count = 0
    while (count != dice_number):
        game()
        count = count+1
    print("\nWanna play again?")
    decide = input("""
        1. type 'Y' (case sensitive) to play.
        2. press anything else to EXIT
        """)
    if (decide == 'Y'):
        conduct()
    else:
        print("Bye,", name)


print("""Hi! This a model for Dice Rolling Game| Version 1.0 .
      created by SOUYMYAJIT SINHA
      """)
name = input("what is your name?\n")

print("Ok,", name, "do you want to play rolling the dice?")
decission = input("""
    1. type 'Play' (case sensitive) to play.
    2. press anything else to EXIT
    """)
if (decission == 'Play'):
    print("lets play")
    dice_number = askdice()
    print("\nTHE READINGS OF DICE ARE AS FOLLOWS")
    count = 0
    while (count != dice_number):
        game()
        count = count+1
    print("\nWanna play again?")
    decide = input("""
        1. type 'Y' (case sensitive) to play.
        2. press anything else to EXIT
        """)
    if (decide == 'Y'):
        conduct()
    else:
        print("Bye,", name)
else:
   print("Bye", name)


