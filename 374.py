# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        startIdx = 1
        endIdx = n

        while (startIdx <= endIdx):
            midIdx = (startIdx + endIdx)//2

            if guess(midIdx) == 0:
                return midIdx
            elif guess(midIdx) == 1:
                startIdx = midIdx + 1
            elif guess(midIdx) == -1:
                endIdx = midIdx - 1