class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        Sum = 0
        if len(prices) < 2:
            return Sum
        ptr1 = 0
        ptr2 = 1
        while ptr2 < len(prices):
            if prices[ptr1] < prices[ptr2]:
                Sum += prices[ptr2] - prices[ptr1]
            ptr1 += 1
            ptr2 += 1
        return Sum