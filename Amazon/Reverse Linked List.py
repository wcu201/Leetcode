'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:    
    def reverseList(self, head: ListNode) -> ListNode:
        current, prev = head, None
        
        while current:
            swap = current.next
            current.next = prev
            prev = current
            current = swap   
        return prev
        
