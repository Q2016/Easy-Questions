Question:
You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.
We repeatedly make duplicate removals on s until we no longer can. Return the final string after all such duplicate removals have been made. 
It can be proven that the answer is unique.

Example 1:
Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  
The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".


Solution:
If current char is same as previous char in the ArrayDeque, pop out the previous char;
Otherwise, add current char into the ArrayDeque.

    def removeDuplicates(self, S: str) -> str:
        dq = collections.deque()
        for c in S:
            if dq and dq[-1] == c:
                dq.pop()
            else:
                dq.append(c)
        return ''.join(dq)
Or just use list:

    def removeDuplicates(self, S: str) -> str:
        stack = []
        for c in S:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)
