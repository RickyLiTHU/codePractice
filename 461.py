class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x_ = '{0:b}'.format(x).zfill(32)
        y_ = '{0:b}'.format(y).zfill(32)
        counter = 0
        for i,j in zip(x_,y_):
            if i != j:
                counter += 1
        return counter