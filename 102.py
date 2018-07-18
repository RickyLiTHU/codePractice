# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        output = []
        temp_list = [[root]]
        
        while temp_list:
            cur = temp_list.pop()
            temp_output = []
            candidates = []
            
            for entry in cur:
                if entry:
                    temp_output.append(entry.val)
                    if entry.left:
                        candidates.append(entry.left)
                    if entry.right:
                        candidates.append(entry.right)
                    
            if temp_output:
                output.append(temp_output)
            if candidates:
                temp_list.append(candidates)
            
        return output