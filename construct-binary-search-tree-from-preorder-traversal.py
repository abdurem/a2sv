# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
    
        root = TreeNode(preorder[0])
        stack = [root]

        for val in preorder[1:]:
            node = TreeNode(val)
            if val < stack[-1].val:
                stack[-1].left = node
            else:
                while stack and val > stack[-1].val:
                    parent = stack.pop()
                parent.right = node
            stack.append(node)

        return root