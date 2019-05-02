from connectfour.agents.computer_player import RandomAgent
import random
import math

class StudentAgent(RandomAgent):
    def __init__(self, name):
        super().__init__(name)
        self.MaxDepth = 4

    def boardSim(self, board):
        for row in range(0 , board.height):
            for col in range(0 , board.width):
                print(row , col , " the piece in this cell is a " , board.get_cell_value(row , col))
                return 0



    def get_move(self, board):
        """
        Args:
            board: An instance of `Board` that is the current state of the board.

        Returns:
            A tuple of two integers, (row, col)
        """

        valid_moves = board.valid_moves()
        vals = []
        moves = []

        for move in valid_moves:
            next_state = board.next_state(self.id, move[1])
            moves.append( move )
            vals.append( self.dfMiniMax(next_state, 1) )

        bestMove = moves[vals.index( max(vals) )]
        return bestMove

    def dfMiniMax(self, board, depth):
        # Goal return column with maximized scores of all possible next states

        #check if student wins in 2 moves, return large priority
        if depth == 2 and board.winner() == self.id:
            return 1000000

        #check if opponent wins in 2 moves, return large negative to block
        if depth == 2 and board.winner() == self.id%2+1:
            return -100000

        #check if opponent wins in 3 moves, return large negative to block
        if depth == 3 and board.winner() == self.id%2+1:
            return -10000

        #check if opponent wins in 4 moves, return large negative to block
        if depth == 4 and board.winner() == self.id%2+1:
            return -1000

        if depth == self.MaxDepth:
            return self.evaluateBoardState(board)

        valid_moves = board.valid_moves()
        vals = []
        moves = []

        for move in valid_moves:
            if depth % 2 == 1:
                next_state = board.next_state(self.id % 2 + 1, move[1])
            else:
                next_state = board.next_state(self.id, move[1])

            moves.append( move )
            vals.append( self.dfMiniMax(next_state, depth + 1) )

        if depth % 2 == 1:
            bestVal = min(vals)
        else:
            bestVal = max(vals)


        return bestVal


    def boardSim1():
        return print("boardSim")

    def evaluateBoardState(self, board):

        #student board state score, init to 0
        playerOne = 0
        #2d array init to the current board state
        boardSim = board.board

        """search through the 2d array for 1 - 3 tokens in a row, giving higher priority depending
        on if there is just one friendly token in a row or 3, or enemy token's 1 or 3 in a row
        """

        if board.next_state and board.winner() == self.id:
            print("win")
            return 10000000

        for i in range(0, board.height):
            for j in range(0, board.width):
                try:
                    #searching for friendly tokens in a vertical line
                    if boardSim[i][j] == boardSim[i + 1][j] == 1:
                        playerOne += 10
                    if boardSim[i][j] == boardSim[i + 1][j] == boardSim[i + 2][j] == 1:
                        playerOne += 100
                    if boardSim[i][j] == boardSim[i + 1][j] == boardSim[i + 2][j] == boardSim[i + 3][j] == 1:
                        playerOne += 1000

                    #searching for vertical enemy tokens in a vertical line
                    if boardSim[i][j] == boardSim[i + 1][j] == 2:
                        playerOne -= 10
                    if boardSim[i][j] == boardSim[i + 1][j] == boardSim[i + 2][j] == 2:
                        playerOne -= 100
                    if boardSim[i][j] == boardSim[i + 1][j] == boardSim[i + 2][j] == boardSim[i + 3][j] == 2:
                        playerOne -= 10000
                except IndexError:
                    pass



                try:
                    #searching for friendly tokens in a horizontal line
                    if boardSim[i][j] == boardSim[i][j + 1] == 1:
                        playerOne += 10
                    if boardSim[i][j] == boardSim[i][j + 1] == boardSim[i][j + 2] == 1:
                        playerOne += 100
                    if boardSim[i][j] == boardSim[i][j + 1] == boardSim[i + 2][j] == boardSim[i][j + 3] == 1:
                        playerOne += 1000

                    #searching for enemy tokens in a horizontal line
                    if boardSim[i][j] == boardSim[i][j + 1] == 2:
                        playerOne -= 10
                    if boardSim[i][j] == boardSim[i][j + 1] == boardSim[i][j + 2] == 2:
                        playerOne -= 100
                    if boardSim[i][j] == boardSim[i][j + 1] == boardSim[i][j + 2] == boardSim[i][j + 3] == 2:
                        playerOne -= 10000
                except IndexError:
                    pass



                try:
                    #searching for friendly tokens in a diagonal in the left to right direction, in a row
                    if 0 < j + 3 < board.height and boardSim[i][j] == boardSim[i + 1][j + 1] == 1:
                        playerOne += 10
                    if 0 < j + 3 < board.height and boardSim[i][j] == boardSim[i + 1][j + 1] == boardSim[i + 2][j + 2] == 1:
                        playerOne += 100
                    if 0 < j + 3 < board.height and boardSim[i][j] == boardSim[i + 1][j + 1] == boardSim[i + 2][j + 2] == boardSim[i + 3][j + 3] == 1:
                        playerOne += 1000

                    #searching for enemy tokens in a diagonal in the left to right direction, in a row
                    if 0 < j + 3 < board.height and boardSim[i][j] == boardSim[i + 1][j + 1] == 2:
                        playerOne -= 10
                    if 0 < j + 3 < board.height and boardSim[i][j] == boardSim[i + 1][j + 1] == boardSim[i + 2][j + 2] == 2:
                        playerOne -= 100
                    if 0 < j + 3 < board.height and boardSim[i][j] == boardSim[i + 1][j + 1] == boardSim[i + 2][j + 2] == boardSim[i + 3][j + 3] == 2:
                        playerOne -= 10000
                except IndexError:
                    pass


                try:
                    #searching for friendly tokens in a diagonal in the right to left direction, in a row
                    if board.height > j - 3 > 0 and boardSim[i][j] == boardSim[i - 1][j + 1] == 1:
                        playerOne += 10
                    if board.height > j - 3 > 0 and boardSim[i][j] == boardSim[i - 1][j + 1] == boardSim[i - 2][j + 2] == 1:
                        playerOne += 100
                    if board.height > j - 3 > 0 and boardSim[i][j] == boardSim[i - 1][j + 1] == boardSim[i - 2][j + 2] == boardSim[i - 3][j + 3] == 1:
                        playerOne += 10000

                    #searching for enemy tokens in a diagonal in the right to left direction, in a row
                    if board.height > j - 3 > 0 and boardSim[i][j] == boardSim[i - 1][j + 1] == 2:
                        playerOne -= 10
                    if board.height > j - 3 > 0 and boardSim[i][j] == boardSim[i - 1][j + 1] == boardSim[i - 2][j + 2] == 2:
                        playerOne -= 100
                    if board.height > j - 3 > 0 and boardSim[i][j] == boardSim[i - 1][j + 1] == boardSim[i - 2][j + 2] == boardSim[i - 3][j + 3] == 2:
                        playerOne -= 10000
                except IndexError:
                    pass

        print(playerOne)
        return playerOne
        """Your evaluation function should look at the current state and return a score for it.
        As an example, the random agent provided works as follows:
            If the opponent has won this game, return -1.
            If we have won the game, return 1.
            If neither of the players has won, return a random number.


        These are the variables and functions for board objects which may be helpful when creating your Agent.
        Look into board.py for more information/descriptions of each, or to look for any other definitions which may help you.

        Board Variables:
            board.width
            board.height
            board.last_move
            board.num_to_connect
            board.winning_zones
            board.score_array
            board.current_player_score

        Board Functions:
            get_cell_value(row, col)
            try_move(col)
            valid_move(row, col)
            valid_moves()
            terminal(self)
            legal_moves()
            next_state(turn)
            winner()
    """
