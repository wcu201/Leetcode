'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
'''

from operator import itemgetter
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return intervals
        i = sorted(intervals, key=itemgetter(0))
        result = []
        
        it, start, currentMax = 0, 0, i[0][1]
        
        while it < len(i):
            if(it != len(i)-1 and currentMax>=i[it+1][0]): currentMax = max(currentMax, i[it+1][1])
            else:
                result.append([i[start][0], currentMax])
                start = it + 1
                if it != len(i)-1: currentMax = i[it + 1][1]
            it = it + 1
            
        
        return (result)

'''
O(nlogn) algorithm. Go through a sorted version of the intervals list keeping track of a currentMax value if it is overlapping with the current 
interval at iteration. When currentMax doesn't overlap append the beginning of your starting interval and the currentMax to the result. 
Your new start will be the iterval at the next index and the new currentMax will be the end of that interval
'''
