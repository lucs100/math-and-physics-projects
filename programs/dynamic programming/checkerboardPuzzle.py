# Solution to https://en.wikipedia.org/wiki/Dynamic_programming#Checkerboard

board = [[6, 7, 4, 7, 8], [7, 6, 1, 1, 4], [3, 5, 7, 8, 2], [0, 6, 7, 0, 0], [0, 0, 5, 0, 0]]

def solveMin(board, x, y):
    if x < 0 or x > 4:  #forces algo to select on the board
        return float('inf')
    if y == 0:  #end of puzzle
        return
    return (min(solveMin(board, x-1, y-1), solveMin(board, x, y-1), solveMin(board, x+1, y-1)) + board[x][y])   #gives algo three choices - leftup, up, or rightup, adding current square to total

print(solveMin(board, 2, 4))

# board layout:
#     6  7 	4  7  8
#     7  6 	1  1  4
#     3  5 	7  8  2
#     –  6 	7  0  –
#     –  – 	5  -  –
