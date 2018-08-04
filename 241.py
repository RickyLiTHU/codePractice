class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        memo={}
        def helper(st,ed):
            key=(st,ed)
            if key in memo:
                return memo[key]
            if all([dig not in "+-*" for dig in expression[st:ed+1]]):
                return [int(expression[st:ed+1])]
            ans=[]
            for sp in range(st+1,ed):
                if expression[sp] in "+-*":
                    lefts=helper(st,sp-1)
                    rights=helper(sp+1,ed)
                    for left in lefts:
                         for right in rights:
                                if expression[sp]=="-":
                                    ans.append(left-right)
                                if expression[sp]=="+":
                                    ans.append(left+right)
                                if expression[sp]=="*":
                                    ans.append(left*right)
            memo[key]=ans
            return ans
        return helper(0,len(expression)-1)