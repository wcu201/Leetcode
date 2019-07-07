'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        carryover = 0
        l1It, l2It = l1, l2
        result = ListNode(None)
        head = result
        
        while(l1It != None or l2It != None):
            result.next = ListNode(None)
            result = result.next
            summation = 0
            if (l1It != None and l2It != None): 
                summation = l1It.val + l2It.val + carryover
                l1It = l1It.next
                l2It = l2It.next    
            elif (l1It != None and l2It == None):
                summation = l1It.val + carryover
                l1It = l1It.next
            elif (l1It == None and l2It != None):
                summation = l2It.val + carryover
                l2It = l2It.next
                
            result.val = int(summation%10)
            carryover = int(summation/10)
        
        if carryover!=0: result.next = ListNode(carryover)
        return (head.next)


#Alternative

        '''
        it1 = it2 = 1 
        l1It, l2It = l1, l2
        num1 = num2 = 0 
        
        while(l1It != None):
            num1 = num1+it1*l1It.val
            l1It = l1It.next
            it1 = it1*10
            
        while(l2It != None):
            num2 = num2+it2*l2It.val
            l2It = l2It.next
            it2 = it2*10 
            
        
        result = ListNode(None)
        head = result
        sumStr = str(num1+num2)
        tail = None
        
        for x in sumStr[::-1]:
            result.val = int(x)
            result.next = ListNode(None)
            tail = result
            result = result.next
        
        if(tail!=None):
            tail.next = None
            
        return head
    '''