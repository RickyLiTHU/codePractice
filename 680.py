class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s[::-1]==s:
            return True
        i=0
        j=len(s)-1
        while(i<j):
            if s[i] != s[j]:
                sA=s[:i]+s[i+1:]
                sB=s[:j]+s[j+1:]
                if sA==sA[::-1] or sB==sB[::-1]:
                    return True
                else:
                    return False
            i+=1
            j-=1