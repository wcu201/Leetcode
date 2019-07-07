'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        read = {}
        longest, currentLongest = 0, 0
        
        p1, p2 = 0, 0
        p1Mode = False
        dup = ' '
        while(True):
            if(p2 >= len(s)):
                break
            if(not p1Mode):
                if s[p2] not in read:
                    currentLongest = currentLongest + 1
                    if currentLongest > longest: longest = currentLongest
                    read[s[p2]] = 1
                    p2 = p2 + 1
                else:
                    p1Mode = True
                    dup = s[p2]
            else:
                if s[p1] == dup:
                    p1Mode = False
                    p2 = p2 + 1
                else:
                    del read[s[p1]]
                    currentLongest = currentLongest - 1
                p1 = p1 + 1   
        if currentLongest > longest: longest = currentLongest       
        return longest
            