class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 3:
            return 0
        water = 0
        maxindex = height.index(max(height))
        left = 0
        leftindex = 0
        for i in range(maxindex+1):
            if height[i] >= left:
                water += (i-leftindex-1) * left - sum(height[leftindex+1:i])
                left = height[i]
                leftindex = i
        right = 0
        rightindex = len(height)-1
        for j in range(len(height)-1,maxindex-1,-1):
            if height[j] >= right:
                water += (rightindex-j-1) * right - sum(height[j+1:rightindex])
                right = height[j]
                rightindex = j
        return water