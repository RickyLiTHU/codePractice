class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = set()
        for num in nums:
            if num in d:
                d.remove(num) 
            else:
                d.add(num)
        return d.pop()