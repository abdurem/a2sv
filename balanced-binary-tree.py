# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root) >= 0
    
    def height(self, root):
        if root == None:
            return 0
        
        l=self.height(root.left)+1
        r=self.height(root.right)+1

        if abs(l-r) > 1:
            return float(-inf)
        return max(l,r)