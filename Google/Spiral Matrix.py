'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''

class Solution:
    def __init__(self):
        self.result = []
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if len(matrix)>1:
            
            self.result+=(matrix[0])
            
            if len(matrix)>2:
                for index, row in enumerate(matrix):
                    if index!=0 and index!=len(matrix)-1: self.result.append(row[len(row)-1])
                self.result+=(matrix[len(matrix)-1][::-1]) 
                if len(matrix[0])>1:
                    for index, row in enumerate(matrix[::-1]):
                        if index!=0 and index!=len(matrix)-1: self.result.append(row[0])
                
            else: self.result+=(matrix[len(matrix)-1][::-1])
            nextMatrix = matrix[1:len(matrix)-1]
            for index, row in enumerate(nextMatrix):
                if row[1:len(row)-1]: nextMatrix[index] = row[1:len(row)-1]
                else: 
                    nextMatrix[:] = []
                    break
            return self.spiralOrder(nextMatrix)
        
        else: 
            if len(matrix)!=0:self.result+=(matrix[0])
            return self.result
'''
O(nm) solution. I append the perimeter of the matrix to the result in spiral 
then I call a the same funciton recursively on a new matrix without the perimeter. 
Logic is kind of messy, and this can definitley be done without recursion, but it's decently fast so whatevs.
''' 
    
