class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        def helper(a, divisor): 
            if dividend < divisor:
                return 0,0
            d = divisor
            next_d = d + d
            q = 1
            while next_d <= a:
                d = next_d
                next_d += next_d
                q += q
            return d, q

        negSign = (dividend>0) ^ (divisor>0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        d, q = helper(dividend, divisor)
        while dividend - d >= divisor:
            dd, qd = helper(dividend - d, divisor)
            d += dd
            q += qd
        return min(2147483647, (-1 if negSign else 1) * q)