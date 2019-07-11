'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

class Solution:
    results = []
    def __init__(self):
        self.results = []
    
    def validCombos(self, currentString: str, currentSum: int, openPara: int, closedPara: int):
        if currentSum>0:
            return
        if(openPara==0 and closedPara==0):
            self.results.append(currentString)
            return
        if openPara>0:self.validCombos(currentString+'(', currentSum-1, openPara-1, closedPara)
        if closedPara>0:self.validCombos(currentString+')', currentSum+1, openPara, closedPara-1)
            
    def generateParenthesis(self, n: int) -> List[str]:
        self.validCombos("", 0, n, n)
        return(self.results)


'''
Create a helper recursive function the goes through all possible combinations and stores valid ones. 
Way to optpmize is to use a sum value to keep track of the difference between number of open paranthese and closed. 
There can never more open closed than open as you're reading a combo from left to right so stop the recursive function if that ever happens.
''' 
