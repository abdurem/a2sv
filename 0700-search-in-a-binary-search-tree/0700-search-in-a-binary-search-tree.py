# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return None
        node=None
        if root.val > val:
            node=self.searchBST(root.left, val)
        elif root.val < val:
            node=self.searchBST(root.right, val)
        else:
            return root
        return node