'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from operator import itemgetter

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dic = {}
        head = ListNode(-1)
        current = head
        
        for l in lists:
            obj = l
            while obj!=None:
                if obj.val in dic: dic[obj.val]+=1
                else: dic[obj.val] = 1
                obj = obj.next
        
        dic = sorted(dic.items(), key=itemgetter(0))
        for key, val in dic:
            for x in range(val):
                node = ListNode(key)
                current.next = node
                current = current.next
            
        return head.next

'''
Feel ike there are a lot of ways to do this, and probably a way that is just as fast as mine but takes less space. 
Went through all lists and record the frequency of every value in a dictionary then sorted the dictionary. 
After I recreated the list by going through the sorted dictionary recreating the list making x amount of nodes for every key value 
where x=value stored at the key. Lazy solution but fast and easy to write with minimal logic
'''
