# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = defaultdict(lambda: float('-inf'))
        
        que = deque()
        que.append([0, root])
        
        while que:
            i, node = que.popleft()
            if not node:
                continue
            
            ans[i] = max(ans[i], node.val)
            
            que.append([i+1, node.left])
            que.append([i+1, node.right])
            
        return ans.values()
            
            