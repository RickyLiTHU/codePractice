class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        ans = down = height = 0
        for i in range(n):
            if not i:
                ans = prev = 1
            elif ratings[i] >= ratings[i-1]:
                if down:
                    ans += (down+1) * down // 2 + max(down + 1 - height, 0)
                    down = height = 0
                prev = prev + 1 if ratings[i] > ratings[i-1] else 1
                ans += prev
            else:
                if not height: height = prev
                down += 1
                prev = 1
        if down: ans += max(down + 1 - height, 0)
        return ans + (down+1) * down // 2