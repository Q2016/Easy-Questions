Question:
Given the head of a singly linked list, reverse the list, and return the reversed list.

 
  
Solution:
# https://programmercave0.github.io/blog/2018/01/23/C++-Reverse-the-Linked-List-(Iterative-Method)-program


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        prev=None
        
        while head:
            curr=head
            head=head.next
            curr.next=prev
            prev=curr    
