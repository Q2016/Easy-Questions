Question:
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example:
Input: head = [1,1,2,3,3]
Output: [1,2,3]    


    

Solution:

    def deleteDuplicates(self, head):

        first, second = head, head.next if head else None
        while second:
            if first.val == second.val:
                second = second.next
                first.next = second
            else:
                first = second
                second = second.next
                
        return head
