'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''

class Solution:
    def __init__(self):
        self.permutations = []
        
    def createPerms(self, current: [], nums: List[int]):
        if not nums: self.permutations.append(current)
        else:
            memo = set()
            for index, num in enumerate(nums): 
                if num not in memo:
                    self.createPerms(current+[num], nums[:index]+nums[index+1:])
                    memo.add(num)
    
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.createPerms([], nums)
        return(self.permutations)
        
'''
This takes understanding something simple. In permutations 1 I used a recursive function to give all possible permutations. 
To stop duplicates in permutations the trick is to never call the recursive function on the same interger more than once. 
This would effectively redo the same work since you're calling a recursive function with the same parameters as before 
(number, all the other numbers). I used a set to stop duplicate work (see the else statment of the recursive function, createPerms). 
Space usage could possibly be improved. 
'''
   