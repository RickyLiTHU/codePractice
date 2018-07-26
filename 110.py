# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def parse(self, node, depth):
        if node == None:
            return depth, True
        l_height, balancedl = self.parse(node.left, depth+1)
        r_height, balancedr = self.parse(node.right, depth+1)
        diff = abs(l_height - r_height)
        if diff > 1:
            return max(l_height, r_height), False
        return max(l_height, r_height), balancedl and balancedr
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        height, balanced = self.parse(root, 0)
        return balanced