class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force
        # time complexity: O(n * m)
        # space complexity: O(m)
        # n is length of string
        # m is total of unique characters in the string
        # res = 0
        # for i in range(len(s)):
        #     char_set = set()
        #     for j in range(i, len(s)):
        #         if s[j] in char_set: # O(1)
        #             break
        #         char_set.add(s[j])
        #     res = max(res, len(char_set))
        # return res

        # solution 2

        res = 0
        char_set = set()
        l = 0
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            res = max(res, len(char_set))
        
        return res

