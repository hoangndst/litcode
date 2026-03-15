# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.
"""
from typing import List

class Solution:
    """
    1. Brute force
    time: O(n^2)
    space: O(1)
    the brute force approach checks every posible buy-sell pair
    for each day, we pretend to buy the stock, and then we look all the future days to see
    what the best selling price would be. Among all these profits, we keep the highest one.
    """
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i + 1, len(prices)):
                sell = prices[j]
                res = max(res, sell - buy)
        return res
    
    """
    2. Two pointers
    time: O(n)
    space: O(1)
    we use 2 pointers:
    - l for buy day
    - r for sell day
    if price at r is higher than price at l, we can make profit, then update max profit
    if price at r is lower, then set l = r because cheaper buy is always better
    move r to next day.
    """
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                p = prices[r] - prices[l]
                maxP = max(maxP, p)
            else:
                l = r
            r += 1
        return maxP

    """
    3. DP
    time: O(n)
    space: O(1)

    as we scan through the prices, we keep track two things:
    - the lowest price -> this is the best day to buy
    - the best profit -> selling day - lowest buy price seen earlier
    """
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP