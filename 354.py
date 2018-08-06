class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes = sorted(envelopes, key = lambda x : -x[1])
        envelopes = sorted(envelopes, key = lambda x : x[0])
        tails = []
        for i in range(0, len(envelopes)):
            width = envelopes[i][1]
            j = bisect.bisect_left(tails, width)
            if j == len(tails):
                tails.append(width)
            else:
                tails[j] = width
        return len(tails)