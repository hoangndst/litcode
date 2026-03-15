# https://leetcode.com/problems/valid-palindrome/

"""
Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.
Example 3:
    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.
"""
class Solution:
    # 1. reverse string
    # time complexity: O(n)
    # space complexity: O(n)
    def isPalindrome(self, s: str) -> bool:
        newStr = "" # space: O(n)
        for c in s: # time: O(n)
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]

    # 2. two pointers
    # time complexity: O(n)
    # space complexity: O(1)
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while l < r and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    
    def alphaNum(self, c):
        return (ord("a") <= ord(c) <= ord("z") or
                ord("A") <= ord(c) <= ord("Z") or
                ord("0") <= ord(c) <= ord("9"))
