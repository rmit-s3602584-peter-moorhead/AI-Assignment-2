from connectfour.agents.computer_player import RandomAgent
import random

class StudentAgent(RandomAgent):
    def __init__(self, name):
        super().__init__(name)
        self.MaxDepth = 1

    def test(self, board):
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


    def test1():
        return print("test")

    def evaluateBoardState(self, board):

        studentCount = 42
        opponentCount = 42
        rowCount = 0

        for row in range(0, board.height):
            for col in range(0, board.width):
                if board.get_cell_value(row, board.height) == 2:
                    studentCount = studentCount - 1
                    print(studentCount)

                #if board.get_cell_value(col, board.width) == 2:
                #    studentCount = studentCount - 1
                #    print(studentCount)

        if studentCount >= opponentCount:
            return 0
        else:
            return 1


        #print(row, rowCount)

        #for row in range(0 , board.height):
        #    for col in range(0 , board.width):
        #        print(board.get_cell_value(row, col))
        #print("================================")


        #print(board.width)
        #print("================================")

        #return random.uniform(0, 1)


        """
        Your evaluation function should look at the current state and return a score for it.
        As an example, the random agent provided works as follows:
            If the opponent has won this game, return -1.
            If we have won the game, return 1.
            If neither of the players has won, return a random number.
        """

        """
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

        """+1 to each available tile"""
        """if opponent has 2 in a row, block"""
        """for i in range(10):
            print (i)"""

        """board.valid_moves"""

        """for i in range(self.width):
            same_count = 1
            curr = self.board[0][i]
            for j in range(1, self.height):
                if self.board[j][i] == curr:
                    same_count += 1
                    if same_count == 2 and curr != 0:
                        return curr
                else:
                    same_count = 1
                    curr = self.board[j][i]
        return 0


        if board.get_cell_value(0, 4) == 2:
            return 0
        elif board.get_cell_value(0, 4) == 1:
            return 1
        else:
            return random.uniform(0,1)
        return 0

        return random.uniform(0, 1)"""
        """board1 = board[3][3]
        return board1"""

        """for row in range(0 , board.height):
            for col in range(0 , board.width):
                print(row , col , " the piece in this cell is a " , board.get_cell_value(row , col))
        print("========================================")"""



    """test(self, board)"""
