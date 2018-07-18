class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = list(string.ascii_lowercase)
        if len(s) == 0:
            return -1
        while len(l) > 0:
            for i in s:
                if i in l: 
                    if s.count(i) == 1:
                        return s.index(i)
                    else:
                        l.remove(i)
            break
        return -1