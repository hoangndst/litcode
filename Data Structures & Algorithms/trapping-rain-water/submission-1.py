class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        res = 0

        for i in range(n):
            leftMax = rightMax = height[i]

            for j in range(i):
                leftMax = max(height[j], leftMax)
            for j in range(i + 1, n):
                rightMax = max(height[j], rightMax)
            
            res += min(leftMax, rightMax) - height[i]

        return res