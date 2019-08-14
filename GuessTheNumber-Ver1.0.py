# Dice Rolling Simulator
# To guess a randomly created number.
# © Soumyajit Sinha | update entry : 14-08-2019

#random expriment for (limited b/w 1-225)

# input- number of dices, 'play'
# ouput- numbers displayed , asking (play again? OR exit?)

###doesn't ask the user if he would want to play more

import random  #to make the probability game

print("""Hi! This a model for GUESS THE NUMBER| Version 1.0 .
      created by SOUYMYAJIT SINHA
      """)
name = input("what is your name?\n")

print("Ok,", name, "do you want to play GUESS THE NUMBER?")
decission = input("""
    1. type 'Play' (case sensitive) to play.
    2. press anything else to EXIT
    """)
#if (decission == 'Play'):

number = random.randint(0, 225)
guess = int(input("Guess the number\n"))
attempt = 1

while (guess!=number):
    attempt = attempt+1
    if (guess>number):
        print("Guess a smaller number!\n")
        guess = int(input("Guess the number\n"))
    elif (guess<number):
        print("Guess a bigger number!\n")
        guess = int(input("Guess the number\n"))
    else:
        print("")

print("Yes you have guessed it right. It is ", number, ". It took you", attempt, "attempts.")
