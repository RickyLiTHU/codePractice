# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not p.val < q.val: 
            p,q = q,p
        anchor = root
        
        if p.val == anchor.val: 
            return p
        if q.val == anchor.val:
            return q
        elif p.val < anchor.val and q.val > anchor.val:
            return anchor
        elif p.val > anchor.val and q.val > anchor.val: 
            return self.lowestCommonAncestor(anchor.right,p,q)
        elif p.val < anchor and q.val < anchor.val:
            return self.lowestCommonAncestor(anchor.left,p,q)