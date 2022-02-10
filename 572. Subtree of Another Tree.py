Question:
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and 
node values of subRoot and false otherwise. A subtree of a binary tree tree is a tree that consists of a node in tree and all of 
this node's descendants. The tree tree could also be considered as a subtree of itself.

Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Solution:
Naive approach, O(|s| * |t|)
For each node of s, let's check if it's subtree equals t. We can do that in a straightforward way by an isMatch function: check if 
s and t match at the values of their roots, plus their subtrees match. Then, in our main function, we want to check if s and t match, or 
if t is a subtree of a child of s.

def isMatch(self, s, t):
    if not(s and t):
        return s is t
    return (s.val == t.val and 
            self.isMatch(s.left, t.left) and 
            self.isMatch(s.right, t.right))

def isSubtree(self, s, t):
    if self.isMatch(s, t): return True
    if not s: return False
    return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
