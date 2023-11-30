# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        to_delete = set(to_delete)

        def dfs(node):
            if not node:
                return None

            l = dfs(node.left)
            r = dfs(node.right)

            if l:
                node.left = None
            if r:
                node.right = None

            if node.val in to_delete:
                if node.left:
                    ans.append(node.left)
                if node.right:
                    ans.append(node.right)

                node.left = None
                node.right = None

                return True
        
        dfs(root)
        if root.val not in to_delete:
            ans.append(root)
        return ans
            
