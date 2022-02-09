Question:
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. 
Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
  
Solution:
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
    	return sum(i in J for i in S)



class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
    	return sum(S.count(i) for i in J)



from collections import Counter

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
    	return sum(Counter(S)[i] for i in J)  
