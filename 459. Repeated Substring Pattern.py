Question:
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

Example 1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

    
    
    
    
    
    
    
    
    
    
    
Solution: (is this correct?,if i want to find, then I can just see if it's in the string!)

        
Basic idea:

First char of input string is first char of repeated substring
Last char of input string is last char of repeated substring
Let S1 = S + S (where S in input string)
Remove 1 and last char of S1. Let this be S2
If S exists in S2 then return true else false
Let i be index in S2 where S starts then repeated substring length i + 1 and repeated substring S[0: i+1]

def repeatedSubstringPattern(self, str):

        if not str:
            return False
           
           
Related Question: Print all substrings of a given string: Two-Pointers

'''
* Function to print all (n * (n + 1)) / 2
* substrings of a given string s of length n.
'''
def printAllSubstrings(s, n):
 
    # Fix start index in outer loop.
    # Reveal new character in inner loop till end of string.
    # Print till-now-formed string.
    for i in range(n):
        temp=""
        for j in range(i,n):
            temp+=s[j]
            print(temp)
 
# Driver program to test above function
 
s = "Geeky"
printAllSubstrings(s, len(s))

Time complexity: O(n^2)
Auxiliary Space: O(n)

           
            
        ss = (str + str)[1:-1]
        return ss.find(str) != -1
