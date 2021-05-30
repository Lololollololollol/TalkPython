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
        [None, None, None, None, None, None, None],
    ]

    # 2. choose_initial_player:

    assign_player1 = input("What is your name?: ")
    print()
    assign_player2 = input("What is the name of player2?: ")
    print()
    # print(f"{assign_player1} starts the first!")

    active_player_index = 0
    players = ['assign_player1', 'assign_player2']
    symbols = ['O', 'X']
    player = players[active_player_index]

    # Until Someone wins

    while not find_winner(board):

        player = players[active_player_index]
        symbol = symbols[active_player_index]

        announce_turn(player)
        show_board(board)
        if not choose_location(board, symbol):
            print("That isn't an option, try again.")
            continue

        # TOGGLE ACTIVE PLAYER
        active_player_index = (active_player_index + 1) % len(players)

    print()
    print(f"GAME OVER! {player} has won with the board: ")
    show_board(board)
    print()


# 3. decide the location
def choose_location(board, symbol):
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

# 4. play rounds until there are consecutive 4

def find_winner(board):
    sequences = get_winning_sequences(board)

    for cells in sequences:
        symbol1 = cells[0]
        if symbol1 and all(symbol1 == cell for cell in cells):
            return True

    return False


def get_winning_sequences(board):
    sequences = []

    #4-1) verify_row():
    for c in range(0, 4):
        for r in range(0, 6):
            row_sequence = board[r][c:c+4]
            sequences.extend(row_sequence)

    #4-2) verify_column():
    for c in range(0, 7):
        while c < 7:
            for i in range(0, 3):
                col_sequence = [board[i][c] for i in range(i, i + 4)]
                # if i == 2:
                #     x = +1
                sequences.append(col_sequence)
            break

#     4-3) verify_diagonal():
    for y in range(0,4):
        for x in range(3,6):
            dia1_seq= [board[x][y], board[x-1][y+1], board[x-2][y+2], board[x-3][y+3]]
            if all(dia1_seq):
                sequences.append(dia1_seq)

    for y in range(0,4):
        for x in range(0,3):
            dia2_seq= [board[x][y], board[x+1][y+1], board[x+2][y+2], board[x+3][y+3]]
            if all(dia2_seq):
                sequences.append(dia2_seq)

    return sequences


if __name__ == '__main__':
    main()
