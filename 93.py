class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result=[0]*4
        returnList=[]
        self.backTraceRecursive(0,0,result,returnList,s)
        return returnList

    def backTraceRecursive(self,base,k,result,returnList,s):
        if k==3 and len(s)-base<=3 and self.isOK(s[base:]) and base<len(s):
            result[k]=s[base:]
            returnList.append(".".join(result))

        elif k<3 and base<len(s) and (len(s)-base)>=(4-k) and (len(s)-base)<=(4-k)*3:
            for i in range(1,4):
                newbase=base+i
                result[k]=s[base:newbase]
                if self.isOK((result[k])):
                    self.backTraceRecursive(newbase, k + 1, result, returnList, s)
        else:
            return


    def isOK(self,s):
        if len(s)>3 or len(s)<1 or (len(s)>1 and s[0]=='0'):
            return False

        if int(s)>255:
            return False
        return True