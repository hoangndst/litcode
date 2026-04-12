class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero = 0

        for num in nums:
            if num:
                prod *= num
            else:
                zero += 1

        if zero > 1: return [0] * len(nums)

        res = [0] * len(nums)

        for i in range(len(nums)):
            if zero:
                res[i] = 0 if nums[i] else prod
            else:
                res[i] = prod // nums[i]
        
        return res
