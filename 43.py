class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l_num1 = []
        l_num2 = []

        for i in range(len(num1)):
            l_num1.append(ord(num1[i])-ord('0'))
        number1 = 0
        for j in range(len(l_num1)):
            number1 = number1 * 10 + l_num1[j]
        
        for i in range(len(num2)):
            l_num2.append(ord(num2[i])-ord('0'))
        number2 = 0
        for j in range(len(l_num2)):
            number2 = number2 * 10 + l_num2[j]
        
        
        result = number1 * number2
        
        final_str_list =[]
        final_str = ''
        if(result==0):
            return '0'
        while(result > 0):
            n = result % 10
            result = int(result / 10)
            final_str_list.append(chr(n + ord('0')))
        
        for i in range(len(final_str_list)-1,-1,-1):
            final_str += (final_str_list[i])
        return final_str
