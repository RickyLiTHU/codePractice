# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        def isMirror(a, b):
            return a and b and a.val == b.val and isMirror(a.left, b.right) and isMirror(a.right, b.left) or a is b
        return isMirror(root.left, root.right)