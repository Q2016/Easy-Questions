Question:
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Sample I/O
Example 1
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3







Solution: Deque
The question is to show basic concept of queue which is FIFO.


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.dq = collections.deque()
        self.size = size

    def next(self, val: int) -> float:
        if len(self.dq) == self.size:
            self.dq.popleft()
            self.dq.append(val)
        else:
            self.dq.append(val)
        return sum(self.dq)/len(self.dq)

      
      
We append or pop each value for he constant time so the time complexity is O(1).  
