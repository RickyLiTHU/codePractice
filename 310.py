class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 0:
            return []
        elif len(edges) == 0:
            return [0]

        graph = {}

        for (x, y) in edges:
            if x in graph:
                graph[x].append(y)
            else:
                graph[x] = [y]
            if y in graph:
                graph[y].append(x)
            else:
                graph[y] = [x]

        def bfs(start_vertex):
            visited = [0] * n
            queue = [(start_vertex, 0)]
            max_steps, node = 0, start_vertex
            trace = []
            trace.append(start_vertex)
            while queue:
                u, steps = queue.pop(0)
                if max_steps < steps:
                    max_steps = steps
                    node = u
                    trace.append(u)
                visited[u] = True
                for v in graph[u]:
                    if not visited[v]:
                        queue.append((v, steps + 1))

            return (node, max_steps, trace)

        u, _, _ = bfs(0)
        w, diameter, trace = bfs(u)
        radius = int(diameter / 2)
        if diameter % 2 == 0:
            return trace[radius:radius + 1]
        else:
            return trace[radius:radius + 2]
