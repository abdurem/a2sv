# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root == None:
            return []            
        if root.left == None and root.right == None:
            return [str(root.val)]
        
        l = self.binaryTreePaths(root.left)
        for i in range(len(l)):
            l[i] = str(root.val)+'->'+l[i]
        
        r=self.binaryTreePaths(root.right)
        for i in range(len(r)):
            r[i] = str(root.val)+'->'+r[i]

        return l+r