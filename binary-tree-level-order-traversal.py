# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        l = self.levelOrder(root.left)
        r = self.levelOrder(root.right)

        c = []
        arr=[[root.val]]
        if l or r:
            length = min(len(l),len(r))
            for i in range(length):
                arr += [l[i] + r[i]]
            arr+=l[length:]+r[length:]

        return arr