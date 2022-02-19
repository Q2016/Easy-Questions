Question:
Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).
The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

Example 1:
Input: s = "011101"
Output: 5 
Explanation: 
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5 
left = "01" and right = "1101", score = 1 + 3 = 4 
left = "011" and right = "101", score = 1 + 2 = 3 
left = "0111" and right = "01", score = 1 + 1 = 2 
left = "01110" and right = "1", score = 2 + 1 = 3


Solution: One pass
Step 1: In the first 2 lines of code, calculate the number of 0s in the left substring ("0") and the number of 1s in the right 
substring ("0010"). Thus, we start with zeros = 1 and ones = 1.
Step 2: Traverse only the highlighted part of the string "00010" and update the zeros, ones, and score variables as follows:

At index 1: left = "00" and right = "010", zeros = 2, ones = 1, score 2 + 1 = 3
At index 2: left = "000" and right = "10", zeros = 3, ones = 1, score 3 + 1 = 4
At index 3: left = "0001" and right = "0", zeros = 3, ones = 0, score 3 + 0 = 3
def solution(s):
	zeros = 1 if s[0] == '0' else 0
	ones = s.count('1', 1)  # count 1s in s[1:]
	score = zeros + ones
	for i in xrange(1, len(s) - 1):
		if s[i] == '0':
			zeros += 1
		else:
			ones -= 1
		score = max(zeros + ones,  score)
	return score
