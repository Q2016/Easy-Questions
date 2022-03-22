Question:
Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. 
This path may or may not pass through the root. The length of the path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [5,4,5,1,1,5]
Output: 2

    
    
    
    
    
    
Solution: DFS, Similar to 543. Diameter of Binary Tree
I added the solution of 543 below:
   def diameterOfBinaryTree(self, root):
        self.ans = 0
        def depth(p):
            if not p: return 0
            left, right = depth(p.left), depth(p.right)
            self.ans = max(self.ans, left+right)
            return 1 + max(left, right)
            
        depth(root)
        return self.ans

    
Original solution to 687:    
The approach is similar to the Diameter of Binary Tree question except that we reset the left/right to 0 whenever the current node does not match 
the children node value. In the Diameter of Binary Tree question, the path can either go through the root or it doesn't.
Hence at the end of each recursive loop, return the longest length using that node as the root so that the node's parent can potentially use it 
in its longest path computation. We also use an external variable longest that keeps track of the longest path seen so far.

class Solution(object):
    def longestUnivaluePath(self, root):
        self.ans = 0

        def arrow_length(node):
            if not node: return 0
            left_length = arrow_length(node.left)
            right_length = arrow_length(node.right)
            left_arrow = right_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1
            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1
            self.ans = max(self.ans, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

        arrow_length(root)
        return self.ans
    
    
    
Complexity Analysis
Time Complexity: O(N), where N is the number of nodes in the tree. We process every node once.
Space Complexity: O(H), where H is the height of the tree. Our recursive call stack could be up to H layers deep.
    
