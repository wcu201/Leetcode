'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        result = []
        
        for word in strs:
            order = list(word)
            order.sort()
            key = ''.join(order)
            if key in anagrams: anagrams[key].append(word)
            else: anagrams[key]=[word]
        
        for key, val in anagrams.items(): result.append(val)
        
        return result

#Store anagrams in hashmap based key that is the sorted version of the word which by definition should be the same for anagrams