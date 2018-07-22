class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        occurA = [(ele, A.count(ele)) for ele in set(A)]
        occurB = [(ele, B.count(ele)) for ele in set(B)]
        occurC = [(ele, C.count(ele)) for ele in set(C)]
        occurD = [(ele, D.count(ele)) for ele in set(D)]
        hashtable = {}
        for a,a_count in occurA:
            for b,b_count in occurB:
                hashtable[a+b] =hashtable.get(a+b,0) + a_count*b_count  
        count = 0         
        for c,c_count in occurC :
            for d,d_count in occurD :
                if -c - d in hashtable :
                    count += c_count*d_count*hashtable[-c-d]
        return count