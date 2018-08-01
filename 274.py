class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations = sorted(citations)
        n = len(citations)
        start = 0
        end = n - 1
        res = 0
        while start <= end:
            mid = int((start + end)/2)
            h = n - mid
            if h <= citations[mid]:
                res = max(h, res)
                end = mid - 1
            else:
                start = mid + 1
                
        return res
