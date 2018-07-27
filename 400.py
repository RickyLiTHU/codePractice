class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=9:return n
        tmp_sum = 9
        num = 9
        num2 = 1
        while n>=tmp_sum:
            if n==tmp_sum:return 9
            num*=10
            num2+=1
            tmp_sum+=(num*num2)
        tmp_sum -= (num*num2)
        n = n-tmp_sum
        c1 = n/num2
        c2 = n%num2
        if c2==0:return (num/9+c1-1)%10
        return int(str(num/9+c1)[c2-1])