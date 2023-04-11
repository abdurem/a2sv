"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
            
        if not root.children:
            return 1
        
        arr = []
        for i in root.children:
            arr.append(self.maxDepth(i)+1)
        
        return max(arr)