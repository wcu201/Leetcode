'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''

class Solution:
    def helper(self, encoded: str, ind: int):
        currentWord = k = ""
        i = ind
        while(i < len(encoded)):
            if encoded[i].isdigit(): k+=encoded[i]
            if encoded[i]==']': return (currentWord, i)
            if encoded[i].isdigit()==False and encoded[i]!='[':currentWord+=encoded[i]
            if encoded[i]=='[':
                word = self.helper(encoded, i+1)
                for x in range(int(k)):currentWord+=word[0]
                i, k = word[1], ""
            i+=1
        return currentWord
                   
    def decodeString(self, s: str) -> str:
        result = self.helper(s, 0)
        return result


#Recursive solution. Use a recursive helper funciton that calls itself x times dependent on the number it reads from the string
