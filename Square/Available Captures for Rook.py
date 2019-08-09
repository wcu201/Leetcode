'''
On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces, and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south), then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.

 

Example 1:



Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation: 
In this example the rook is able to capture all the pawns.
Example 2:



Input: [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 0
Explanation: 
Bishops are blocking the rook to capture any pawn.
Example 3:



Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation: 
The rook can capture the pawns at positions b5, d6 and f5.

Note:

board.length == board[i].length == 8
board[i][j] is either 'R', '.', 'B', or 'p'
There is exactly one cell with board[i][j] == 'R'
'''

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rook = []
        
        for yindex, row in enumerate(board):
            for xindex, column in enumerate(row):
                if column == 'R': 
                    rook[:] = [xindex, yindex]
                    break
        
        result = 0
        left = right = rook[0]
        up = down = rook[1]

        while left>=1:
            left-=1
            if board[rook[1]][left] == '.': continue
            if board[rook[1]][left] == 'p': result+=1
            break
        
        while right<=len(board[rook[1]])-2:
            right+=1
            if board[rook[1]][right] == '.': continue
            if board[rook[1]][right] == 'p': result+=1
            break
        
        while up>=1:
            up-=1
            if board[up][rook[0]] == '.': continue
            if board[up][rook[0]] == 'p': result+=1
            break
        
        while down<=len(board)-2:
            down+=1
            if board[down][rook[0]] == '.': continue
            if board[down][rook[0]] == 'p': result+=1
            break
        
        return (result)

#Find the rook then just look for if you can go from that coordinate and hit a pond before anything else