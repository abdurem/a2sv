# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        count = {}
        ans = []

        def ver(root, row, col):
            if not root:
                return 
            if col in count:
                if row in count[col]:
                    insort_left(count[col][row],root.val)
                else:
                    count[col][row] = [root.val]
            else:
                count[col] = {row:[root.val]}
           
            ver(root.left, row +1, col - 1)
            ver(root.right, row+ 1,col + 1)
            return 
        ver(root, 0, 0)
    
        cols = sorted(count)
        
        for col in cols:
            res = []
            rows = sorted(count[col])
            for row in rows:
                res.extend(count[col][row])
            ans.append(res)
        return ans