# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        stack = [TreeNode(postorder.pop())]
        s = stack[0]
        prev = None
        while postorder:
            while stack and stack[-1].val == inorder[-1]:
                inorder.pop()
                prev = stack.pop()
            cur = TreeNode(postorder.pop())
            if prev:
                prev.left = cur
                prev = None
            elif stack:
                stack[-1].right = cur
            stack.append(cur)
        return s