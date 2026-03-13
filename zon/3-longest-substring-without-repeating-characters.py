# https://leetcode.com/problems/longest-substring-without-repeating-characters/

"""
Given a string s, find the length of the longest substring without duplicate characters.
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
"""

class Solution:
    # brute force
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            char_set = set()
            for j in range(i, len(s)):
                if s[j] in char_set:
                    break
                char_set.add(s[j])
            res = max(res, len(char_set))
    
        return res
    # time: O(N * M)
    # space: O(M)

    # sliding window
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        char_set = set()

        for r in range(len(s)): # O(N)
            while s[r] in char_set: # O(N)
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            res = max(res, len(char_set))
        return res
    # time: O(2N) N is length of string
    # space: O(M) M is unique char in string

    # sliding window optimal
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        mp = {}

        # mp = {a: 0, ...}
        # a b b c a
        #         r
        #     l
        # -> l = max(0 + 1, 2) = 2
        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res
    
    # time: O(N)
    # space: O(M)