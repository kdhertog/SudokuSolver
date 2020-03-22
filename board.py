class Board:
    """
    A class used to represent a generic sudoku board, irrespective of size or special rules

    ...

    Attributes
    ----------
    


    Methods
    -------
    

    """

    def __init__(self, boardsize=(9,9), board=None):
        """
        Parameters
        ----------
        board: 2 dim list (9x9)
            the board used for storing the individual cells
        """

        if board is None:
            self.board = [[None for i in range(boardsize[0])] for j in range(boardsize[1])] # Create empty board that can be filled later
        else:
            self.board = board