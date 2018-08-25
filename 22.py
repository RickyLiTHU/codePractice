class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []     
        self.backtrack("", n, n, result, n * 2)
        return result
    
    def backtrack(self, partial, open_remaining, closed_remaining, result, max_len):
        if len(partial) == max_len:
            result.append(partial)
            return

        if open_remaining == closed_remaining and open_remaining > 0:
            self.backtrack(partial + "(", open_remaining - 1, closed_remaining, result, max_len)
            
        elif open_remaining < closed_remaining:
            if open_remaining > 0:
                self.backtrack(partial + "(", open_remaining - 1, closed_remaining, result, max_len)
            if closed_remaining > 0:
                self.backtrack(partial + ")", open_remaining, closed_remaining - 1, result, max_len)