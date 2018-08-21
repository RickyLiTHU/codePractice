class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        d = collections.Counter(ages)
        count = 0
        for ((A,ac),(B,bc)) in itertools.product(d.items(),d.items()):
            count += (B <= A and B > A/2 + 7) * ac * (bc-(A==B))
        return count