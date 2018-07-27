class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2 != 0:
            return False
        else:
            return self._can_partition(nums, sum(nums) / 2, [])

    def _can_partition(self, nums, target, path):
        invalid = []  # the numbers that, if included in the subset, will not sum up to the target
        for (i, n) in enumerate(nums):
            if i in path:
                continue
            if n in invalid:
                continue
            if n > target:
                continue
            elif n == target:
                return True
            else:
                path.append(i)
                if self._can_partition(nums, target - n, path):
                    return True
                path.pop()
            invalid.append(n)
        return False