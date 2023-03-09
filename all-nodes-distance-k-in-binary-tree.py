# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.k = 0
        self.target = 0
        self.ans=[]
        self.s = set()

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.k = k
        self.target = target
        self.s = set()
        self.ans=[]
        self.search(root, target, k)
        return self.ans

    def search(self, root, target, k):
        if root == None:
            return float(inf)
        
        if root == target:
            self.s.add(root)
            self.ans+=self.distance(root, target, k)
            return k-1

        l = self.search(root.left, target, k)
        r = self.search(root.right, target, k)
        
        res = min(l,r)
        if res != float(inf):
            self.s.add(root)
            self.ans+=self.distance(root, target, res)
        
        return res - 1
    
    def distance(self, root, target, k):
        if root == None:
            return []
        if k == 0:
            return [root.val]
        l = []
        r = []
        if root.left not in self.s:
            l = self.distance(root.left, target, k-1)
        if root.right not in self.s:
            r = self.distance(root.right, target, k-1)
        
        return l+r