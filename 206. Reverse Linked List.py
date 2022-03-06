Question:
Given the head of a singly linked list, reverse the list, and return the reversed list.

 
 
 
 
 
 
 
 
 
 
 
 
  
Solution:
Graphics 
https://leetcode.com/problems/reverse-linked-list/discuss/1449712/Easy-C%2B%2BJavaPythonJavaScript-Explained%2BAnimated 
 
The idea is very simple, we maintain 3 pointers, current, next and previous, abbreviated as cur, n and prev respectively. All the events occur in a chain.
Preassign: assign prev=NULL, cur=head .
Below are the steps:
First we initialize n to be the node after cur. i.e(n=cur->next).
Then we make cur->next point to prev (next node pointer).
Then we make prev now point to (one node ahead) the cur node.
At last we move cur also one node ahead to n.
Follow the same steps untill the head points to NULL i.e there is no node to reverse. The prev pointer will be the last non null node and hence the answer. 

     def reverseList(self, head):
         prev = None
         cur = head

         while curr:
             n = cur.next
             cur.next = prev
             prev = cur
             cur = n
         return prev

        
This link is about my assignment confusion in Python:
https://stackoverflow.com/questions/3232376/python-variable-assignment-confusion/3232936
