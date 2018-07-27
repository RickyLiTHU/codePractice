class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)%2 == 0 or len(nums) == 1:
            return True

        n = len(nums)
        dp = [[[0,0] for row in xrange(n)] for _ in xrange(n)]
        
        for i in range(n):
            dp[i][i] = [nums[i], 0]
        
        for length in xrange(2,n+1):
            for i in range(n-length+1):
                j = i + length-1
                # pick i:
                pi = dp[i+1][j][1] + nums[i]
                # pick j:
                pj = dp[i][j-1][1] + nums[j]
                if pi > pj:
                    dp[i][j][0] = pi
                    dp[i][j][1] = dp[i+1][j][0]

                else:
                    dp[i][j][0] = pj
                    dp[i][j][1] = dp[i][j-1][0]

        return dp[0][-1][0] >= dp[0][-1][1]