Question:
Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. 
This path may or may not pass through the root. The length of the path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [5,4,5,1,1,5]
Output: 2

Solution:

# made an assumption that repeateds are connected
# you have to bottom up not top down

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        res=[]
        
        def dfs(node):
            if not node: return 0
            rightdfs(node.right)
            dfs(node.left)
            if node.right and node.right.val==node.val:
                l_right+=1
            if node.left and node.left.val==node.val:
                l_left=+=1
            
            res.append(node.val)
        
        
        if not root: return 0
        
        dfs(root)
        cnt=Counter(res)
        #print(cnt)
        #print(cnt.most_common(1)[0][1])
        return(cnt.most_common(1)[0][1]-1)
