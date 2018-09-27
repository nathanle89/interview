"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.
"""

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board is None:
            return None

        row_length = len(board)
        if row_length == 0:
            return []

        col_length = len(board[0])

        next_state = [[0] * col_length for i in range(0, row_length)]

        for i in range(0, row_length):
            for j in range(0, col_length):
                neighbors = 0
                if i + 1 < row_length:
                    neighbors += board[i + 1][j]
                if j + 1 < col_length:
                    neighbors += board[i][j+1]
                if i + 1 < row_length and j + 1 < col_length:
                    neighbors += board[i + 1][j + 1]
                if i - 1 >= 0:
                    neighbors += board[i - 1][j]
                if j -1 >= 0:
                    neighbors += board[i][j - 1]
                if i - 1 >= 0 and j -1 >= 0:
                    neighbors += board[i - 1][j - 1]
                if i - 1 >= 0 and j + 1 < col_length:
                    neighbors += board[i - 1][j + 1]
                if i + 1 < row_length and j - 1 >= 0:
                    neighbors += board[i + 1][j - 1]

                val = self.getNextStateByNeighborsValue(board[i][j], neighbors)
                next_state[i][j] = val
        for i in range(0, row_length):
            for j in range(0, col_length):
                board[i][j] = next_state[i][j]

    def getNextStateByNeighborsValue(self, current_cel, neighbor_sum):
        if current_cel == 1:
            if neighbor_sum < 2:
                return 0
            elif neighbor_sum <= 3 and neighbor_sum >= 2:
                return 1
            elif neighbor_sum > 3:
                return 0
            else:
                return 1
        else:
            if neighbor_sum == 3:
                return 1
            else:
                return 0

