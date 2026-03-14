# https://leetcode.com/problems/contains-duplicate/

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n_set = set()
        for num in nums:
            if num in n_set:
                return True
            n_set.add(num)
        return False
        