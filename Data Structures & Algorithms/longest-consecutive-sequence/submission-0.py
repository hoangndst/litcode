class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for n in nums:
            temp = n
            if temp - 1 in s:
                continue
            l = 0
            while temp in s:
                temp += 1
                l += 1
            if l > longest:
                longest = l
        return longest
