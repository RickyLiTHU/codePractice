# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        idx = {}
        for i, preE in enumerate(preorder):
            idx[preE] = {}
            idx[preE]['pre'] = i
        for j, inE in enumerate(inorder):
            idx[inE]['in'] = j
        self.count = 0
        
        def build(idx, inorder, preorder, start, end):
            if start > end: return None
            if start == end:
                self.count += 1
                return TreeNode(inorder[start])
            
            #minIdx = len(inorder)
            #for n in inorder[start:end+1]:
            #    minIdx = min(minIdx, idx[n]['pre'])
            minIdx = self.count
            self.count += 1
            
            root = TreeNode(preorder[minIdx])
            root.left = build(idx, inorder, preorder, start, idx[preorder[minIdx]]['in']-1)
            root.right = build(idx, inorder, preorder, idx[preorder[minIdx]]['in']+1, end)
            return root
    
        return build(idx, inorder, preorder, 0, len(preorder)-1)