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
        if p.val < root.val < q.val or p.val > root.val > q.val:
            return root
        
        if root.val > p.val and root.val > q.val:
            l = self.lowestCommonAncestor(root.left, p, q)
            return l
        if root.val < p.val and root.val < q.val:
            r = self.lowestCommonAncestor(root.right, p, q)
            return r
        
        return root