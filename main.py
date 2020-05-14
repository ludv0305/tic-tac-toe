game_over = False

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

turn = "x"

def display_board():
    print("\n")
    print(board[0], "|", board[1], "|", board[2])
    print(board[3], "|", board[4], "|", board[5])
    print(board[6], "|", board[7], "|", board[8])
    print(0, "|", 1, "|", 2)
    print(3, "|", 4, "|", 5)
    print(6, "|", 7, "|", 8)

def basic_board():
    print("\n")
    print(board[0], "|", board[1], "|", board[2])
    print(board[3], "|", board[4], "|", board[5])
    print(board[6], "|", board[7], "|", board[8])

def flip_turn(turn):
    if turn == "x":
        turn = "o"
    elif turn == "o":
        turn = "x"


def move():
    global turn
    valid = False
    while not valid:

        if turn == "x":
            turn2 = int(input("choose your position: "))
            if board[turn2] == "-":
                board[turn2] = "x"
                valid = True
                turn = "o"
            else:
                print("You can't go there")
        elif turn == "o":
            turn3 = int(input("choose your position: "))
            if board[turn3] == "-":
                board[turn3] = "o"
                valid = True
                turn = "x"
            else:
                print("You can't go there")

def row_win():

    if board[0] == "x" and board[1] == "x" and board[2] == "x":
        print("x wins")
        return True
    elif board[0] == "o" and board[1] == "o" and board[2] == "o":
        print("o wins")
        return True
    if board[3] == "x" and board[4] == "x" and board[5] == "x":
        print("x wins")
        return True
    elif board[3] == "o" and board[4] == "o" and board[5] == "o":
        print("o wins")
        return True
    if board[6] == "x" and board[7] == "x" and board[8] == "x":
        print("x wins")
        return True
    elif board[6] == "o" and board[7] == "o" and board[8] == "o":
        print("o wins")
        return True


def line_win():
    if board[0] == "x" and board[3] == "x" and board[6] == "x":
        print("x wins")
        return True
    elif board[0] == "o" and board[3] == "o" and board[6] == "o":
        print("o wins")
        return True
    if board[1] == "x" and board[4] == "x" and board[7] == "x":
        print("x wins")
        return True
    elif board[1] == "o" and board[4] == "o" and board[7] == "o":
        print("o wins")
        return True
    if board[2] == "x" and board[5] == "x" and board[8] == "x":
        print("x wins")
        return True
    elif board[2] == "o" and board[5] == "o" and board[8] == "o":
        print("o wins")
        return True

def cross_win():
    if board[0] == "x" and board[4] == "x" and board[8] == "x":
        print("x wins")
        return True
    elif board[0] == "o" and board[4] == "o" and board[8] == "o":
        print("o wins")
        return True
    if board[2] == "x" and board[4] == "x" and board[6] == "x":
        print("x wins")
        return True
    elif board[2] == "o" and board[4] == "o" and board[6] == "o":
        print("o wins")
        return True

def draw():
    if board[0] != "-" and board[1] != "-" and board[2] != "-" and board[3] != "-" and board[4] != "-" and board[5] != "-" and board[6] != "-" and board[7] != "-" and board[8] != "-":
        print("draw")
        return True

while not game_over:
    display_board()
    move()
    row_win()
    if row_win() == True or line_win() == True or cross_win() == True or draw():
        game_over = True
        display_board()
    flip_turn(turn)
