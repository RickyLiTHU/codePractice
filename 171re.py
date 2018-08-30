n_chars = ord('Z') - ord('A') + 1

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        col_id = 0
        for i, ch in enumerate(reversed(s)):
            c = ord(ch) - ord('A') + 1
            col_id += c * pow(n_chars, i)
        return col_id