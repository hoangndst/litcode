# https://leetcode.com/problems/valid-palindrome-ii

class Solution:
    """Brute force
    1. check if the original string is a palindrome -> return True
    2. for each index i from 0 to (n - 1)
       - create new string by removing the character at index i
       - check if new string is palindrome -> return True
    3. if no removal gives a paralindrome -> return False 

    Time: O(n^2)
    Space: O(n)
    """
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        
        for i in range(len(s)):
            newS = s[:i] + s[i + 1:]
            if newS == newS[::-1]:
                return True
        
        return False
    
    """Two pointers
    1. init two pointers: l, r = start, end of string
    2. while l < r
       - if s[l] == s[r] move l++, r--
       - if they differ. check 2 possibility:
            - skip left character and check s[l + 1 ... r]
            - skip right character and check s[l ... r - 1]
       - return True
    3. return True if the loop complete without mismatches

    time: O(N)
    space: O(N)
    """

    def validPalindrome(self, s: str) -> bool:
        l ,r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skipL = s[l + 1 : r + 1]
                skipR = s[l : r]
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            l, r = l + 1, r - 1 

        return True
