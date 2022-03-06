Question:
Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements 
lies in [low, high]. Trimming the tree should not change the relative structure of the elements that will remain in the tree 
(i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.
Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.

 
 
 
 
 
 
 
Solution:Recursion
Let trim(node) be the desired answer for the subtree at that node. We can construct the answer recursively.
When node.val > high, we know that the trimmed binary tree must occur to the left of the node. Similarly, when node.val < low, 
the trimmed binary tree occurs to the right of the node. Otherwise, we will trim both sides of the tree.


class Solution(object):
    def trimBST(self, root, low, high):

        def trim(node):
            if not node:
                return None
            elif node.val > high:
                return trim(node.left)
            elif node.val < low:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node

        return trim(root)
