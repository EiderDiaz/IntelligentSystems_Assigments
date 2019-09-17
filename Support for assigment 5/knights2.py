# Knights Move game
# Author: Dr. Santiago Enrique Conant Pablos
# Last modification: September 2019

import random
from games import (Game, infinity)
from collections import namedtuple
GameState = namedtuple('GameState', 'to_move, knights, moves')

# ______________________________________________________________________________
# Alpha-Beta Minimax Search

def alphabeta_search(state, game, d=4, cutoff_test=None, eval_fn=None):
    """Search game to determine best action; use alpha-beta pruning.
    This version cuts off search and uses an evaluation function."""

    player = game.to_move(state)

    # Functions used by alphabeta
    def max_value(state, alpha, beta, depth):
        #print('max_value')
        #game.display(state)
        if cutoff_test(state, depth):
            v = eval_fn(state, player)
            #print('max:',v)
            return v
        v = -infinity
        for a in game.actions(state):
            v = max(v, min_value(game.result(state, a),
                                 alpha, beta, depth + 1))
            if v >= beta:
                #print('max:',v)
                return v
            alpha = max(alpha, v)
        #print('max:',v)
        return v

    def min_value(state, alpha, beta, depth):
        #print('min_value')
        #game.display(state)
        if cutoff_test(state, depth):
            v = eval_fn(state, player)
            #print('min:',v)
            return v
        v = infinity
        for a in game.actions(state):
            v = min(v, max_value(game.result(state, a),
                                 alpha, beta, depth + 1))
            #print("v=",v)
            if v <= alpha:
                #print('min:',v)
                return v
            beta = min(beta, v)
        #print('min:',v)
        return v

    # Body of alphabeta_search starts here:
    # The default test cuts off at depth d or at a terminal state
    cutoff_test = (cutoff_test or
                   (lambda state, depth: depth == d or game.terminal_test(state)))
    eval_fn = eval_fn or (lambda state: game.utility(state, player))
    best_score = -infinity
    beta = infinity
    best_action = None
    for a in game.actions(state):
        v = min_value(game.result(state, a), best_score, beta, 1)
        if v > best_score:
            best_score = v
            best_action = a
    return best_action

#_______________________________________________________________________________
# Auxiliary functions

class Knights_Move(Game):
    """Plays Knights on an N x N . A state contains information about the
       next player to play (to_move), the knight location (knight_loc), and a list
       of possible movements in the form of a list of (row, col) locations."""

    def __init__(self, N=8):
        self.N = N
        moves = [(x, y) for x in range(1, N+1) for y in range(1, N+1)]
        knight1 = random.choice(moves)
        moves.remove(knight1)
        knight2 = random.choice(moves)
        moves.remove(knight2)
        # Always starts the player 1 followed by player 2
        self.initial = GameState(to_move=1, knights={1:knight1, 2:knight2},
                                 moves=set(moves))

    def actions(self, state):
        """The legal movements are the locations generated with chess knight
        movements that are in the possible moves list."""
        return self.__legal_moves(state.moves, state.knights[state.to_move])

    def __legal_moves(self, smoves, kloc):
        """Determines the legal movements of a player on a board."""
        moves = []
        nloc = (kloc[0] + 2, kloc[1] - 1)
        if nloc in smoves: moves.append(nloc)
        nloc = (kloc[0] + 2, kloc[1] + 1)
        if nloc in smoves: moves.append(nloc)
        nloc = (kloc[0] + 1, kloc[1] + 2)
        if nloc in smoves: moves.append(nloc)
        nloc = (kloc[0] - 1, kloc[1] + 2)
        if nloc in smoves: moves.append(nloc)
        nloc = (kloc[0] - 2, kloc[1] + 1)
        if nloc in smoves: moves.append(nloc)
        nloc = (kloc[0] - 2, kloc[1] - 1)
        if nloc in smoves: moves.append(nloc)
        nloc = (kloc[0] - 1, kloc[1] - 2)
        if nloc in smoves: moves.append(nloc)
        nloc = (kloc[0] + 1, kloc[1] - 2)
        if nloc in smoves: moves.append(nloc)
        return moves

    def result(self, state, move):
        """Modifies the current state by changing the knight location"""
        moves = state.moves.copy()
        moves.remove(move)
        player = state.to_move
        knights = state.knights.copy()
        knights[player]=move
        return GameState(to_move=(2 if player == 1 else 1),
                         knights=knights, moves=moves)
                    
    def utility(self, state, player):
        "Return the value to player; 1 for win, -1 for loss, 0 otherwise."
        return 1 if player != state.to_move else -1

    def display(self, state):
        """Displays the state of the game board"""
        print('\\', end=' ')
        for y in range(1, self.N+1): print(y, end=' ')
        print('/')
        for r in range(1, self.N+1):
            print(r, end=' ')
            for c in range(1, self.N+1):
                if state.knights[1]  == (r, c):
                    print(1, end=' ')
                elif state.knights[2]  == (r, c):
                    print(2, end=' ')
                elif (r, c) in state.moves:
                    print('.', end=' ')
                else:
                    print('_', end=' ')
            print(r)
        print('/', end=' ')
        for y in range(1, self.N+1): print(y, end=' ')
        print('\\')


