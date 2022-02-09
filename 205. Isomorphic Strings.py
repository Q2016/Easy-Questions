Question:
Given two strings s and t, determine if they are isomorphic. Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters 
may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Solution:
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        cnt_s=Counter(list(s))
        cnt_t=Counter(list(t))
        
        print(cnt_s)
        
        arr1=[]
        for _,j in cnt_s.items():
            arr1.append(j)
            
        arr2=[]
        for _,j in cnt_t.items():
            arr2.append(j)
            
        if arr1==arr2:
            return True
        else:
            return False  
