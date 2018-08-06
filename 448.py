class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        y = []
        x = [0]*(len(nums))
        for i in nums:
            x[i-1] = 1
        for i,val in enumerate(x):
            if val == 0:
                y.append(i+1)
        return y;
