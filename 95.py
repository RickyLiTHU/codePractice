# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generate(low, high):
            if low > high:
                return [None]
            elif low == high:
                return [TreeNode(low)]
            elif (low, high) in memory:
                return memory[(low, high)]
            else:
                trees = []
            for root_val in range(low, high+1):

                left_subtrees = generate(low, root_val-1)
                right_subtrees = generate(root_val+1, high)
                
                
                for left_root in left_subtrees:
                    for right_root in right_subtrees:
                        root = TreeNode(root_val)
                        root.left = left_root
                        root.right = right_root
                        trees.append(root)
            memory[(low, high)] = trees
            return trees
    
        memory = {}
        return [] if n==0 else generate(1, n)