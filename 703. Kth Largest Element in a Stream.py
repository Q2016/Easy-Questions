Question:
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.
Implement KthLargest class:
KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
 
Example 1:
Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8


Solution:
So now that we know what a heap does, how does it help solve this problem? Let's say we have some stream of numbers, 
nums = [6, 2, 3, 1, 7], and k = 3. Because the input is small, we can clearly see the kth smallest element is 3. Although, 
earlier we said that a heap can only find an element in O(1) time if it's a minimum or maximum (depending on choice of implementation). 
Well, a heap is also capable of removing the smallest element quickly, so what if we just keep removing the smallest element from nums 
until nums.length == k? In this case, we would have nums = [3, 6, 7], and a heap can now give us our answer in O(1) time.
That's the key to solving this problem - use a min-heap (min means that the heap will remove/find the smallest element, a max heap is 
the same thing but for the largest element) and keep the heap at size k. That way, the smallest element in the heap (the one we can access in O(1)) 
will always be the kth largest element. This way, when adding a number to the heap with add(), we can do it very quickly in log(n) time. 
If our heap exceeds size k, then we can also remove it very quickly. In the end, the smallest element in the heap will be the answer.
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
