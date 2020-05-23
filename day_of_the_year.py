
Jan = "January"
Feb = "February"
Mar = "March"
Apr = "April"
May = "May"
June = "June"
July = "July"
Aug = "August"
Sep = "September"
Oct = "October"
Nov = "November"
Dec = "December"
MONTH = [Jan, Feb, Mar, Apr, May, June, July, Aug, Sep, Oct, Nov, Dec]
A = [[Jan, 1], [Feb, 4], [Mar, 4], [Apr, 7], [May, 2], [June, 5], [July, 7], [Aug, 3], [Sep, 6], [Oct, 1], [Nov, 4], [Dec, 6]]
B = [[Jan, 2], [Feb, 5], [Mar, 0], [Apr, 0], [May, 0], [June, 0], [July, 0], [Aug, 0], [Sep, 0], [Oct, 0], [Nov, 0], [Dec, 0]]
C = [[Jan, 3], [Feb, 6], [Mar, 0], [Apr, 0], [May, 0], [June, 0], [July, 0], [Aug, 0], [Sep, 0], [Oct, 0], [Nov, 0], [Dec, 0]]
D = [[Jan, 4], [Feb, 7], [Mar, 0], [Apr, 0], [May, 0], [June, 0], [July, 0], [Aug, 0], [Sep, 0], [Oct, 0], [Nov, 0], [Dec, 0]]
E = [[Jan, 5], [Feb, 1], [Mar, 0], [Apr, 0], [May, 0], [June, 0], [July, 0], [Aug, 0], [Sep, 0], [Oct, 0], [Nov, 0], [Dec, 0]]
F = [[Jan, 6], [Feb, 2], [Mar, 0], [Apr, 0], [May, 0], [June, 0], [July, 0], [Aug, 0], [Sep, 0], [Oct, 0], [Nov, 0], [Dec, 0]]
G = [[Jan, 7], [Feb, 3], [Mar, 0], [Apr, 0], [May, 0], [June, 0], [July, 0], [Aug, 0], [Sep, 0], [Oct, 0], [Nov, 0], [Dec, 0]]
H = [[Jan, 1], [Feb, 4], [Mar, 0], [Apr, 0], [May, 0], [June, 0], [July, 0], [Aug, 0], [Sep, 0], [Oct, 0], [Nov, 0], [Dec, 0]]
I = [[Jan, 2], [Feb, 5], [Mar, 0], [Apr, 0], [May, 0], [June, 0], [July, 0], [Aug, 0], [Sep, 0], [Oct, 0], [Nov, 0], [Dec, 0]]
J = [[Jan, 3], [Feb, 6], [Mar, 0], [Apr, 0], [May, 0], [June, 0], [July, 0], [Aug, 0], [Sep, 0], [Oct, 0], [Nov, 0], [Dec, 0]]
K = [[Jan, 4], [Feb, 7], [Mar, 0], [Apr, 0], [May, 0], [June, 0], [July, 0], [Aug, 0], [Sep, 0], [Oct, 0], [Nov, 0], [Dec, 0]]
L = [[Jan, 5], [Feb, 1], [Mar, 0], [Apr, 0], [May, 0], [June, 0], [July, 0], [Aug, 0], [Sep, 0], [Oct, 0], [Nov, 0], [Dec, 0]]
M = [[Jan, 6], [Feb, 2], [Mar, 0], [Apr, 0], [May, 0], [June, 0], [July, 0], [Aug, 0], [Sep, 0], [Oct, 0], [Nov, 0], [Dec, 0]]
N = [[Jan, 7], [Feb, 3], [Mar, 4], [Apr, 7], [May, 2], [June, 5], [July, 7], [Aug, 3], [Sep, 6], [Oct, 1], [Nov, 4], (Dec, 6)]

MONTHS = [A, B, C, D, E, F, G, H, I, J, K , L, M, N]

#MAKING THE TABLE

for i in range(1,13):
    for j in range(2, 12):
        a = (((MONTHS[(i-1)][j][1])+8)%7)
        if a == 0:
            a = 7
        b = (((MONTHS[(i-1)][j][1])+9)%7)
        if b == 0:
            b = 7
        if a == MONTHS[0][j][1]:
            MONTHS[i][j][1]=b
        elif a != MONTHS[0][j][1]:
            MONTHS[i][j][1]=a
        else:
            MONTHS[i][j][1]=MONTHS[i][j][1]


#checking the correctingness
#for i in range(0,14):
#    print("\n--------------", i, "------------\n")
#    print(MONTHS[i])


YEARS = [[A], [B], [C], [K], [F], [G], [A], [I], [D], [E], [F], [N], [B], [C], [D], [L], [G], [A], [B], [J], [E], [F], [G], [H], [C],
         [D], [E], [M]]+[[A], [B], [C], [K], [F], [G], [A], [I], [D], [E], [F], [N], [B], [C], [D], [L], [G], [A], [B], [J], [E], [F], [G], [H], [C],
         [D], [E], [M]]+[[A], [B], [C], [K], [F], [G], [A], [I], [D], [E], [F], [N], [B], [C], [D], [L], [G], [A], [B], [J], [E], [F], [G], [H], [C],
         [D], [E], [M]]+[[A], [B], [C], [K], [F], [G], [A], [I], [D], [E], [F], [N], [B], [C], [D], [E]]
for i in range(0,100):
    YEARS[i].append((2001+i))
#    print("\n",i," :-\t", YEARS[i])


WEEK = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

import time

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
    yyyymmdd = []
    year = None
    month = None
    date = None
    while year not in range(2001, 2101):
        year = int(input("Provide an year (from 2001 to 2100)\n"))
    yyyymmdd.append(year)
    while month not in range(1,13):
        month = int(input("""Provide which month you are looking for :
        1. January
        2. February
        3. March
        4. April
        5. May
        6. June
        7. July
        8. August
        9. September
        10. October
        11. November
        12. December\n"""))
    yyyymmdd.append(MONTH[(month-1)])
    if (year%4) == 0:
        if month == 2:
            while date not in range(1, 30):
                date = int(input("What is the date?\n"))
        elif month in (1, 3, 5, 7, 8, 10, 12):
            while date not in range(1, 32):
                date = int(input("What is the date?\n"))
        elif month in (4, 6, 9, 11):
            while date not in range(1, 31):
                date = int(input("What is the date?\n"))
    else:
        if month == 2:
            while date not in range(1, 29):
                date = int(input("What is the date?\n"))
        elif month in (1, 3, 5, 7, 8, 10, 12):
            while date not in range(1, 32):
                date = int(input("What is the date?\n"))
        elif month in (4, 6, 9, 11):
            while date not in range(1, 31):
                date = int(input("What is the date?\n"))

    yyyymmdd.append(date)

    print("The day you have chosen is : ", yyyymmdd[2], yyyymmdd[1], ", of ", yyyymmdd[0])

    yearmatchlist = yearmatch(year)
    monthmatchnumber = monthmatch(yearmatchlist, month)


    week = ((monthmatchnumber+date+5)%7)
    print("The day for that date is : ", WEEK[week])







def yearmatch(year):
    for i in range(0, 100):
        if YEARS[i][1] == year:
            return YEARS[i][0]


def monthmatch(yearmatchlist, month):
    return yearmatchlist[(month-1)][1]

print("""HI ! I am SINHA's CENTURY CALENDAR ! ! !""")
makeitplay()


