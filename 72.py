class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word1) == 0 and len(word2) == 0:
            return 0

        distanceBetweenPrefixes = []

        for i in range(len(word1)):
            distanceBetweenPrefixes.append([-1] * len(word2))

        def helper(word1, idx_1, word2, idx_2):
            if idx_1 < 0:
                return idx_2 + 1
            if idx_2 < 0:
                return idx_1 + 1
            if distanceBetweenPrefixes[idx_1][idx_2] == -1:
                if word1[idx_1] == word2[idx_2]:
                    distanceBetweenPrefixes[idx_1][idx_2] = helper(word1, idx_1 - 1, word2, idx_2 -1)
                else:
                    subLast = helper(word1, idx_1 - 1, word2, idx_2 -1)
                    addLast = helper(word1, idx_1, word2, idx_2-1)
                    deleteLast = helper(word1, idx_1-1, word2, idx_2)
                    distanceBetweenPrefixes[idx_1][idx_2] = 1 + min(subLast, addLast, deleteLast)
            return distanceBetweenPrefixes[idx_1][idx_2]

        return helper(word1, len(word1)-1, word2, len(word2)-1)