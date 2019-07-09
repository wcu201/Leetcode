'''
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = {}
        cumulativeSum, result = 0, 0
        
        for index, num in enumerate(nums):
            cumulativeSum += num
            if cumulativeSum in sums: sums[cumulativeSum].append(index)
            else: sums[cumulativeSum] = [index]
    
        
        for key, amount in sums.items():
            for index in sums[key]:
                if (k+key-nums[index]) in sums:
                    for ind in sums[k+key-nums[index]]:
                        if ind >= index: result+=1
            
        return result

'''
Combination of cumulative sum and 2sum. Create a cumulative sum dictionary and check to see if it has a complement who's difference k. 
That's the underlying concept but a lot of edge cases like same cumlative sum and reverse subarray get in the way. 
This solution is not perfect so should be improved. '''
