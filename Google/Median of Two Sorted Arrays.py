'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
            choose = None
            pointer1 = pointer2 = counter = median = 0
            
            while(True):
                if counter==int((len(nums1) + len(nums2))/2):
                    current = 0
                    if pointer1<len(nums1) and pointer2<len(nums2): 
                        current = min(nums1[pointer1], nums2[pointer2])
                    if pointer1<len(nums1) and pointer2>=len(nums2): current = nums1[pointer1]
                    if pointer1>=len(nums1) and pointer2<len(nums2): current = nums2[pointer2]
       
                    if (len(nums1) + len(nums2))%2==0:median = float(choose + current)/2
                    else: median = float(current)
                    break
        
                if pointer1<len(nums1) and pointer2<len(nums2):
                    if nums1[pointer1]<=nums2[pointer2]:
                        choose = nums1[pointer1]
                        pointer1+=1
                    else: 
                        choose = nums2[pointer2]
                        pointer2+=1
                
                elif pointer1<len(nums1) and pointer2>=len(nums2):
                    choose = nums1[pointer1]
                    pointer1+=1
                    
                elif pointer1>=len(nums1) and pointer2<len(nums2): 
                    choose = nums2[pointer2]
                    pointer2+=1
                
                counter+=1
                    
            
            return median

'''
Just use the two pointer technique. Have pointers that move through both arrays. 
If the pointer pointing to one array points to the smaller value that pointer gets incremented. 
Once you reach the halfway point of theoretically merged array you just return the pointer that points to the minimum value or 
the average of two minimum values if you have an even sized merged array. 
Try to minimize logic as best you can.(I didn't do the best job of that here) (Time Complexity: O(n+m))
'''
