class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        if(num <= 10):
            return num
        strr = []
        for i in str(num):
            strr.append(i)
            
        
        pos = 0
        while(pos<len(strr)-1):
            to = strr[pos]
            pos+=1
            fm = max(strr[pos:])
            if(fm>to):
                index = len(strr)-1-strr[::-1].index(fm)
                
                strr[pos-1] = fm
                strr[index] = to
                
                return int("".join(strr))
            
        return num
