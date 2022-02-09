Question:
Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.
For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 

Solution:
def titleToNumber(self, s):
    res = 0
    for c in s:
        res = res*26 + ord(c)-ord('A')+1
    return res  
