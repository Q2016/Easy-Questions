Question:
Given two strings s and t, return true if s is a subsequence of t, or false otherwise. A subsequence of a string is a new string that is 
formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining 
characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

    
    
Solution: Dynamic programming (Reduce the problem to smaller ones)
The first solution I think when I see this problem is dynamic programming. Let dp[i][j] = 1 if s[:j] is substring of t[:i]. How can we find it:

If s[j] == t[i], then we need to search string s[:j-1] in t[:i-1]
If s[j] != t[i], then we need to search string s[:j] in t[:i-1]
Here we use also s = "!" + s trick which allows as to handle border cases with empty strings.

Complexity: time and space complexity is O(nm), because we need to iterate over all table once.

    def isSubsequence(self, s, t):
        s, t = "!" + s, "!" + t
        m, n = len(s), len(t)
        dp = [[0] * m for _ in range(n)] 
        for i in range(n): dp[i][0] = 1
   
        for i,j in product(range(1, n), range(1, m)):
            if s[j] == t[i]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j]
                    
        return dp[-1][-1]
