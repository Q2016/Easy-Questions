Question:
Given the root of a binary tree, invert the tree, and return its root.
            4              4
          /   \          /   \
         2     7        7     2
        / \   / \      / \   / \ 
       1   3 6   9    9   6 3   1
Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

    




Solution: Recursive

    def invertTree(self, root):
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
        
