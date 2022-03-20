Question:
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST. According to the definition of 
LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as 
descendants (where we allow a node to be a descendant of itself).”
                        6
                      /   \
                     2      8
                   /  \    / \
                  0    4  7   9
                      / \
                     3   5
Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

    
Solution: Top down traverse
  
  It's intresting, first you think this problem should not be solved with Top down. Look at the conditions below memorize them.
    
def lowestCommonAncestor(self, root, p, q):
    while root:
        if root.val > p.val and root.val > q.val:
            root = root.left
        elif root.val < p.val and root.val < q.val:
            root = root.right
        else:
            return root
