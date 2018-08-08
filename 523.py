class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not k: return any(nums[i] == nums[i - 1] == 0 for i in range(1, len(nums)))
        mods, sm = set(), 0
        for i, num in enumerate(nums):
            sm = (sm + num) % k
            if sm in mods or (not sm and num and i): return True
            mods |= {sm}
        return False