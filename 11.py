class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0 # i points to the beginning
        j = len(height) - 1 # j points to the end
        max_area = 0
        while i < j: # i and j will get closer to eachother but never pass, ensuring every element is only visited once
            width = abs(i-j) # the distance between i and j, set before i or j is reassigned
            if height[i] < height[j]: # the lower wall dictates vertical distance bc gravity
                    h = height[i]
                    i += 1 # if the i wall is lower, move forward to try to find a taller wall
            else:
                    h = height[j]
                    j -= 1 # if the j wall is lower, move backwards to try to find a taller wall
            max_area = max(max_area, h * width)
        return max_area