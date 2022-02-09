Question:
Given two strings s and t, return true if s is a subsequence of t, or false otherwise. A subsequence of a string is a new string that is 
formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining 
characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Solution:
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        k=0

        if s=="":
            return True
        
        if len(s)==1 and s in t:
            return True
        
        while i <= j and j< len(t):
            if t[i]==s[k]:
                j=i
                j+=1
            else:
                i+=1
                j=i
                continue

            k+=1
            if k==len(s):
                return False

            while j< len(t):
                if t[j]==s[k]:
                    i=j

                    if k==len(s)-1:
                        return True
                    break
                else:
                    j+=1

        if k==len(s):
            return True
        else:
            return False
                        
                    
