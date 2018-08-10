class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        cache = {}
        def helper(X):
            if len(X) == 1:
                # Any integer can be divide by 1
                return 1
            
            if X in cache:
                return cache[X]
            total = 0
            for j in range(len(X)):
                if X[j] % len(X) == 0 or len(X) % X[j] == 0:
                    total += helper(X[:j] + X[j+1:])
                    
            cache[X] = total 
            return total 
        
        return helper(tuple(range(1, N+1)))
