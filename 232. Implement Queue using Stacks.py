Question:
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of 
a normal queue (push, peek, pop, and empty).
Implement the MyQueue class:
void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.



Solution:
The idea is to simulate a queue using two stacks (same as previous posts). I use python list as the underlying data structure for stack 
and add a "move()" method to simplify code: it moves all elements of the "inStack" to the "outStack" when the "outStack" is empty. Here is the code

class Queue(object):
    def __init__(self):
        self.inStack, self.outStack = [], []

    def push(self, x):
        self.inStack.append(x)

    def pop(self):
        self.move()
        self.outStack.pop()

    def peek(self):
        self.move()
        return self.outStack[-1]

    def empty(self):
        return (not self.inStack) and (not self.outStack) 
        
    def move(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
