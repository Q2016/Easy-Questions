Question:
Given an array of strings words, return true if it forms a valid word square.
A sequence of strings forms a valid word square if the kth row and column read the same string, where 0 <= k < max(numRows, numColumns).

Example 1:
Input: words = ["abcd","bnrt","crmy","dtye"]
Output: true
Explanation:
The 1st row and 1st column both read "abcd".
The 2nd row and 2nd column both read "bnrt".
The 3rd row and 3rd column both read "crmy".
The 4th row and 4th column both read "dtye".
Therefore, it is a valid word square.


Solution:
Check if words[i][j] == words[j][i] and if the lengthes of columns and rows match.

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i in range(len(words)):
            for j in range(len(words[i])):
                if i != j and (j >= len(words) or i >= len(words[j]) or words[i][j] != words[j][i]):
                    return False
            
        return True
        
        
Time Complexity: O(MN).
Space Complexity: O(1).
