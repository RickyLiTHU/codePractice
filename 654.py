# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        root = TreeNode(nums[0])
        
        for v in nums[1:]:
            if v < root.val:
                tmp = root
                while tmp.right != None and tmp.right.val > v:
                    tmp = tmp.right
                if tmp.right == None:
                    tmp.right = TreeNode(v)
                else:
                    node = TreeNode(v)
                    node.left = tmp.right
                    tmp.right = node
            else:
                node = TreeNode(v)
                node.left = root
                root = node
            
        return root