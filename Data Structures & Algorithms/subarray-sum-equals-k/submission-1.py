class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        cur_sum = 0
        prefix_sums = {0 : 1}

        for num in nums:
            cur_sum += num

            target = cur_sum - k
            if target in prefix_sums:
                count += prefix_sums[target]
            
            prefix_sums[cur_sum] = prefix_sums.get(cur_sum, 0) + 1

        return count
