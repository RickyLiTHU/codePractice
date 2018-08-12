class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        if buckets == 1:
            return 0
        if minutesToTest // minutesToDie <= 1:
            return buckets - 1
        # general case: just get the n in n^(test_times + 1) = buckets
        return int(math.ceil(math.log(buckets, (minutesToTest // minutesToDie) + 1)))