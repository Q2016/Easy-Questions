Question:
Given the head of a singly linked list, reverse the list, and return the reversed list.

 
  
Solution:
Graphics 
https://leetcode.com/problems/reverse-linked-list/discuss/1449712/Easy-C%2B%2BJavaPythonJavaScript-Explained%2BAnimated 
 
     def reverseList(self, head):
         prev = None
         cur = head

         while curr:
             n = cur.next
             cur.next = prev
             prev = cur
             cur = n

         return prev
