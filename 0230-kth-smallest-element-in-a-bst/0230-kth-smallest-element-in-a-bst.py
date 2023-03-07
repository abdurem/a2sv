# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = None
        self.k = k
        def traverse(node):
            if node == None:
                return None
            
            traverse(node.left)
            self.k-=1
            if self.k == 0:
                self.ans =  node
                return self.ans
            
            traverse(node.right)
            return node
        
        traverse(root)
        return self.ans.val

        
