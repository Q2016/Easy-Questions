Question:
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.


Solution:Depth First Search
Let's find the leaf value sequence for both given trees. Afterwards, we can compare them to see if they are equal or not.
To find the leaf value sequence of a tree, we use a depth first search. Our dfs function writes the node's value if it is a 
leaf, and then recursively explores each child. This is guaranteed to visit each leaf in left-to-right order, as left-children are 
fully explored before right-children.

class Solution:
    def leafSimilar(self, root1, root2):
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)

        return list(dfs(root1)) == list(dfs(root2))
