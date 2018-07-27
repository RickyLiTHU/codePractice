class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while(low <= high):
            mid = (low + high) / 2
            if (mid == 0 or nums[mid - 1] < nums[mid]) and (mid == len(nums) - 1 or nums[mid] > nums[mid + 1]):
                return mid
            elif nums[mid - 1] > nums[mid]:
                high = mid - 1
            elif nums[mid] < nums[mid + 1]:
                low = mid + 1
        return 0 if nums[0] > nums[1] else 1   