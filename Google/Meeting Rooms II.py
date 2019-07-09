'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
'''

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        maxRooms = currentRooms = 0
        times = []
        
        for interval in intervals:
            times.append([1, interval[0]])
            times.append([0, interval[1]])
            
        
        times.sort(key = operator.itemgetter(1, 0))

        for time in times: 
            if time[0]==1: 
                currentRooms+=1
                maxRooms = max(currentRooms, maxRooms)
            else:
                currentRooms-=1

        
        return maxRooms
'''
Very similar to the death question example given by the lady who wrote CTCI. Created an array of times and whether they were starts or ends. 
Then I sorted them. When I hit a start time I increment my result. When I hit an end time I decrement.'''
