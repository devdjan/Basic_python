# Игра крестики нолики
# Stage 1
# Draw board, make main loop.

# Stage 2
# How to win - Write combinations

# Stage 3
# Make another player
# Write combinations for player O. The same as player X

import time

board = ['_'] * 9 # we have created a list containing _ 9 characters
# ['_', '_' ...]
def print_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])


while True:
    # Printing board of the game
    print_board()

    # Player X input
    choice = int(input('Write a number form 0 to 8 for X: '))
    # Checking if the space is empty or not
    if board[choice] == '_':
        board[choice] = 'X'
    else:
        print('Sorry, that space is not empty')
        time.sleep(1)

    # Check for win combinations
    if (board[0] == 'X' and board[1] == 'X' and board[2] == 'X') or \
        (board[3] == 'X' and board[4] == 'X' and board[5] == 'X') or \
        (board[6] == 'X' and board[7] == 'X' and board[8] == 'X') or \
        (board[0] == 'X' and board[3] == 'X' and board[6] == 'X') or \
        (board[1] == 'X' and board[4] == 'X' and board[7] == 'X') or \
        (board[2] == 'X' and board[5] == 'X' and board[8] == 'X') or \
        (board[0] == 'X' and board[4] == 'X' and board[8] == 'X') or \
        (board[2] == 'X' and board[4] == 'X' and board[6] == 'X'):
        print_board()
        print('X player wins the game. Congratulations!')
        break

    # Print board. To see the moves of X / O players
    print_board()

    # Player O input
    choice = int(input('Write a number form 0 to 8 for O: '))
    # Checking if the space is empty or not
    if board[choice] == '_':
        board[choice] = 'O'
    else:
        print('Sorry, that space is not empty')
        time.sleep(1)

    # Check for win combinations
    if (board[0] == 'O' and board[1] == 'O' and board[2] == 'O') or \
        (board[3] == 'O' and board[4] == 'O' and board[5] == 'O') or \
        (board[6] == 'O' and board[7] == 'O' and board[8] == 'O') or \
        (board[0] == 'O' and board[3] == 'O' and board[6] == 'O') or \
        (board[1] == 'O' and board[4] == 'O' and board[7] == 'O') or \
        (board[2] == 'O' and board[5] == 'O' and board[8] == 'O') or \
        (board[0] == 'O' and board[4] == 'O' and board[8] == 'O') or \
        (board[2] == 'O' and board[4] == 'O' and board[6] == 'O'):
        print_board()
        print('O player wins the game. Congratulations!')
        break
#
#