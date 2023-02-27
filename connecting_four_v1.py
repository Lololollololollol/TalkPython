import datetime
import json
import os.path
import platform
import colorama
from colorama import Fore
from prompt_toolkit import prompt


def show_header():
    print("------------------------------------------------")
    print("----------Welcome to Connecting 4 V.3-----------")
    print("--------(Packages and Error Handling)-----------")
    print("------------------------------------------------")

def main():
    log("App starting up...")

    show_header()
    show_leaderboard()

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

    assign_player1 = input(Fore.BLUE + "What is the name of player1?: ")
    print()
    assign_player2 = input(Fore.YELLOW + "What is the name of player2?: " + Fore.WHITE)
    print()
    log(f"{assign_player1} and {assign_player2} have logged in.")
    active_player_index = 0
    players = [assign_player1, assign_player2]
    symbols = ['O', 'X']
    player = players[active_player_index]

    # Until Someone wins
    while not find_winner(board):

        player = players[active_player_index]
        symbol = symbols[active_player_index]

        announce_turn(player)
        show_board(board)
        if not choose_location(board, symbol):
            print(Fore.RED + "That isn't an option, try again." + Fore.WHITE)
            continue

        # TOGGLE ACTIVE PLAYER
        active_player_index = (active_player_index + 1) % len(players)

    print()
    msg = f"GAME OVER! {player} has won with the board."
    fore = Fore.BLUE if {player} == assign_player1 else Fore.GREEN
    print(fore + msg + Fore.WHITE)
    show_board(board)
    record_wins(player)
    log(msg)
    print()


def show_leaderboard():
    leaders = load_leaderboard()

    sorted_leaders = list(leaders.items())
    sorted_leaders.sort(key=lambda l: l[1], reverse=True)

    print()
    print("---------------------------")
    print("LEADERS:")
    for name, wins in sorted_leaders[0:5]:
        print(f"{wins:,}- {name}")
    print("---------------------------")
    print()


def load_leaderboard():
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, 'leaderboard.json')

    if not os.path.exists(filename):
        return {}

    with open(filename, 'r', encoding='utf-8') as fin:
        return json.load(fin)


def record_wins(player):
    leaders = load_leaderboard()

    if player in leaders:
        leaders[player] += 1

    else:
        leaders[player] = 1

    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, 'leaderboard.json')

    with open(filename, 'w', encoding='utf-8') as fout:
        json.dump(leaders, fout)


# 3. decide the location
def choose_location(board, symbol):
    try:
        # def choose_column():
        given_column = int(input("Select a column: "))
        column = given_column - 1

        for u in range(5, -1, -1):
            if board[u][column] is None:
                board[u][column] = symbol
                return True
    except ValueError as ve:
        print()
        print(f"It should be between 1 to {len(board[0])}")

    except Exception:
        print()
        print(Fore.RED + f"Exception: Unknown Error" + Fore.WHITE)


def show_board(board):
    for row in board:
        print("| ", end='')
        for cell in row:
            symbol = cell if cell is not None else "_"
            print(symbol, end=" | ")
        print()


def announce_turn(player):
    print()
    msg = f"It's {player}'s turn. Please select a column from the board."
    print(msg)
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

    # 4-1) verify_row():
    for c in range(0, 4):
        for r in range(0, 6):
            row_sequence = board[r][c:c + 4]
            sequences.append(row_sequence)

    # 4-2) verify_column():
    for c in range(0, 7):
        while c < 7:
            for i in range(0, 3):
                col_sequence = [board[i][c] for i in range(i, i + 4)]
                # if i == 2:
                #     x = +1
                sequences.append(col_sequence)
            break

    #     4-3) verify_diagonal():
    for y in range(0, 4):
        for x in range(3, 6):
            dia1_seq = [board[x][y], board[x - 1][y + 1], board[x - 2][y + 2], board[x - 3][y + 3]]
            if all(dia1_seq):
                sequences.append(dia1_seq)

    for y in range(0, 4):
        for x in range(0, 3):
            dia2_seq = [board[x][y], board[x + 1][y + 1], board[x + 2][y + 2], board[x + 3][y + 3]]
            if all(dia2_seq):
                sequences.append(dia2_seq)

    return sequences


def log(msg):
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, 'connecting_four.log')

    with open(filename, 'a', encoding='utf-8') as fout:
        fout.write(f"[{datetime.datetime.now().date().isoformat()}]")
        fout.write(msg)
        fout.write('\n')


if __name__ == '__main__':
    main()
