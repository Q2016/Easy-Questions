Question:
You are given an integer array nums consisting of n elements, and an integer k. Find a contiguous subarray whose length is equal to k that has 
the maximum average value and return this value. 

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75


Solution: Sliding Window
We want to find the maximum K-length sum. After, we can divide by K to get the average.
We have two techniques for getting these sums efficiently: prefix sums, or sliding window.

In the first approach, we calculate P[i] = A[0] + A[1] + ... + A[i-1] in linear time. Then, A[i] + A[i+1] + ... + A[i+K-1] = P[i+K] - P[i], 
and we should find the max of these.


def findMaxAverage(self, A, K):
    P = [0]
    for x in A:
        P.append(P[-1] + x) # creates cumsum

    ma = max(P[i+K] - P[i] for i in range(len(A) - K + 1)) # sliding window
    return ma / float(K)



In the second approach, we maintain su = the sum of A[i-K+1] + A[i-K+2] + ... + A[i]. Then, when we have K elements in this sum (if i >= K-1), 
it is a candidate to be the maximum sum ma.


def findMaxAverage(self, A, K):
    su = 0
    ma = float('-inf')
    for i, x in enumerate(A):
        su += x
        if i >= K:
            su -= A[i-K]
        if i >= K - 1:
            ma = max(ma, su)
    return ma / float(K)
