# Interactive pet Game
# © Soumyajit Sinha | update entry : 26-May-2020
import time

class Critter(object):
    """A vitual pet"""
    def __init__(self, name, hunger=0, boredom =0):
        self.name= name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom +=1

    @property
    def mood(self):
        unhappiness = self.boredom + self.hunger

        if unhappiness<5:
            m = 'happy'
        elif 5<=unhappiness<=10:
            m = 'okay'
        elif 11<=unhappiness<=15:
            m = 'frustrated'
        else:
            m = 'mad'
        return  m

    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now\n")
        self.__pass_time()

    def eat(self, food =4):
        print("Burrrpp!! thank you.")
        self.hunger -=4
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def playthepet(self, fun =4):
        print("wheee!!!")
        self.boredom -=4
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()









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
    crit_name = input("What name do you want for your Virtual pet?\n")
    crit = Critter(crit_name)

    choice = None
    while choice != 0:
        print("""
        Virtual Pet Caretaker
        
        0 - quit
        1 - Listen to you virtual pet.
        2 - Feed your virtual pet
        3 - Play with your virtual pet""")

        choice = int(input("choice :\n"))
        if choice == 0:
            print("Good bye. thank you.")
        elif choice==1:
            crit.talk()
        elif choice==2:
            crit.eat()
        elif choice== 3:
            crit.playthepet()
        else:
            print("Invalid choice request. try in 0, 1, 2 or 3")


print("""Hi! This a model for The Critter Caretaker Game| Version 1.0 .
      created by SOUMYAJIT SINHA | CGEC CSE 34900118020
      """)
time.sleep(0.5)
name = input("what is your name?\n")
makeitplay()
