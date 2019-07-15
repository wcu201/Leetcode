'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

class Solution:
    def __init__(self):
        self.permutations = []
        
    def createPerms(self, current: [], nums: List[int]):
        if not nums: self.permutations.append(current)
        else:
            for index, num in enumerate(nums): self.createPerms(current+[num], nums[:index]+nums[index+1:])
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.createPerms([], nums)
        return(self.permutations)

#Use recursion to make all possible permtations. You would think that you need to memoize but for some reason it still works without having to. 
