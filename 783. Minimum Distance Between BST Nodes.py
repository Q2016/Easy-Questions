Question:
Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.










Solution: Inorder traversal~sorted array
	
The idea is to use an in-order traversal and find the difference between the current node and the node previously checked.
Think of this question like a variation on "what is the smallest distance between any two values in a sorted array?" With a 
sorted array, all you do is scan through the entire array looking for the absolute minimum difference between two adjacent values 
since you know, when the array is sorted, that the answer can only be found between those two ADJACENT values.
To scan the BST like a sorted array, just go through IN-ORDER traversal and keep track of the previous node evaluated.

    pre = -float('inf')
    res = float('inf')

    def minDiffInBST(self, root):
        if root is None:
            return
        
        self.minDiffInBST(root.left)
	# evaluate and set the current node as the node previously evaluated
        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val
        self.minDiffInBST(root.right)
        return self.res
