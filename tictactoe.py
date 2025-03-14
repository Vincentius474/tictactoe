"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    if x_count > o_count:
        return O
    
    return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions_set = set()
    
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                possible_actions_set.add((i,j))
            
    return possible_actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise ValueError("Invalid action : Cell is alreay occupied")
    
    board_copy = copy.deepcopy(board)
    current_player = player(board_copy)
    board_copy[action[0]][action[1]] = current_player

    return board_copy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
        
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or all(board[i][j] != EMPTY for i in range(3) for j in range(3))


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    player_won = winner(board)
    
    if player_won == X:
        return 1
    if player_won == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    current_player = player(board)
    
    if current_player == X:
        best_value = -float('inf')
        best_move = None
        for action in actions(board):
            new_board = result(board, action)
            value = min_value(new_board)
            if value > best_value:
                best_value = value
                best_move = action
        return best_move
    else:
        best_value = float('inf')
        best_move = None
        for action in actions(board):
            new_board = result(board, action)
            value = max_value(new_board)
            if value < best_value:
                best_value = value
                best_move = action
        return best_move
    

def max_value(board):
    """
    Returns the max for the given board state
    """
    if terminal(board):
        return utility(board)
    
    value = -float('inf')
    for action in actions(board):
        new_board = result(board, action)
        value = max(value, min_value(new_board))
    return value

def min_value(board):
    """
    Returns the min value for the given board state
    """
    if terminal(board):
        return utility(board)
    
    value = float('inf')
    for action in actions(board):
        new_board = result(board, action)
        value = min(value, max_value(new_board))
    return value