# ______________________________________________________________________________
# evaluation function

def eval_fn(state, player):
    """A very simple evaluation function"""
    evaluation = 1
    #print(state.to_move, player)
    if player == 1:
        return evaluation
    else:
        return -evaluation

# ______________________________________________________________________________
# Player for Games

def query_player(game, state):
    "Make a move by querying standard input."
    actions = game.actions(state)
    to_move = "Player 1" if game.to_move(state) == 1 else "Player 2"
    if not actions: return None
    while True:
        print(to_move, end=' ')
        move_string = input('move? ')
        try:
            move = eval(move_string)
        except:
            move = move_string
        if move in actions:
            return move

def random_player(game, state):
    "A player that chooses a legal move at random."
    actions = game.actions(state)
    return random.choice(actions) if actions else None

def alphabeta_player(depth=2, eval_fn=eval_fn):
    """A team player that decides after depth plies and evaluates
    the states using the eval_fn function of the team"""
    return (lambda game, state:
            alphabeta_search(state, game, d=depth, eval_fn=eval_fn))

def display_move(player, move):
    "Display a player's move"
    if player == 1:
        print('Player 1', end=' ')
    else:
        print('Player 2', end=' ')
    print("selects", move)

def play_game(game, *players, show=True):
    """Play an n-person, move-alternating game."""
    state = game.initial
    print('INITIAL BOARD')
    game.display(state)
    plays = 0
    while True:  
        plays += 1
        if show: print('PLAY #', plays)
        for player in players:
            if show: print("legal moves=", game.actions(state))
            move = player(game, state)
            if show: display_move(state.to_move, move)
            state = game.result(state, move)
            if game.terminal_test(state):
                print('END BOARD')
                game.display(state)
                utility = game.utility(state, game.to_move(game.initial))
                if utility > 0:
                    print('Player 1 wins!!')
                elif utility < 0:
                    print('Player 2 wins!!')
                else:
                    print('Tie: Nobody wins!!')
                return utility
            if show: game.display(state)

# Examples of calls for playing some games between agents that decide
# using the MINIMAX with alpha-beta pruning, between players that decide
# randomly, and between human players.
# Additionally, in the call you can combine the types of players, change the
# size of the board, and change the depth of the look ahead and the
# evaluation function for the alphabeta_players.
#
#play_game(Knights_Move(), alphabeta_player(1), alphabeta_player(1))
#play_game(Knights_Move(), random_player, random_player, show=False)
#play_game(Knights_Move(), query_player, query_player)
  
