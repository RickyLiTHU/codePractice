class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = curr = "0" * (n - 1)
        toVisit = collections.defaultdict(lambda : k - 1)
        for _ in range(k**n):
            res += str(toVisit[curr])
            toVisit[curr] -= 1
            curr = res[len(res) - n + 1:]
        return res