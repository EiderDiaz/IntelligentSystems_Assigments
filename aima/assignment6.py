from csp import *

class SkyscraperPuzzle(CSP):
    """Make a CSP for the Skyscraper puzzle for search with min_conflicts.
       Suitable for large n, it uses only data structures of size O(n).
       Think of placing queens one per column, from left to right.
       That means position (x, y) represents (var, val) in the CSP.
       The main structures are three arrays to count queens that could conflict:
           rows[i]      Number of queens in the ith row (i.e val == i)
           downs[i]     Number of queens in the \ diagonal
                        such that their (x, y) coordinates sum to i
           ups[i]       Number of queens in the / diagonal
                        such that their (x, y) coordinates have x-y+n-1 = i
       We increment/decrement these counts each time a queen is placed/moved from
       a row/diagonal. So moving is O(1), as is nconflicts.  But choosing
       a variable, and a best value for the variable, are each O(n).
       If you want, you can keep track of conflicted variables, then variable
       selection will also be O(1).
       >>> len(backtracking_search(NQueensCSP(8)))
       8
       """

    def __init__(self, n):
        """Initialize data structures for n Queens."""
        CSP.__init__(self, list(range(n)), UniversalDict(list(range(n))),
                     UniversalDict(list(range(n))), queen_constraint)

        self.rows = [0] * n

