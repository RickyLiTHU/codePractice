class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        newS="#"+"#".join(list(s))+"#"
        z=[0]*len(newS)
        center,right=1,1
        for i in range(1,len(newS)):
            if i>right:
                    center=i
                    right=i
            if z[2*center-i]+i<right:
                z[i]=z[2*center-i]
            else:
                center=i
                left=2*center-right
                while left-1>=0 and right+1<len(newS) and newS[left-1]==newS[right+1]:
                    left-=1
                    right+=1
                z[i]=right-i
            count+=(z[i]/2+z[i]%2)
        return count