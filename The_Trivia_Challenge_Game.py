# Trivia Challenge Game
# © Soumyajit Sinha | update entry : 22-May-2020
import time
import  sys


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


def play():
    sinha_trivia_file = open_file("sinha.txt", "r")
    title = next_line(sinha_trivia_file)
    welcome (title)
    score = 0
    score = questionfornext(sinha_trivia_file, score)




def open_file(filename, command):
    """Trivia game that reads a plain text file"""

    try:
        the_file = open(filename, command)
    except IOError as e:
        print("Unable to open the file", filename, ". Terminating the program. ! ! !")
        input("\n\nPress the ENTER key to exit.")
        sys.exit()
    else:
        return the_file


def next_line(filevariable):
    """ return the next line from the textfile"""
    line = filevariable.readline()
    line = line.replace("/", "\n")
    return line

def welcome(text):
    print('\t\tHi,', name, 'Welcome to Sinha\'s Trivia Challenge!\n')
    print("\t\t", text,"\n")

def questionfornext(filename, score):
    time.sleep(0.5)
    print("Ready for next question ?")
    decide = input("""1. type 'Y' / 'y' to confirm.
2. press anything else to EXIT the game
""")
    decide=decide.lower()
    if (decide == 'y'):
        category, question, options, correctoption, answer, explaination = nextblock(filename)
        if category == "......\n":
            print("hehe, there aren's anymore questions, your trivia challenge is complete.\nHere is your score..")
            declarescore(score)


        else:
            print(category)
            print(question)
            for i in range(0, len(options)):
                time.sleep(0.4)
                print(options[i])
            askanswer = None
            while askanswer not in (1, 2, 3, 4):
                askanswer = int(input("Choose you Reply option\n"))
                if askanswer not in (1, 2, 3, 4):
                    print("Your reply is invalid. Try choosing in 1, 2, 3 or 4.\n")

            #checking answer and scoring
            time.sleep(0.4)
            if askanswer == correctoption:
                print("Yes, that's the correct option.")
                score = score+1
            else:
                print("Ooops! That was incorrect.")
            time.sleep(0.4)
            print("The correct answer to this Question is : ", answer)
            time.sleep(0.4)
            print("Logic :\n", explaination)
            score = questionfornext(filename, score)
    else:
        declarescore(score)
    return score


def nextblock(filename):
    """Retieve data from text file"""
    category = next_line(filename)
    question, options, correctoption, answer, explaination = 0, 0, 0, 0, 0
    if category != '......':
        question = next_line(filename)
        options =[]
        for i in range(0,4):
            options.append(next_line(filename))
        try:
            correctoption = int(next_line(filename))
        except ValueError as v:
            correctoption = 0
        answer = next_line(filename)
        explaination = next_line(filename)
    return category, question, options, correctoption, answer, explaination

def declarescore(score):
    print('Well,', name, '. You have made a total score of ', score)



print("""Hi! This a model for Trivia - Challenge Game| Version 1.0 .
      created by SOUMYAJIT SINHA | CGEC CSE 34900118020
      """)
time.sleep(0.5)
name = input("what is your name?\n")
makeitplay()




