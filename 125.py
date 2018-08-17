class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        check = "".join(re.findall(r"\w+|\d+", s.lower()))
        return check == check[::-1]