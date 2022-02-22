Question:
Given a n-ary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value.
                1
              / | \
             3  2  4
            / \
           5   6
Example:
Input: root = [1,null,3,2,4,null,5,6]
Output: 3

Solution: DFS

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        return 1 + max((self.maxDepth(node) for node in root.children), default=0)    
    
or longer version:
    
Solution:
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # Base case
        if root == None:
            return 0
        # Depth level of the tree
        depth = 0
        
        # Loops through children array
        for child in root.children:
            # Compares current depth of depth with a new level of depth 
            # Sets the biggest value to variable depth
            depth = max(depth, self.maxDepth(child))
        
        # As going deeper into the tree increases depth by 1
        #print ('root ' + str(root.val) + ' depth ' + str(depth + 1))
        return depth + 1 
    

