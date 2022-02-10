Question:
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].


Solution:

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
The question boils down to understanding that if we look at the magnitude of the elements in the array, A, both ends "slide down" and converge towards the center of the array. With that understanding, we can use two pointers, one at each end, to iteratively collect the larger square to a list. However, collecting the larger square in a list with list's append, results in elements sorted in descending order. To circumvent this, we need to append to the left of the list. Using a collections.deque() allows us to append elements to the left of answer in O(1) time, maintaining the required increasing order.

Alternative without deque or list reversal

def sortedSquares(self, A):
    answer = [0] * len(A)
    l, r = 0, len(A) - 1
    while l <= r:
        left, right = abs(A[l]), abs(A[r])
        if left > right:
            answer[r - l] = left * left
            l += 1
        else:
            answer[r - l] = right * right
            r -= 1
    return answer
We first declare a list of length, len(A) then add the larger square from the back of the list, denoted by the index r - l.

Shorter, terribly unreadable version - 6 lines

def sortedSquares(self, A):
    l, r, answer = 0, len(A) - 1, [0] * len(A)
    while l <= r:
        left, right = abs(A[l]), abs(A[r])
        answer[r - l] = max(left, right) ** 2
        l, r = l + (left > right), r - (left <= right)
    return answer
