# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)

        mn = min(l,r)
        if l == 0:
            mn = r
        elif r == 0:
            mn = l

        return mn+1