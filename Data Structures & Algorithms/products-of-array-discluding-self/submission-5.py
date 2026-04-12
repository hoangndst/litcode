class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # 1 2 3 4
        # res = [1, 1, 2, 6] prefix
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]
        
        # 1 2 3 4
        # res = [1, 1, 2, 6] postfix
        postfix = 1
        for i in range(n - 2, -1, -1):
            postfix *= nums[i + 1]
            res[i] *= postfix
        
        return res