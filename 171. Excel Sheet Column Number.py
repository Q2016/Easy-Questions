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
    
Going through the digits from right to left i.e first, second, third each must be multiplied by 26 similar to 10 based numbers that 123= 100*1+10*2+1*3

def titleToNumber(self, s):
    res = 0
    for c in s:
        res = res*26 + ord(c)-ord('A')+1
    return res  
