Question:
Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.
Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].
For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
 
Example 1:
Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

 
 
 
Solution:
If the characters at the index of i in both strings are identical, i.e. s[i] == goal[i], we call the characters at the index i as matched.
If swapping s[i] and s[j] would demonstrate that s and goal are buddy strings, then s[i] == goal[j] and s[j] == goal[i]. That means among the four 
free variables s[i], s[j], goal[i], goal[j], there are only two cases: either s[i] == s[j] or not.
 
 
  class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        if len(s) != len(goal): 
            return False
        
        if s == goal:
            seen = set()
            for a in s:
                if a in seen:
                    return True
                seen.add(a)
            return False

        pairs = []
        for a, b in zip(s, goal):
            if a != b:
                pairs.append((a, b))
            if len(pairs) >= 3: 
                return False
        return len(pairs) == 2 and pairs[0] == pairs[1][::-1]
       
Or we can just use: 
1- Use counter and compare the results for two strings 2- count the number of pairs that are not match, if more than two pairs=> False
