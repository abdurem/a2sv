# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d = self.count(root)
        mx = list(d)[0]
        ans=[]
        for i in d:
            if d[mx] < d[i]:
                mx = i
        for i in d:
            if d[i] == d[mx]:
                ans.append(i)
        return ans
    
    def count(self, root):
        if root == None:
            return defaultdict(int)
        
        l = self.count(root.left)
        r = self.count(root.right)

        for i in r:
            l[i] += r[i]
        l[root.val]+=1

        return l