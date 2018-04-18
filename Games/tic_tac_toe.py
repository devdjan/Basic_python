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

# Stage 5
# Creating game AI
# def computer moves(board, player):
# Computer will return us random number - random move
# Number should be on empty sport

# Stage 6
# Write code for computer moves
# Test code

# Stage 7
# Write some combinations for computer to win the game if computer have 1 and 7 moves on board, so put 4

import time
import random

board = ['', '_', '_', '_', '_', '_', '_', '_', '_', '_']# we have created a list containing _ 9 characters

def print_board():
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[7] + '|' + board[8] + '|' + board[9])

# Checking if X is a winner
def had_player_won(board, player):
    if (board[1] == player and board[2] == player and board[3] == player) or \
            (board[4] == player and board[5] == player and board[6] == player) or \
            (board[7] == player and board[8] == player and board[9] == player) or \
            (board[1] == player and board[4] == player and board[7] == player) or \
            (board[2] == player and board[5] == player and board[8] == player) or \
            (board[3] == player and board[6] == player and board[9] == player) or \
            (board[1] == player and board[5] == player and board[9] == player) or \
            (board[3] == player and board[5] == player and board[7] == player):
        return True
    else:
        return False

# Main function to chek if the board is full or not

def is_board_full(board):
    if '_' in board:
        return False
    else:
        return True

def computer_move(board, player):
    for i in range (1,10):
        if board[i] == '_':
            board[i] = player
            if had_player_won(board,player):
                return i
            else:
                board[i] = '_'

    if board[5] == '_':
        return 5

    while True:
        move = random.randint(1,9)
        # If computer move to blank, go ahead
        if board[move] == '_':
             return move
             break
    return 5

while True:
    print_board()

    # Player X input
    choice = i----------
    # Checking if the space is empty or not
    if board[choice] == '_':
        board[choice] = 'X'
    else:
        print('Sorry, that space is not empty')
        time.sleep(1)
        # Как сделать, я хожу например O и при попадании в поле, где уже стоит(крестик / нолик)
        # пишет "Это занятое место", и отдает ход игроку Х

    if had_player_won(board, "X"): # If X wins(value of func. is True, we keep doing code
        print_board()
        print('X player wins the game. Congratulations!')
        break

    print_board()

    # Chek Is the board full
    if is_board_full(board):
        print('There are no empty space!')
        break

    # Player O input
    choice = computer_move(board, 'O')
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