Question:
Given a number N, return true if and only if it is a confusing number, which satisfies the following condition:
We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively. 
When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid. A confusing number is a number that when rotated 180 degrees becomes a 
different number with each digit valid.

Example 1:
Input: 6
Output: true
Explanation: 
We get 9 after rotating 6, 9 is a valid number and 9!=6.


Solution:
Create a mapping between numbers and their rotated numbers and check if the reversed string can be same as their rotated string.

class Solution:
    def confusingNumber(self, N: int) -> bool:
        mapping = {
            '0': '0',
            '1': '1',            
            '6': '9',
            '8': '8',
            '9': '6',            
        }
        
        rotated_str = ""
        n_str = str(N)
        for c in n_str[::-1]:
            if c not in mapping:
                return False
            else:
                rotated_str += mapping[c]
                
        return rotated_str != n_str
                
                
Time Complexity: O(N).
Space Complexity: O(N).
