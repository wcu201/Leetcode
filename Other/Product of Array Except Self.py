'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]
        n = len(nums)
        
        leftProduct = 1
        for index in range(n):
            if index!=0:
                leftProduct *= nums[index-1]
                result.append(leftProduct)
        
        
        rightProduct = 1
        for index in reversed(range(n)):
            if index!=len(nums)-1:
                rightProduct *= nums[index+1]
                result[index]*=rightProduct
    
        return(result)

'''
Understand that you can find that you can find the product of all things to the left of every value and all things right of every value in linear time. 
This is done by simply keeping track of the cumulative product from left to right then right ot left. 
The product of obth these products at a given index will be the total product without the value at that index.  
'''
#ProTip: Don't forget len(), [::-1], and reversed() are O(n) functions so call them as few times as you can or store their results to a variable and just reuse that variable.