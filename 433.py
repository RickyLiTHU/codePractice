class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        return self.min_muts(start, end, bank, set())
    
    def min_muts(self, start, end, bank, visited):
        if start == end:
            return 0
        
        visited.add(start)        
        min_dist = sys.maxint
        for b in bank:
            if self.dist(start, b) == 1 and b not in visited:
                dist = self.min_muts(b, end, bank, visited)
                if dist != -1:
                    min_dist = min(dist, min_dist)                
        visited.remove(start)
        return min_dist + 1 if min_dist != sys.maxint else -1

    def dist(self, s, e):
        return sum([1 if si != ei else 0 for (si, ei) in zip(s, e)])