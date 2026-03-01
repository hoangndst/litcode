# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers

class Solution:

    # Intuition:
    # - A deci-binary number contains only digits 0 or 1.
    # - We are given a decimal number n, and we must split it into the minimum number of deci-binary numbers whose sum equals n.
    # Approach
    # - Traverse the string.
    # - Track the maximum digit.
    # - Return that digit.
    # Complexity
    # - Time complexity: O(n)
    # - Space complexity: O(1)

    def minPartitions(self, n: str) -> int:
        return int(max(n))
