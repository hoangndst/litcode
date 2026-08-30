class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # position of car in miles
        # speed of car in miles / hour
        # target - miles
        # 1. only catch up to another car and then drive at same speed

        # ------- 1 2 3 4 5 6 7 8 9 10
        # car1(3)       *
        # car2(2)            *
        
        pair = []
        for i in range(len(position)):
            p = (position[i], speed[i])
            pair.append(p)
        
        pair.sort(reverse=True)

        stack = []
        for p, s in pair:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)