Question:
Given two strings s and t, return true if s is a subsequence of t, or false otherwise. A subsequence of a string is a new string that is 
formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining 
characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. 
In this scenario, how would you change your code?


Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

    
    
    
    
    
    
Solution: Dynamic programming (Reduce the problem to smaller ones)
    
Solution 1: dynamic programming
The first solution I think when I see this problem is dynamic programming. Let dp[i][j] = 1 if s[:j] is substring of t[:i]. How can we find it:

If s[j] == t[i], then we need to search string s[:j-1] in t[:i-1]
If s[j] != t[i], then we need to search string s[:j] in t[:i-1]
Here we use also s = "!" + s trick which allows as to handle border cases with empty strings.

Complexity: time and space complexity is O(nm), because we need to iterate over all table once.

class Solution:
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
Solution 2: two pointers
You can notice, that actually we update only one element in each row of or dp table, so we do a lot of job which is not neccesary. 
Each moment of time we need to keep only two pointers: one for stirng s and one for string t. Then if we found new symbol in string t, 
which is equal to symbol in s, we move two pointers by one. If we did not found, then we move onle pointer for t.

Complexity is now only O(n + m) = O(n), because we traverse both strings only once.

class Solution:
    def isSubsequence(self, s, t):
        s_i, t_i = 0, 0
        
        while s_i < len(s) and t_i < len(t):
            s_i, t_i = s_i + (s[s_i] == t[t_i]), t_i + 1
            
        return s_i == len(s)
Solution 3: binary search for follow-up question.
If we have a lot strings S1, S2, ... , Sk, where k is big number we want to find faster method. Let us create for each symbol sorted list 
of indexes for this symbol.

Complexity, both time and space of preprocessing is O(n), we iterate once over our list.

Complexity of one search for string S_i is O(m_i)*log(n), where m_i is length of string and we have log(n) factor, because we potentially 
can have list of indexes with length n. So if m is the longest length of S_i, we have complexity O(k m log n), when two-pointer approach 
has O(k n) complexity. So, if length of original string n is big and m is small, it is worth to use this method.

class Solution:
    def isSubsequence(self, s, t):
        places = defaultdict(list)
        for i, symbol in enumerate(t):
            places[symbol].append(i)
        
        current_place = 0
        for symbol in s:
            current_ind = bisect.bisect_left(places[symbol], current_place)
            if current_ind >= len(places[symbol]):
                return False
            current_place = places[symbol][current_ind] + 1
            
        return True
