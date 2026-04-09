class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        for i in range(len(height)):
            for j in range(i, len(height)):
                h = height[i] if height[i] <= height[j] else height[j]
                w = j - i
                if h != 0:
                    res = max(res, h * w)

        return res