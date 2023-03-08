# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None

        l = self.lowestCommonAncestor(root.left, p, q)          
        r = self.lowestCommonAncestor(root.right, p ,q)
        
        if (root == p or root == q) or (l and r):
            return root
        
        return l or r