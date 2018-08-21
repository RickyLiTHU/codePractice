class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        visited = set()
        for i in range(len(graph)):
            if i in visited or len(graph[i]) == 0:
                continue
            level = {i}
            while level:
                next_level = set()
                for j in level:
                    visited.add(j)
                    for n in graph[j]:
                        if n in level:
                            return False
                        if n not in visited:
                            next_level.add(n)
                level = next_level
        return True