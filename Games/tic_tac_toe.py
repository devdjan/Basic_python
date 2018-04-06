# Игра крестики нолики
# Stage 1
# Draw board, make main loop.

# Stage 2
# How to win - Write combinations

# Stage 3
# Make another player
# Write combinations for player O. The same as player X

# Stage 4
# reuse code, where we check winning combinations
# Write two functions to check if o winner or X
# Function to check If the board is full - Does not work, will fix later

import time

board = ['_'] * 9 # we have created a list containing _ 9 characters
# ['_', '_' ...]
def print_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])

# Checking if X is a winner
def had_player_won(board, player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
            (board[3] == player and board[4] == player and board[5] == player) or \
            (board[6] == player and board[7] == player and board[8] == player) or \
            (board[0] == player and board[3] == player and board[6] == player) or \
            (board[1] == player and board[4] == player and board[7] == player) or \
            (board[2] == player and board[5] == player and board[8] == player) or \
            (board[0] == player and board[4] == player and board[8] == player) or \
            (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False

# Main function to chek if the board is full or not
# Небольшой костыль
def is_board_full(board):
    if '_' in board:
        return False
    else:
        return True

while True:
    print_board()

    # Player X input
    choice = int(input('Write a number form 0 to 8 for X: '))
    # Checking if the space is empty or not
    if board[choice] == '_':
        board[choice] = 'X'
    else:
        print('Sorry, that space is not empty')
        time.sleep(1)
        # Как сделать, я хожу например O и при попадании в поле, где уже стоит(крестик / нолик)
        # пишет "Это занятое место", и отдает ход игроку Х

# Т.е. в player - мы передаем нашего игрока икс, также и для О
    if had_player_won(board, "X"): # If X wins(value of func. is True, we keep doing code
        print_board()
        print('X player wins the game. Congratulations!')
        break

    # Print board. To see the moves of X / O players
    print_board()

    # Chek Is the board full
    if is_board_full(board):
        print('There are no empty space!')
        break

    # Player O input
    choice = int(input('Write a number form 0 to 8 for O: '))
    # Checking if the space is empty or not
    if board[choice] == '_':
        board[choice] = 'O'
    else:
        print('Sorry, that space is not empty')
        time.sleep(1)

    if had_player_won(board, 'O'):
        print_board()
        print('O player wins the game. Congratulations!')
        break

    # Chek Is the board full
    if is_board_full(board):
        print('There are no empty space!')
        break