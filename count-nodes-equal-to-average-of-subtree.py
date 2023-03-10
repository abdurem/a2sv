# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        return self.subTree(root)[2]

    def subTree(self, root):
        if root == None:
            return [0,0,0]
        
        
        l = self.subTree(root.left)
        r = self.subTree(root.right)

        nodes = l[1]+r[1]+1
        sm = root.val + l[0]+ r[0]
        count = l[2]+r[2]

        if root.val == sm // nodes:
            return [sm, nodes, count+1]
        
        return [sm, nodes, count]
        


        return avg