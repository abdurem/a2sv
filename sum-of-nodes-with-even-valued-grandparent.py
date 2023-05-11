# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        l = self.sumEvenGrandparent(root.left)
        r = self.sumEvenGrandparent(root.right)

        if root.val%2 == 0:
            return self.sumGrandChild(root,2)+l+r
        
        return l+r
    
    def sumGrandChild(self, root, depth):
        if root == None:
            return 0
        if depth == 0:
            return root.val
        
        l = self.sumGrandChild(root.left,depth-1)
        r = self.sumGrandChild(root.right,depth-1)

        ans=l+r
        return ans