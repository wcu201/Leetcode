'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''

class Solution:

    def __init__(self):
        self.results = []
        self.numsToLetters = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"} 
    
    def helper(self, currentString: str, digits: str):
        if len(digits)==0:
            return
        if len(digits)==1:
            for x in range(3):
                self.results.append(currentString + self.numsToLetters[int(digits[0])][x])
            if len(self.numsToLetters[int(digits[0])])==4:
                self.results.append(currentString + self.numsToLetters[int(digits[0])][3])
        else:
            for x in range(3):
                self.helper(currentString+self.numsToLetters[int(digits[0])][x], digits[1:])
            if len(self.numsToLetters[int(digits[0])])==4:
                self.helper(currentString+self.numsToLetters[int(digits[0])][3], digits[1:])
            
        
    def letterCombinations(self, digits: str) -> List[str]:
        self.helper("", digits)
        return self.results

'''
Key is to use a helper recursive function that passes along a current string variable that keeps track of the current permutaion you're doing. 
Once it reaches the end of the word just add the possibility to an array. Your final array should have all possibilities 
'''
