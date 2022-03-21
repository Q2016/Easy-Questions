Question:
A permutation, "perm", of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:
s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.

Example 1:
Input: s = "IDID"
Output: [0,4,1,3,2]

    
    
Solution:
If we see say S[0] == 'I', we can always put 0 as the first element; similarly, if we see S[0] == 'D', we can always put N as the first element.
Say we have a match for the rest of the string S[1], S[2], ... using N distinct elements. Notice it doesn't matter what the elements are, 
only that they are distinct and totally ordered. Then, putting 0 or N at the first character will match, and the rest of the elements 
(1, 2, ..., N or 0, 1, ..., N-1) can use the matching we have.

class Solution(object):
    def diStringMatch(self, S):
        lo, hi = 0, len(S)
        ans = []
        for x in S:
            if x == 'I':
                ans.append(lo)
                lo += 1
            else:
                ans.append(hi)
                hi -= 1

        return ans + [lo]
