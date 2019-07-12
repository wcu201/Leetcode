'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
'''

class Solution:
    memo = {}
    
    def __init__(self):
        self.memo = {}
    
    def other(self, s: str, wordDict: set()) -> bool:
        if not s: return True
        
        result = False
        currentWord = ""
        for ch in s:
            currentWord+=ch
            if currentWord in wordDict:
                if s[len(currentWord):] in self.memo: 
                    if self.memo[s[len(currentWord):]]==True: return True
                
                elif self.other(s[len(currentWord):], wordDict)==True:
                    self.memo[s[len(currentWord):]]=True
                    return True
                else:self.memo[s[len(currentWord):]]=False
            
        
        return result
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic = set()
        for word in wordDict: dic.add(word)
        
        return(self.other(s, dic))

'''
Several ways to handle this, but if you want to do this without exceeding the time limit, 
you should memoize or do some type of dynamic programming. I used recursion to check if the word's prefix was in the dictionary. 
If found call the same recursive method with that prefix remoived until you get an empty string then return true. 
You want to memoize all substring results you find in a dictionary so you don't have to repeat work. 
Kind of confusing to explain but once you understand, it feels naive. 
'''
