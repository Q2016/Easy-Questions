Question:
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.















Solution:
Just inorder travel the tree.
Note: There are at least two nodes in this BST.

    def getMinimumDifference(self, root):
        L = []
        def dfs(node):
            if node.left: dfs(node.left)
            L.append(node.val)
            if node.right: dfs(node.right)
        dfs(root)
        return min(b - a for a, b in zip(L, L[1:]))


Similarity to 700. Search in a Binary Search Tree:
    
class Solution:
    def searchBST(self, root, val):
        if root and val < root.val: return self.searchBST(root.left, val)
        elif root and val > root.val: return self.searchBST(root.right, val)
        return root
