'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3

'''

class Solution:
    def dfs(self, x: int, y: int, grid: List[List[str]]):
        if y < len(grid) and y >= 0 and x >= 0 and x < len(grid[y]):
            if grid[y][x] == '1':
                grid[y][x] = '2'
                self.dfs(x, y+1, grid)
                self.dfs(x+1, y, grid)
                self.dfs(x-1, y, grid)
                self.dfs(x, y-1, grid)
        
        
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        
        for rowIndex, row in enumerate(grid):
            for columnIndex, column in enumerate(row):
                if grid[rowIndex][columnIndex] == '1':
                    count = count + 1
                    self.dfs(columnIndex, rowIndex, grid)
        
        return count

'''
You want to go through every point in the 2D grid iteratively. 
At every point run a dfs where you basically perform a recursive algorithm 
that changes a '1' to a value differnt from '1' or '0' (in this case '2'). 
Then you will recurse in all 4 adjacent directions. This will make at most 1 island of 2's at every iterative step. 
'''
