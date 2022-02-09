Question:
An integer x is a good if after rotating each digit individually by 180 degrees, we get a valid number that is different from x. 
Each digit must be rotated - we cannot choose to leave it alone. A number is valid if each digit remains a digit after rotation. For example:
0, 1, and 8 rotate to themselves, 2 and 5 rotate to each other (in this case they are rotated in a different direction, in other words, 2 or 5 gets mirrored),
6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.
Given an integer n, return the number of good integers in the range [1, n].

Example 1:
Input: n = 10
Output: 4
Explanation: There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

Solution:
class Solution:
    def rotatedDigits(self, n: int) -> int:
        m=0
        for i in range(n+1):
            string=str(i)
            tmp1=True
            tmp2=False
            for c in string:
                if c in ["0","1","8","2","5","6","9"]: 
                    tmp1=tmp1 and True
                    if c in ["2","5","6","9"]:
                        tmp2=True
                else:
                    tmp1=tmp1 and False     
            if tmp1 and tmp2:
                m+=1
        return m
