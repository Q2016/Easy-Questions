Question:
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:
Input: num = "69"
Output: true
Example 2:
Input: num = "88"
Output: true
Example 3:
Input: num = "962"
Output: false
Example 4:
Input: num = "1"
Output: true
Explanation
Create a reference mapping for strobo grammatic numbers. Then use the two-pointer technique to check if the numbers from 
left and right match the mapping.




Solution: Two pointers+ Dic

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mapping = {"9": "6", "6": "9", "8": "8", "1": "1", "0": "0"}

        left = 0
        right = len(num) - 1
        
        while left <= right:
            if num[left] in mapping and mapping[num[left]] == num[right]:
                left += 1
                right -= 1            
            else:
                return False
        
        return True
        
        
        
Time Complexity: ~N
Space Complexity: ~1
