Question:
Given the root of a binary tree, return all root-to-leaf paths in any order. A leaf is a node with no children.


Solution:
# dfs + stack
    def binaryTreePaths1(self, root):
        if not root:
            return []
        res, stack = [], [(root, "")]
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls+str(node.val))
            if node.right:
                stack.append((node.right, ls+str(node.val)+"->"))
            if node.left:
                stack.append((node.left, ls+str(node.val)+"->"))
        return res
        
    # bfs + queue
    def binaryTreePaths2(self, root):
        if not root:
            return []
        res, queue = [], collections.deque([(root, "")])
        while queue:
            node, ls = queue.popleft()
            if not node.left and not node.right:
                res.append(ls+str(node.val))
            if node.left:
                queue.append((node.left, ls+str(node.val)+"->"))
            if node.right:
                queue.append((node.right, ls+str(node.val)+"->"))
        return res
        
    # dfs recursively
    def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        self.dfs(root, "", res)
        return res
    
    def dfs(self, root, ls, res):
        if not root.left and not root.right:
            res.append(ls+str(root.val))
        if root.left:
            self.dfs(root.left, ls+str(root.val)+"->", res)
        if root.right:
            self.dfs(root.right, ls+str(root.val)+"->", res)
			
    def binaryTreePaths1(self, root):
        return self.dfs(root, "")
    
    def dfs(self, root, path):
        if not root:
            return []
        path += str(root.val)
        if not root.left and not root.right:
            return [path]
        path += "->"
        return self.dfs(root.left, path) + self.dfs(root.right, path)
    
    def binaryTreePaths(self, root): # inorder
        stack, ret = [(root, "")], []
        while stack:
            node, path = stack.pop()
            if node:
                if not node.left and not node.right:
                    ret.append(path+str(node.val))
                s = path + str(node.val) + "->"
                stack.append((node.right, s))
                stack.append((node.left, s))    
        return ret
        
