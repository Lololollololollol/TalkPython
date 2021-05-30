import numpy

board = [
    [0.1, 1, 2, 3, 4, 5, 6],
    [10, 11, 12, 13, 14, 15, 16],
    [20, 21, 22, 23, 24, 25, 26],
    [30, 31, 32, 33, 34, 35, 36],
    [40, 41, 42, 43, 44, 45, 46],
    [50, 51, 52, 53, 54, 55, 56],
]
#

print("dia1")
sequences = []

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

for y in range(0,4):
    for i in range(0,3):
        dia2_seq= [board[i][j], board[i+1][j+1], board[i+2][j+2], board[i+3][j+3]]
        if all(dia2_seq):
            # sequences_dia.append(dia2_seq)
            sequences_dia.append(dia2_seq)
print(sequences_dia)

