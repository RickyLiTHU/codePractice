class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        heap, count = [], collections.Counter(words)
        for key, value in count.items():
            heap.append((-value, key))
        top = heapq.nsmallest(k, heap)
        return [word[1] for word in top]