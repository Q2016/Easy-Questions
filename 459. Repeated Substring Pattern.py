Question:
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

Example 1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Solution:
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        if len(s)==1:
            return False

        cnt=Counter(s)

        frequencies = list(cnt.values())

        f=math.gcd(*frequencies)
        
        if f==1:
            return False
        
        part=len(s)//f
        for i in range(f-1):
            if s[0+i*part:part+i*part]!=s[0+(i+1)*part:part+(i+1)*part]:
                return False
        return True
