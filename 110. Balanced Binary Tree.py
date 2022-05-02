Question:
Given a binary tree, determine if it is height-balanced. For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.












Solution: Recursive
Trick is to use max depth for this problem, maxdepth is done in 104

class Solution:
    result = True;

    def isBalanced(TreeNode root) :
        maxDepth(root)
        return result

    def maxDepth(TreeNode root):
        if (root == None):
            return 0
        l = maxDepth(root.left)
        r = maxDepth(root.right)
        if (abs(l - r) > 1):
            result = False
        return 1 + max(l, r)

