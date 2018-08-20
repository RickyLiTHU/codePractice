# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def twoReturnTree(self,root):
        #first get the diameter, then return the largest length
        if(root==None):
            return (0,0)
        if(root.left==None and root.right==None):
            return (0,0)
        elif(root.left==None):
            diameter, depth=self.twoReturnTree(root.right)
            return (max(diameter,depth+1), depth+1)
        elif(root.right==None):
            diameter, depth=self.twoReturnTree(root.left)
            return (max(diameter,depth+1), depth+1)
        else:
            diameterLeft,depthLeft=self.twoReturnTree(root.left)
            diameterRight,depthRight=self.twoReturnTree(root.right)
            depth=max(depthLeft,depthRight)+1
            diameter=max(depthLeft+depthRight+2,diameterLeft,diameterRight)
            return(diameter,depth)

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.twoReturnTree(root)[0]