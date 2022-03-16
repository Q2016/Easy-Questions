Question:
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
Can be solved in O(n).

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].





Solution: Two pointers
The question boils down to understanding that if we look at the magnitude of the elements in the array at both ends and gradually 
"slide down" and converge towards the center of the array. With that understanding, we can use two pointers, one at each end, 
to iteratively collect the larger square to a list. However, collecting the larger square in a list with list's append, results 
in elements sorted in descending order. To circumvent this, we need to append to the left of the list. Using a collections.deque() 
allows us to append elements to the left of answer in O(1) time, maintaining the required increasing order.

def sortedSquares(self, A):
    answer = collections.deque()
    l, r = 0, len(A) - 1
    while l <= r:
        left, right = abs(A[l]), abs(A[r])
        if left > right:
            answer.appendleft(left * left)
            l += 1
        else:
            answer.appendleft(right * right)
            r -= 1
    return list(answer)


Or for O(nlog n): 
    def sortedSquares(self, A: List[int]) -> List[int]:
        for i in range(len(A)):
            A[i] *= A[i]
        A.sort()
        return A    

similarly:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([v**2 for v in A])
