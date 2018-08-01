class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if len(num) < 3:
            return False
        def fibGenerator(one, two, k):
            three = one + two
            res = str(three)
            while len(res) < k:
                one, two = two, three
                three = one + two
                res += str(three)
            return res
        for i in range(len(num) - 2):
            for j in range(i + 1, len(num) - 1):
                one, two = int(num[:i + 1]), int(num[i + 1:j + 1])
                # no leading zero
                if ((one == 0 and i == 0) or num[0] != '0') and ((two == 0 and i + 1 == j) or num[i + 1] != '0')\
                and fibGenerator(one, two, len(num) - j - 1) == num[j + 1:]:
                    return True
        return False