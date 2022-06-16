Question:
Given two strings s and t, return true if t is an anagram of s, and false otherwise. An Anagram is a word or phrase formed by 
rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true  
  

  
  
  
  
  
  
  
  
Solution: Dictionary


  
def isAnagram1(self, s, t):
    dic1, dic2 = {}, {}
    for item in s:
        dic1[item] = dic1.get(item, 0) + 1
    for item in t:
        dic2[item] = dic2.get(item, 0) + 1
    return dic1 == dic2
    
def isAnagram2(self, s, t):
    dic1, dic2 = [0]*26, [0]*26
    for item in s:
        dic1[ord(item)-ord('a')] += 1
    for item in t:
        dic2[ord(item)-ord('a')] += 1
    return dic1 == dic2

  
Time O(N)  
    
       
def isAnagram3(self, s, t):
    return sorted(s) == sorted(t)
  
Time O(NlogN)
