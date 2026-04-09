class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        prefix = [0] * n
        suffix = [0] * n
        # nums =   [1, 2, 4, 6]
        # prefix = [1, 1, 2, 12]
        # suffix = [48, 24, 6, 1]

        prefix[0] = suffix[n - 1] = 1
        for i in range(1, n):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]
        
        for i in range(n):
            res[i] = prefix[i] * suffix[i]
        return res