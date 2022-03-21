Question:
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

        
        
        
        
        
        
Solution: BST


def sortedArrayToBST(num):
    if (len(num) == 0):
        return None
    ead = helper(num, 0, len(num) - 1)
    return head;


def helper(num, low, high):
    if (low > high) :        
        return None
    mid = (low + high) / 2
    node = TreeNode(num[mid])
    node.left = self.helper(num, low, mid - 1)
    node.right = self.helper(num, mid + 1, high)
    return node

