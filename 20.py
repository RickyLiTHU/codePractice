class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        len_s = len(s)
        if len_s%2 != 0:
            return False
        #stack method
        my_list = []
        count = 0
        for sub_s in s:
            if sub_s in '({[':
                my_list.append(sub_s)
                count = count + 1
            elif len(my_list)!=0 and (sub_s+my_list.pop() in [')(', '][', '}{']):
                count = count - 1
            else:
                return False
        return True and count == 0