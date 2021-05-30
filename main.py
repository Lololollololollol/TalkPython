# Build Connecting 4
#
# &1. create a 6*7 board
# 2. choose a player between the computer and a person
# 3. a player chooses a column
#  verify the row using the input from #3.
# . mark the board with a symbol
#  play until someone wins
# . verify connecting 4
# . announce the game over


def human_vs_human():
    pass

def human_vs_computer():
    pass

def main():
    print("--------------------------------------------")
    print("-------Welcome to Connecting 4 V.1----------")
    print("--------------------------------------------")

    # 1. create_board:

    board = [
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None]
    ]

    # 2. choose_initial_player:

    assign_player1 = input("What is your name?: ")
    print()
    auto = input("Do you want to play with Computer?: ")
    mode = None
    print()

    if auto == "No":
        assign_player2 = input("What is the name of player2?: ")
        mode = "hVSh"
        # human_vs_human()
    else:
        mode = "hVSm"
        # human_vs_computer()

    print(f"{assign_player1} starts the first!")

    active_player_index = 0
    players = ['assign_player1', 'assign_player2']
    symbols = ['O', 'X']
    player = players[active_player_index]

# Until Someone wins


    while not find_winner(player) is True:

        player = players[active_player_index]
        symbol = symbols[active_player_index]

        announce_turn(player)
        decide_location(board, symbol)
        show_board(board)

        if not mark_symbol(board, symbol):
            print("That isn't an option, try again.")
            continue

        # TOGGLE ACTIVE PLAYER
        active_player_index = (active_player_index + 1) % len(players)

    print()
    print(f"GAME OVER! {player} has won with the board: ")
    show_board(board)
    print()


def show_board(board):
    for row in board:
        print("| ", end='')
        for cell in row:
            symbol = cell if cell is not None else "_"
            print(symbol, end=" | ")
        print()


def announce_turn(player):
    print()
    print("It's {player}'s turn. Please select a column from the board.")
    print()


def find_winner(board):
    connecting_row = get_winning_sequences(board)

    for cells in connecting_row:
        symbol1 = cells[0]
        if symbol1 and all(symbol1 == cell for cell in cells):
            return True

    return False


# 3. decide the location
def decide_location(board, symbol):
    # def choose_column():
    while True:
        given_column = int(input("Select a column: "))
        column = given_column - 1
        if given_column < 1 or given_column > 7:
            print("You entered a wrong column. The column value should be between 1 and 7")
            continue
        else:
            return given_column
    # def decide_row()
    x = 0,
    while board[x][given_column] is not None:
        x = +1
        y = given_column - 1
        symbol1 = board[x][y]

def mark_symbol(board, symbol):

    row = int(input("Choose which row: "))
    column = int(input("Choose which column: "))

    row -= 1
    column -= 1
    if row < 0 or row >= len(board):
        return False
    if column < 0 or column >= len(board[0]):
        return False

    cell = board[row][column]
    if cell is not None:
        return False

    board[row][column] = symbol
    return True


# 4. play rounds until there are consecutive 4

def get_winning_sequences(board):
    connecting_row = []

    #   verify_row():
    x = range(0, 7)
    y = range(0, 4)  # 4= len(row)-4+1

    rows = board
    row = board[x]
    cell = row[y]

    # board[x][y]

    # while y < len(row)-4+1:
    #     connecting_row.extend(board[x][y])

    for r4 in range(0, 4):
        x=0
        con_r4 = [board[x][r4]]
        for x in range(0, 7):
            row_group = [board[x][r4]]
            connecting_row.append(row_group)
            # connecting_row(con_r4)

    # board[0][0], board[0][1], board[0][2], board[0][3]
    # board[1][0], board[1][1], board[1][2], board[1][3]
    # ....

    connecting_col = []
    # board[0][0], board[1][0], board[2][0], board[3][0]
    # board[0][1], board[1][1], board[2][1], board[3][1]
    # ....

    connecting_dia1 = []
    connecting_dia1 = []

    symbol1 = rows





#import numpy as np

# def correct_boundary(num):
#     if num < 0:
#         return 0
#     elif num > 6:
#         return 6
#     else:
#         return num


#     4-2) verfy_column():
#     4-3) verify_diagonal():
#
#
#
# while verify_connecting4() is not True:
#
#


# 5. Game Over, active player won!


if __name__ == '__main__':
    main()
