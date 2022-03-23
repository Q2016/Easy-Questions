Question:
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked 
lists have no intersection at all, return null.













Solution: (Smart Solution)

For a good understanding and explanation: 
    https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49785/Java-solution-without-knowing-the-difference-in-len!    
        
    

    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None

        node_a = headA 
        node_b = headB

        while node_a is not node_b:
            # if either pointer hits the end, switch head and continue the second traversal, 
            # if not hit the end, just move on to next
            node_a = headB if node_a is None else node_a.next
            node_b = headA if node_b is None else node_b.next

        return node_b # only 2 ways to get out of the loop, they meet or the both hit the end=None


