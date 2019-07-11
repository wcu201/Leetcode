'''
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

'''

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:

        for rowIndex, row in enumerate(board):
            for columnIndex, column in enumerate(row):
                count = 0
                
                try: 
                    if (board[rowIndex-1][columnIndex]==1 or board[rowIndex-1][columnIndex]==-1)  and rowIndex!=0: count+=1
                except IndexError: pass
                try: 
                    if (board[rowIndex-1][columnIndex+1]==1 or board[rowIndex-1][columnIndex+1]==-1) and rowIndex!=0: count+=1
                except IndexError: pass
                try: 
                    if board[rowIndex][columnIndex+1]==1 or board[rowIndex][columnIndex+1]==-1: count+=1
                except IndexError: pass
                try: 
                    if board[rowIndex+1][columnIndex+1]==1 or board[rowIndex+1][columnIndex+1]==-1: count+=1
                except IndexError: pass
                try: 
                    if board[rowIndex+1][columnIndex]==1 or board[rowIndex+1][columnIndex]==-1: count+=1
                except IndexError: pass
                try: 
                    if (board[rowIndex+1][columnIndex-1]==1 or board[rowIndex+1][columnIndex-1]==-1) and columnIndex!=0: count+=1
                except IndexError: pass
                try: 
                    if (board[rowIndex][columnIndex-1]==1 or board[rowIndex][columnIndex-1]==-1) and columnIndex!=0: count+=1
                except IndexError: pass
                try: 
                    if (board[rowIndex-1][columnIndex-1]==1 or board[rowIndex-1][columnIndex-1]==-1) and columnIndex!=0  and rowIndex!=0:                             count+=1
                except IndexError: pass
                
                if board[rowIndex][columnIndex] == 1:
                    if count < 2 or count > 3: board[rowIndex][columnIndex] = -1
                else:
                    if count==3: board[rowIndex][columnIndex] = -2

        
        for rowIndex, row in enumerate(board):
            for columnIndex, column in enumerate(row):
                if board[rowIndex][columnIndex] == -1: board[rowIndex][columnIndex] = 0
                if board[rowIndex][columnIndex] == -2: board[rowIndex][columnIndex] = 1
        
        """
        Do not return anything, modify board in-place instead.
        """
'''
Fast standard solution. Go through all the indecies and count neighbors, then follow the rules.
Error catching is good if you go out of the indecies, and it's also good to be aware that in python, the index -1 returns the end of the list,
so that could cause an error if you don't check for it. Doing this in place just requires placeholder variables (In this case -1 and -2).
'''



