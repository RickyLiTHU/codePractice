# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        Q = collections.deque([root,None])
        lastnode,res = None,0
        while Q:
            node = Q.popleft()
            if lastnode == None:
                res = node.val
            lastnode = node
            if node == None:
                if not Q:
                    return res
                Q.append(None)
                continue

            if node.left: Q.append(node.left)
            if node.right: Q.append(node.right)