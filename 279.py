class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        edges = []
        for i in range(1, int(math.ceil(math.sqrt(n)))+1):
            edges.append(i*i)
        
        depth = 1
        nodes = set([n])
        
        while nodes:
            nextLevel = set()
            for node in nodes:
                
                for e in edges:
                    if node - e == 0:
                        return depth
                    elif node - e > 0:
                        nextLevel.add(node-e)
                    else:
                        break
            
            depth += 1
            nodes = nextLevel