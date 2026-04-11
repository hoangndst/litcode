class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        res = 0

        # res = 3
        # mp = {a:0 | b:2  | c : 3 }
        # a b b c a
        #     l
        #         r


        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)

        return res