class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def is_connected(arr, i, j):
            if parent(arr, i) == parent(arr, j): return True
            return False
            
        def parent(arr, i):
            while i != arr[i]:
                i = arr[i]
            return i
                    
        def union(arr, i, j):
            iroot = parent(arr, i)
            jroot = parent(arr, j)
            if iroot == jroot: return
            arr[iroot] = jroot
            
        _max = list(sorted([i for pair in edges for i in pair]))[-1]
        
        data = [i for i in range(0, _max+1)]

        found = []
        for i, j in edges:
            if is_connected(data, i, j):
                found.append([i, j])
            else:
                union(data, i, j)        
        return [i for pair in found for i in pair]