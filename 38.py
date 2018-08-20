class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def readString(s):
            temp = s[0]
            count = 1
            result = ''
            if len(s) == 1:
                return "11"

            for i in range(1, len(s)):
                if i == len(s) - 1:
                    if s[i] == temp:
                        count += 1
                        result += str(count) + s[i]
                    else:
                        result += str(count) + s[i-1] + "1" + s[i]
                else:    
                    if s[i] == temp:
                        count += 1
                    else:
                        result += str(count) + temp
                        temp = s[i]
                        count = 1

            return result
        
        def recursion(n):
            if n == 1:
                return "1"
            
            return readString(recursion(n-1))
        
        final = recursion(n)
        return final