# https://leetcode.com/problems/two-sum/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in m:
                return [m[diff], i]
            m[num] = i

        return []
