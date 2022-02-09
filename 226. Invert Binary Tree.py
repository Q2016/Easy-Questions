Question:
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Solution:

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root: 
            tmp=self.invertTree(root.right)
            root.right=self.invertTree(root.left)
            root.left=tmp
        
        return root
        
