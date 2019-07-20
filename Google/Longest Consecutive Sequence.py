'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = set(nums)
        maxCount = 0
        while dic:
            key = dic.pop()
            count = 1
            left, right = key-1, key+1
            
            while left in dic:
                count+=1
                dic.remove(left)
                left-=1
            while right in dic:
                count+=1
                dic.remove(right)
                right+=1
            maxCount = max(maxCount, count)
            
        return(maxCount)
