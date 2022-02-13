Question:
Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.

Solution:
class Solution(object):
    def closestValue(self, root, target):

        if root is None:
            return float('inf')

        if root.val == target:
            return root.val
        elif root.val < target:
            rightRes = self.closestValue(root.right, target)
            return root.val if abs(root.val - target) < abs(rightRes - target) else rightRes
        elif root.val > target:
            leftRes = self.closestValue(root.left, target)
            return root.val if abs(root.val - target) < abs(leftRes - target) else leftRes
