Question:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Implement the MinStack class:
MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.

Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Solution:
# https://codereview.stackexchange.com/questions/167534/python-implementation-of-stack-to-return-minimum-in-o1-time


class MinStack:

    def __init__(self):
        self.element_stack = []
        self.min_element_stack = []
    
    
    def push(self, item: int) -> None:
        if self.size() == 0:
            self.min_element_stack.append(item)
        else:
            self.min_element_stack.append(min(self.min_element_stack[self.size() - 1], item))
        self.element_stack.append(item)
        

    def pop(self) -> None:
        if self.is_empty():
            raise ValueError('Empty stack')
        self.min_element_stack.pop()
        return self.element_stack.pop()
        

    def top(self) -> int:
        return self.element_stack[-1]

    def getMin(self) -> int:
        if self.is_empty():
            raise ValueError('Empty stack')
        return self.min_element_stack[self.size() - 1]

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.element_stack)
