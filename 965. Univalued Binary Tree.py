Question:
A binary tree is uni-valued if every node in the tree has the same value.
Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.









Solution: Depth-First Search
  
Let's output all the values of the array. After, we can check that they are all equal.
To output all the values of the array, we perform a depth-first search.

class Solution(object):
    def isUnivalTree(self, root):
        vals = []

        def dfs(node):
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return len(set(vals)) == 1
