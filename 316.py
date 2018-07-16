from collections import Counter

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = Counter(s)
        seen, stack = set(), []
        for c in s:
            cnt[c] -= 1
            if c not in seen:
                while stack and stack[-1] > c and cnt[stack[-1]]:
                    seen.remove(stack.pop())
                stack.append(c)
                seen.add(c)
        return "".join(stack)
