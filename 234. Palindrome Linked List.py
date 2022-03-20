Question:
Given the head of a singly linked list, return true if it is a palindrome.















Solution: Two pointers

This can be solved by reversing the 2nd half and compare the two halves. Let's start with an example [1, 1, 2, 1].

In the beginning, set two pointers fast and slow starting at the head.

1 -> 1 -> 2 -> 1 -> null 
sf
(1) Move: fast pointer goes to the end, and slow goes to the middle.

1 -> 1 -> 2 -> 1 -> null 
          s          f
(2) Reverse: the right half is reversed, and slow pointer becomes the 2nd head.

1 -> 1    null <- 2 <- 1           
h                      s
(3) Compare: run the two pointers head and slow together and compare.

1 -> 1    null <- 2 <- 1             
     h            s
          
          
def isPalindrome(head) :
    fast = head 
    slow = head
    while (fast != None and fast.next != None): 
        fast = fast.next.next # double speed
        slow = slow.next
    
    if (fast != None) : # odd nodes: let right half smaller
        slow = slow.next
    
    slow = reverse(slow)
    fast = head
    
    while (slow != None) :
        if (fast.val != slow.val) :
            return False
        fast = fast.next
        slow = slow.next
    return True


def reverse(head) :
    prev = None
    while (head != None) :
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev

