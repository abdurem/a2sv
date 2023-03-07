# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = self.traverse(root)
        return arr == sorted(arr) and len(set(arr)) == len(arr)
    
    def traverse(self, root):
        if root == None:
            return []
        
        arr=self.traverse(root.left)
        arr.append(root.val)
        arr+=self.traverse(root.right)

        return arr