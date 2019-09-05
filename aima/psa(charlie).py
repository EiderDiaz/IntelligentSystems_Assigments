"""Search (Chapters 3-4)

The way to use this code is to subclass Problem to create a class of problems,
then create problem instances and solve them with calls to the various search
functions."""

from utils import (
    is_in, argmin, argmax, argmax_random_tie, probability,
    weighted_sample_with_replacement, memoize, print_table, DataFile, Stack,
    FIFOQueue, PriorityQueue, name
)
#from grid import distance
def distance(a, b):
    """The distance between two (x, y) points."""
    return math.hypot((a[0] - b[0]), (a[1] - b[1]))

from collections import defaultdict
import math
import random
import sys
import bisect

infinity = float('inf')

from search import *
# ______________________________________________________________________________

class MovableWall(object):
    pass

class NotMovableWall(object):
    pass

class TargetPiece(object):
    pass

class TargetPosition(object):
    pass

class PushPullPuzzle(Problem):
    def __init__(self, initial, goal=None):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal.  Your subclass's constructor can add
        other arguments."""
        self.initial = initial
        self.goal = goal
        self.width = 6
        self.height = 6

def printMatrix():
    pass
initial = 1
board1 = PushPullPuzzle(initial)
targetPiece = TargetPiece()
print(board1)