Question:
In a string s of lowercase letters, these letters form consecutive groups of the same character.
For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".
A group is identified by an interval [start, end], where start and end denote the start and end indices (inclusive) of the group. 
In the above example, "xxxx" has the interval [3,6].
A group is considered large if it has 3 or more characters.
Return the intervals of every large group sorted in increasing order by start index.

Example 1:
Input: s = "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the only large group with start index 3 and end index 6.

Solution: Two Pointer
We scan through the string to identify the start and end of each group. If the size of the group is at least 3, we add it to the answer.
Maintain pointers i, j with i <= j. The i pointer will represent the start of the current group, and we will increment j forward until it 
reaches the end of the group. We know that we have reached the end of the group when j is at the end of the string, or S[j] != S[j+1]. 
At this point, we have some group [i, j]; and after, we will update i = j+1, the start of the next group.

class Solution(object):
    def largeGroupPositions(self, S):
        ans = []
        i = 0 # The start of each group
        for j in xrange(len(S)):
            if j == len(S) - 1 or S[j] != S[j+1]:
                # Here, [i, j] represents a group.
                if j-i+1 >= 3:
                    ans.append([i, j])
                i = j+1
        return ans
