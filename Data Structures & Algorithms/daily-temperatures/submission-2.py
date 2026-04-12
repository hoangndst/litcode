class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        res = [0] * n

        # 30,38,30,36,35,40,28
        # 
        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n:
                if temperatures[j] > temperatures[i]:
                    res[i] = j - i
                    break
                if res[j] == 0:
                    res[i] = 0
                    break
                else:
                    j += res[j]
        
        return res