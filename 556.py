class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n>2**30-1:
            return -1
        string_n = [a for a in str(n)]
        permutation_values=[]
				
        i = len(string_n)-1
        while i>=0 and (not permutation_values or int(string_n[i]) >= int(permutation_values[-1])):
            permutation_values.append(string_n[i])
            i-=1
        if i==-1 and len(permutation_values)==len(string_n): 
            return -1
        
        for j in range(len(permutation_values)): 
            if int(permutation_values[j])>int(string_n[i]):
                string_n[i], permutation_values[j]=permutation_values[j], string_n[i]
                break

        string_n[i+1:]=permutation_values
                    
        
        return int("".join(string_n))
