class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        window = set()
        for i in xrange(0, len(nums)):
            if len(window) >= k+1:
                window.remove(nums[i-k-1])
            if nums[i] in window:
                return True
            window.add(nums[i])
        return False