class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):

        if len(path)> 1: res.append(path)

        visited = []
        for i in range(index, len(nums)):
            if nums[i] in visited: continue
            if not path or nums[i]>= path[-1]:
                visited+=[nums[i]]
                self.dfs(nums, i+1, path+[nums[i]], res)