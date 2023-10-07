# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ans = 0
        self.dfs(root, targetSum, [0])
        return self.ans
    
    def dfs(self, node, targetSum, path):
        if not node:
            return
        sm = path[-1] + node.val
        diff = sm - targetSum
        self.ans += path.count(diff)
        path.append(sm)
        self.dfs(node.left, targetSum, path)
        self.dfs(node.right, targetSum, path)
        path.pop()
