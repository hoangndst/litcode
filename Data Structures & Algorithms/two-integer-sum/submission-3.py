class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pMap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in pMap:
                return [pMap[diff], i]
            pMap[nums[i]] = i
        return []
        