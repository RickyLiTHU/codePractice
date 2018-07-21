class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        top_index = 0
        bottom_index = len(matrix) - 1
        right_index = len(matrix[0]) - 1
        
        if matrix[top_index][0] > target or matrix[bottom_index][right_index] < target:
            return False
        
        while matrix[top_index][right_index] < target:
            top_index += 1
        while matrix[bottom_index][0] > target:
            bottom_index -= 1
        
        for i in range(top_index, bottom_index+1):
            if self.binary_search(matrix[i], 0, right_index, target) != -1:
                return True
            
        return False
    
    def binary_search(self, array, p, r, x):
        if r < p:
            return -1
        q = (p+r) // 2
        if x == array[q]:
            return q
        elif x < array[q]:
            return self.binary_search(array, p, q-1, x)
        else:
            return self.binary_search(array, q+1, r, x)