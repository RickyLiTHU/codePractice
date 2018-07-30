class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n

        prev, current = 1, 2
        for i in range(3, n):
            prev, current = current, prev + current
        return current + prev