# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        que = deque([root])
        ans = []
        while que:
            tot = 0
            arr = []
            l = len(que)

            for q in que:
                tot += q.val
                if q.left:
                    arr.append(q.left)
                if q.right:
                    arr.append(q.right)
            
            ans.append(tot/l)
            que = arr
        
        return ans