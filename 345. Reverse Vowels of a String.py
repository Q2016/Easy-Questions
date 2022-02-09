Question:
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

Example 1:
Input: s = "hello"
Output: "holle"

Solution:
class Solution:
    def reverseVowels(self, s: str) -> str:
        
        s=list(s)
        
        vowels=[]
        for c in s:
            if c in ["a","e","i","o","u","A","E","I","O","U"]:
                vowels.append(c)
        
        vowels=vowels[::-1]
        
        res=[]                
        n=0
        for c in s:
            if c in ["a","e","i","o","u","A","E","I","O","U"]:
                res.append(vowels[n])
                n+=1
            else:
                res.append(c)
                
        return "".join(res)
      
