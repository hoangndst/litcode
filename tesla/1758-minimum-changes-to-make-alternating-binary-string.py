# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/
class Solution:
    def minOperations(self, s: str) -> int:
        curr = cnt1 = 0
        for c in s:
            if int(c) != curr:
                cnt1 += 1
            curr ^= 1
        
        curr = 1
        cnt2 = 0
        for c in s:
            if int(c) != curr:
                cnt2 += 1
            curr ^= 1
    
        return min(cnt1, cnt2)
