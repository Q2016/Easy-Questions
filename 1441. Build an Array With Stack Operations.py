Question:
You are given an array target and an integer n. In each iteration, you will read a number from list = [1, 2, 3, ..., n].
Build the target array using the following operations: "Push": Reads a new element from the beginning list, and pushes it in the array.
"Pop": Deletes the last element of the array. If the target array is already built, stop reading more elements.
Return a list of the operations needed to build target. The test cases are generated so that the answer is unique.

Example 1:
Input: target = [1,3], n = 3
Output: ["Push","Push","Pop","Push"]
Explanation: 
Read number 1 and automatically push in the array -> [1]
Read number 2 and automatically push in the array then Pop it -> [1]
Read number 3 and automatically push in the array -> [1,3]

Solution:
Step 1: Create an empty list res to store the result.
Step 2: Add the elements of the input array target to a set to improve lookup performance.
Step 3: Iterate through the integers of target and add "Push" to the res list for each integer in 
range(1, target[-1] + 1). Then, add "Pop" if the integer is not in the set.
Step 4: Return the result.

* Note: The n parameter is not used in this approach.

def solution(target, n):
    res = []
	s = set(target)
    for i in range(1, target[-1] + 1):
        res.append("Push")
        if i not in s:
            res.append("Pop")
    return res
