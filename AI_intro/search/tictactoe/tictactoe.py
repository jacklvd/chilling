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
    player_x, player_o = 0, 0
    
    for row in board:
        player_x += row.count(X)
        player_o += row.count(O)

    return X if player_x <= player_o else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception('no actions required')
    
    action_board = copy.deepcopy(board)
    
    if action_board[action[0]][action[1]] != EMPTY:
        raise Exception('the position has been taken')
    
    action_board[action[0]][action[1]] = player(board)
    
    return action_board


# a helper function to check winning condition
def is_three(a, b, c):
    return a == b == c


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """  
    # win horizontally
    for i in range(len(board)):
        if is_three(board[i][0], board[i][1], board[i][2]):
            if board[i][0] == X:
                return X
            elif board[i][0] == O:
                return O
    # win vertically.
        if is_three(board[0][i], board[1][i], board[2][i]):
            if board[0][i] == X:
                return X
            elif board[0][i] == O:
                return O

    # win diagonally.
    if is_three(board[0][0], board[1][1], board[2][2]):
        if board[0][0] == X:
            return X
        elif board[0][0] == O:
            return O
    elif is_three(board[0][2], board[1][1], board[2][0]):
        if board[0][2] == X:
            return X
        elif board[0][2] == O:
            return O


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    else:
        counter = 0
        for row in board:
            counter += row.count(EMPTY)
        if counter == 0: 
            return True 
    return False
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    who = winner(board)
    if who == X:
        return 1
    elif who == O:
        return -1
    return 0



def max_evaluation(board):
    if terminal(board): return utility(board)
    best_score = -math.inf
    for action in actions(board):
        score = min_evaluation(result(board, action))
        if score > best_score:
            best_score = score
    return best_score


def min_evaluation(board):
    if terminal(board): return utility(board)
    best_score = math.inf
    for action in actions(board):
        score = max_evaluation(result(board, action))
        if score < best_score:
            best_score = score
    return best_score


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    optimal_move = None
    
    if terminal(board): return None
    
    if player(board) == X:
        best_score = -math.inf
        for action in actions(board):
            score = min_evaluation(result(board, action))
            if score > best_score:
                best_score = score
                optimal_move = action
    
    elif player(board) == O:
        best_score = math.inf
        for action in actions(board):
            score = max_evaluation(result(board, action))
            if score < best_score:
                best_score = score
                optimal_move = action
    
    return optimal_move