class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbol2num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res, idx, size = 0, 0, len(s)
        for idx, value in enumerate(s):
            if idx < size - 1 and symbol2num[s[idx]] < symbol2num[s[idx + 1]]:
                res -= symbol2num[s[idx]]
            else:
                res += symbol2num[s[idx]]
        return res