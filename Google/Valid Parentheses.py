'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for ch in s:
            if ch=='(' or ch=='{' or ch=='[':stack.append(ch)
            
            if ch==')' or ch=='}' or ch==']':
                if ch==')':
                    if len(stack)!=0 and stack[len(stack)-1]=='(': del stack[-1]
                    else: return False
                if ch=='}':
                    if len(stack)!=0 and stack[len(stack)-1]=='{': del stack[-1]
                    else: return False
                if ch==']':
                    if len(stack)!=0 and stack[len(stack)-1]=='[': del stack[-1]
                    else: return False
        
        return (len(stack)==0)

'''
Make a stack using a list(vector). All open characters go into the stack by order you read them. 
If you reach a closing character and the top of your stack(end of the list) is empty or do not have the corresponding character, 
the string is incorrect.  
'''                    
                    