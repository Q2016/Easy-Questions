Question:
Given the root of a binary tree, return its maximum depth. A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.












Solution: Recursive
    
Trick is to assume depth 0 at a not that satisfies (Not node==True) and recursivly go up the tree.    
    
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

   
Time: O(N) - for DFS
Space: O(N) - for the recursive stack
    
    

Iterative
from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        worklist = deque([root])
        num_node_level = 1
        levels = 0
        while worklist:
            node = worklist.popleft()
            if node.left:
                worklist.append(node.left)
            if node.right:
                worklist.append(node.right)
            num_node_level -= 1
            if num_node_level == 0:
                levels += 1
                num_node_level = len(worklist)
                
        return levels  
    
    

