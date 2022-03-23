Question:
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

Example 1:
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

    
    
    
    
    
    
Solution:

Method 1:

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        elif root.val < L:
            return self.rangeSumBST(root.right, L, R)
        elif root.val > R:
            return self.rangeSumBST(root.left, L, R)
        return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)

 
solution from 669. Trim a Binary Search Tree:
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
    
    
    
    
The following are two more similar recursive codes.

Method 2:

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        return self.rangeSumBST(root.left, L, R) + \
                self.rangeSumBST(root.right, L, R) + \
                (root.val if L <= root.val <= R else 0)
Method 3:

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        sum = 0
        if root.val > L:
            sum += self.rangeSumBST(root.left, L, R)
        if root.val < R:
            sum += self.rangeSumBST(root.right, L, R)
        if L <= root.val <= R:
            sum += root.val     
        return sum
