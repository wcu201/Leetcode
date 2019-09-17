'''
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = ""
        num2 = ""
        
        currentL1 = l1
        currentL2 = l2
        
        while currentL1 or currentL2:
            if currentL1:
                num1+=str(currentL1.val)
                currentL1=currentL1.next
            
            if currentL2:
                num2+=str(currentL2.val)
                currentL2=currentL2.next
            

        number=str(int(num1)+int(num2))
        
        head = ListNode(None)
        current = head
        
        for index in range(len(number)): 
            current.val = int(number[index])
            
            if index!=len(number)-1:
                new = ListNode(None)
                current.next = new
                current = current.next
        
        
        return(head)
        
        
        