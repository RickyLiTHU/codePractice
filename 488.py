class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        hm = collections.defaultdict(int)
        for b in hand: 
            hm[b] += 1
        def longestConsecutive(board):
            start,s,e = 0,0,0
            for i in xrange(len(board)):
                if board[i] != board[start]:
                    start = i
                if i-start > e-s:
                    s,e = start,i
            return (s,e)
        def minStep(board):
            i,n,localMin = 0,len(board),float('inf')
            if n==0: return 0
            start,end = longestConsecutive(board)
            if end-start > 1:
                return minStep(board[:start]+board[end+1:])
            while i < n:
                ball,step = board[i],1 if i < n-1 and board[i]==board[i+1] else 2
                if hm[ball] >= step:
                    hm[ball] -= step
                    ms = minStep(board[:i]+board[i+3-step:])
                    localMin = min(localMin,(step+ms) if ms != -1 else localMin)
                    hm[ball] += step
                i += 3-step
            return localMin if localMin != float('inf') else -1
        return minStep(board)