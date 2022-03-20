Question:
Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.

Example:
Input: root = [4,2,5,1,3], target = 3.714286
    4
   / \
  2   5
 / \
1   3
Output: 4



Solution: Time O(log n)
 

    def closestValue(root, target) :
        return closest(root, target, root.val)
    
    def closest(node, target, val) :
        if (node == None) return val
        if (math.abs(node.val - target) < math.abs(val - target)): 
            val = node.val
        if (node.val < target): 
            val = closest(node.right, target, val)
        elif (node.val > target): 
            val = closest(node.left, target, val);
        return val;
     
