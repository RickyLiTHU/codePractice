class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ss = collections.Counter(s)
        tt = collections.Counter(t)
        res = tt-ss
        return res.keys()[0]
