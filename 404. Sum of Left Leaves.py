Question:
Given the root of a binary tree, return the sum of all left leaves.

Solution:
Very simple problem, where we just need to traverse our tree and find left leaves.

Let us defint dfs(self, root, side), where root is current node and side is -1 if this node is left children of some other node and +1 if this node is right children of some node. Then:

If we reached None node, then we just return, we are out of tree
If current node do not have children, then we check that it is left children of some other node and if it is the case, we add its value to global self.sum.
Finally, run recursively dfs for left children with -1 and for right children with 1.
Complexity: time complexity is O(n), because we traverse every node only once. Space complexity is O(h), where h is height of our tree.

class Solution:
    def dfs(self, root, side):
        if not root: return
        
        if not root.left and not root.right:
            if side == -1: self.sum += root.val
        
        self.dfs(root.left, -1)
        self.dfs(root.right, 1)
    
    def sumOfLeftLeaves(self, root):
        self.sum = 0
        self.dfs(root, 0)
        return self.sum
