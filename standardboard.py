from board import Board

class StandardBoard(Board):
    """
    A class used to represent a the standard sudoku board, 9 by 9 size and standard rules
    ...

    Attributes
    ----------
    board: 2 dim list (9x9)
        the board used for storing the individual cells


    Methods
    -------
    

    """

    def __init__(self, boardsize=None, board=None):
        """
        Parameters
        ----------
        board: 2 dim list (9x9)
            the board used for storing the individual cells
        """

        Board.__init__(self, boardsize)

        testvar = "This works"
        print(testvar)