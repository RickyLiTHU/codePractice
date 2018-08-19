class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums :
            return -2147483648      
        l = nums[:]
        for i in range(len(nums)-1)[::-1]:
            l[i] = max(nums[i], nums[i]+l[i+1])
        return max(l)