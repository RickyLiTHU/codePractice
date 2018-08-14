class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        ans = [0] * (n + 1)
        stack = []
        prev_time = 0
        prev_idx = n
        for log in logs:
            idx, action, t = log.split(':')
            idx, t = int(idx), int(t)
            ans[prev_idx] += t - prev_time
            prev_time = t
            if action == 'start':
                stack.append(prev_idx)
                prev_idx = idx
            else:
                ans[prev_idx] += 1
                prev_time += 1
                prev_idx = stack.pop()
        return ans[:n]