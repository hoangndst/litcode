class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pMap = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in pMap:
                return [pMap[diff], i]
            pMap[num] = i
        return []
        