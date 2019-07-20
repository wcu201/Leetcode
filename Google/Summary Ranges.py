'''
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
'''

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return([])
        result = []
        
        start = nums[0]
        for index, val in enumerate(nums):
            if index==len(nums)-1: 
                if start==val: result.append(str(start))
                else: result.append(str(start)+"->"+str(val))
                break
            if nums[index+1]!=val+1:
                if start==val: result.append(str(start))
                else: result.append(str(start)+"->"+str(val))
                start = nums[index+1]
        
        
        return(result)