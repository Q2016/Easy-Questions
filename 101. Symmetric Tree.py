Question:
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).












Solution: Recursive

Start from the root, check left and right then after that check every subtree i.e. left.right with right.left and right.left with left.right 

class Solution:
  def isSymmetric(self, root):
    if root is None:
      return True
    else:
      return self.isMirror(root.left, root.right)

  def isMirror(self, left, right):
    if left is None and right is None:
      return True
    if left is None or right is None:
      return False

    if left.val == right.val:
      outPair = self.isMirror(left.left, right.right)
      inPiar = self.isMirror(left.right, right.left)
      return outPair and inPiar
    else:
      return False
    
Time: O(n) # just visiting every element of the tree
Space: O(n) # space complexity of the stack    
    
    
    
    
The essence of recursively is Stack, so we can use our own stack to rewrite it into iteratively:

 class Solution2:
  def isSymmetric(self, root):
    if root is None:
      return True

    stack = [[root.left, root.right]]

    while len(stack) > 0:
      pair = stack.pop(0)
      left = pair[0]
      right = pair[1]

      if left is None and right is None:
        continue
      if left is None or right is None:
        return False
      if left.val == right.val:
        stack.insert(0, [left.left, right.right])

        stack.insert(0, [left.right, right.left])
      else:
        return False
    return True
