class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = ""
        carry = 0
        if len(num1) <= len(num2):
            for i in range(1,len(num1)+1):
                carry, num = divmod(int(num1[-i])+int(num2[-i])+carry,10)
                num = str(num)
                res  = num + res
            for j in range(len(num1)+1,len(num2)+1):
                carry, num = divmod(int(num2[-j])+carry,10)
                num = str(num)
                res  = num + res
            if carry != 0:
                res = str(carry) + res
            return res
        else:
            for i in range(1,len(num2)+1):
                carry, num = divmod(int(num1[-i])+int(num2[-i])+carry,10)
                num = str(num)
                res  = num + res
            for j in range(len(num2)+1,len(num1)+1):
                carry, num = divmod(int(num1[-j])+carry,10)
                num = str(num)
                res  = num + res
            if carry != 0:
                res = str(carry) + res
            return res