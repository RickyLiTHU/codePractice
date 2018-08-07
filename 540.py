class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            lSize = mid - l

            if nums[mid - 1] < nums[mid] < nums[mid + 1]:
                return nums[mid]

            if nums[mid - 1] == nums[mid]:
                if lSize % 2 == 0:
                    r = mid
                else:
                    l = mid + 1

            else:
                if nums[mid] == nums[mid + 1]:
                    if lSize % 2 == 0:
                        l = mid
                    else:
                        r = mid - 1
                        
        return nums[l]