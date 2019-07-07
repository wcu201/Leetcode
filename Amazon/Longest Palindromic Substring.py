'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"

'''

#Expand around center approach I believe. 
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest, oddLongest, evenLongest = 0, 1, 0
        evenCheck, oddCheck = True, True
        longestSubStr = ""
    
        evenIndex, oddIndex = 0, 0
        
        while evenIndex < len(s) - 1:
            even1 = evenIndex
            even2 = evenIndex + 1
            evenCheck = True
            while(True):
                if(even1 < 0 or even2 >= len(s) or not evenCheck): 
                    break
                
                if(even1 >= 0 and even2 < len(s) and evenCheck):
                    if(s[even1] != s[even2]):
                        evenCheck = False
                    else:
                        evenLongest = len(s[even1:even2+1])
                        if evenLongest > longest: 
                            longest = evenLongest
                            longestSubStr = s[even1:even2+1]
                        even1 = even1 - 1
                        even2 = even2 + 1
            evenIndex = evenIndex + 1
        
        while oddIndex < len(s):
            odd1, odd2 = oddIndex, oddIndex
            oddCheck = True
            while(True):
                if(odd1 < 0 or odd2 >= len(s) or not oddCheck): 
                    break
                
                if(odd1 >= 0 and odd2 < len(s) and oddCheck):
                    if(s[odd1] != s[odd2]):
                        oddCheck = False
                    else:
                        oddLongest = len(s[odd1:odd2+1])
                        if oddLongest > longest:
                            longest = oddLongest
                            longestSubStr = s[odd1:odd2+1]
                        odd1 = odd1 - 1
                        odd2 = odd2 + 1
            oddIndex = oddIndex + 1
        
        return longestSubStr

                        