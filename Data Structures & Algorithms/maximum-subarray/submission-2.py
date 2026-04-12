class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0

        # 2 -3 4 -2 2 1 -1 4
        # curSum = 8
        # maxSum = 8
        for n in nums:
            curSum = max(curSum, 0)
            curSum += n
            maxSum = max(maxSum, curSum)

        return maxSum