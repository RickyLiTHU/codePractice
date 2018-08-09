# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        def construct(node):
            if node is not None:
                cur_str = str(node.val)
                if node.left and node.right:
                    return "{}({})({})".format(cur_str, construct(node.left), construct(node.right))
                elif node.left:
                    return "{}({})".format(cur_str, construct(node.left))
                elif node.right:
                    return "{}()({})".format(cur_str, construct(node.right))
                else:
                    return "{}".format(cur_str)
                return cur_str
            else:
                return ''
        return construct(t)