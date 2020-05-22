# Tic-Tac-toe
# © Soumyajit Sinha | update entry : 21-May-2020
import time

def instructions():
    print(
    """
    You will making your move by entering the location values (0 to 8).
    The numbers will be corresponding to the locations as follows :-
                0 | 1 | 2
                ---------
                3 | 4 | 5
                ---------
                6 | 7 | 8
    Let the battle begin ! ! !
    """)


def makeitplay():
    time.sleep(0.5)
    print("\nWanna play ?")
    decide = input("""1. type 'Y' / 'y' to play.
2. press anything else to EXIT
""")
    decide=decide.lower()
    if (decide == 'y'):
        gametype()
        makeitplay()
    else:
        print('Bye. Thanks for playing.')

def gametype():
    time.sleep(0.5)
    decidegame = int(input("""\nWhat kind of game do you want to play?
1. Player v/s Player 
2. Player v/s Computer
"""))

    if (decidegame == 1):
        play_play()
    elif (decidegame==2):
        play_comp()
    else:
        print("invalid choice")
        gametype()

def play_play():
    time.sleep(0.5)
    print("GAME CHOSEN : P L A Y E R   v/s   P L A Y E R\n-------------------------------------------")
    time.sleep(0.5)
    instructions()
    player1, player2 = pieces()
    turn = X
    board = new_board()
    time.sleep(0.5)
    display_board(board)

    while not winner(board):
        if turn == player1:
            move = player_move(board, player1)
            board[move] = player1
        else:
            move = player_move(board, player2)
            board[move] = player2
        display_board(board)
        turn = next_turn(turn)
        print("NOW player '", turn, "' will make a move")

    the_winner = winner(board)
    congrat_winner(the_winner, player1, player2)


def play_comp():
    time.sleep(0.5)
    print("GAME CHOSEN : P L A Y E R   v/s   C O M P U T E R\n-----------------------------------------------")
    time.sleep(0.5)
    instructions()
    computer, player = pieces()
    turn = X
    board = new_board()
    time.sleep(0.5)
    display_board(board)

    while not winner(board):
        if turn == player:
            move = player_move(board, player)
            board[move] = player
        else:
            move = computer_move(board, computer, player)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
        print("NOW player ", turn, " will make a move\n")

    the_winner = winner(board)
    congrat_winner(the_winner, computer, player)

    if the_winner == computer:
        print("You Fool! you think, you can win over Computer? HAHAHAHA!!!")
    elif the_winner == player:
        print("You indeed are genious. Computer accepts it's defeat. You broke the Silicon's ego.")
    elif the_winner== TIE:
        print("That's the best you can ever get, hehe!")


def pieces():
    """Define the players and choice of 1st move"""
    go_first = ask_yes_no("Do you require the 1st move? (y/n) :\n")
    if go_first.lower() == 'y':
        time.sleep(0.5)
        print(name, ', You will be starting the match then. AS " X ".\n')
        a = X
        b = O
    else:
        time.sleep(0.5)
        print(name, ', OK so you will be having the next move. AS " O ".\n')
        b = X
        a = O
    return b, a

def ask_yes_no(question):
    response = None
    while response not in ('y', 'n',):
        response = input(question).lower()
    return response


def new_board():
    """creates new game board"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    time.sleep(0.5)
    print("\n\t", board[0], " | ", board[1], " | ", board[2])
    time.sleep(0.5)
    print("\t----------------")
    time.sleep(0.5)
    print("\n\t", board[3], " | ", board[4], " | ", board[5])
    time.sleep(0.5)
    print("\t----------------")
    time.sleep(0.5)
    print("\n\t", board[6], " | ", board[7], " | ", board[8], "\n")


def winner(board):
    """Determines ways to win"""
    WAYS_TO_WIN = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
    return None

def player_move(board, human):
    legal = legal_moves(board)
    move = None

    while move not in legal:
        move = ask_number("Where do you want to place your mark? (0-8): \n", 0, NUM_SQUARES)
        if move not in legal:
            print("That location is already marked. Choose another location.\n")
        time.sleep(0.5)
    print("Location accepted...")
    return move

def legal_moves(board):
    """list of acceptable moves"""
    moves = []
    for squares in range(NUM_SQUARES):
        if board[squares] == EMPTY:
            moves.append(squares)
    return moves

def ask_number(question, low, high):
    response = None
    while response not in range (low, high):
        response = int(input(question))
    return response

def next_turn(turn):
    """Switch turns"""

    if turn == X:
        return O
    else:
        return X


def computer_move(board, computer, player):
    board = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("The computer shall be taking the location", end=" ")

     #if computer wins, it will take that move
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        #done checking this move, undo it
        board[move] = EMPTY

    #if humn wins, it will block the location
    for move in legal_moves(board):
        board[move] = player
        if winner(board) == player:
            print(move)
            return move
        #done checking the move, undo it
        board[move] = EMPTY

    #since no one is winning in next move, lets take best move
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move

def congrat_winner(the_winner, a, b):
    if the_winner != TIE:
        print("\t\t\t C O N G R A T U L A T I O N S ",the_winner, "won!!\n")
    else:
        print("Its a TIE !!!\n")



print("""Hi! This a model for TIC-TAC-TOE Game| Version 1.0 .
      created by SOUMYAJIT SINHA | CGEC CSE 34900118020
      """)
name = input("what is your name?\n")


#global variable
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9


makeitplay()
