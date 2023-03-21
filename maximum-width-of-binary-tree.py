class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        max_width = 0
        queue = [(root, 0)]
        
        while queue:
            level_size = len(queue)
            left_index = queue[0][1]
            
            for i in range(level_size):
                node, index = queue.pop(0)
                
                if node.left:
                    queue.append((node.left, 2*index))
                if node.right:
                    queue.append((node.right, 2*index + 1))
                    
            right_index = index
            
            max_width = max(max_width, right_index - left_index + 1)
        
        return max_width