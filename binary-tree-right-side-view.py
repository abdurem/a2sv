# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        
        left = self.rightSideView(root.left)
        right = self.rightSideView(root.right)

        for i in range(min(len(left),len(right))):
            left[i] = right[i]
        
        left = [root.val]+left
        right = [root.val]+right

        return left if len(left) > len(right) else right