# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return '()'
        
        l = self.tree2str(root.left)
        r = self.tree2str(root.right)

        if l == '()' and r == '()':
            return str(root.val)
        elif r == '()':
            return str(root.val) + '(' + l + ')'
        else:
            if l == '()':
                return str(root.val) + l + '(' + r + ')'
            return str(root.val) + '(' + l + ')' + '(' + r + ')'