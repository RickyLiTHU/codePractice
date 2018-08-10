class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = list()
        ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
        for token in tokens:
            if token in ops:
                t1 = int(stack.pop())
                t2 = int(stack.pop())
                res = ops[token](t2, t1)
                stack.append(res)
            else:
                stack.append(token)
        return int(stack.pop())