class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        m, n, heap, trapped = len(heightMap), len(heightMap and heightMap[0]), [], 0
        for i in range(m):
            for j in range(n):
                if i in {0, m - 1} or j in {0, n - 1}:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    heightMap[i][j] = -1          
        while heap:
            h, i, j = heapq.heappop(heap)
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 < x < m and 0 < y < n and heightMap[x][y] != -1:
                    trapped += max(h - heightMap[x][y], 0)
                    heapq.heappush(heap, (max(heightMap[x][y], h), x, y))
                    heightMap[x][y] = -1
        return trapped