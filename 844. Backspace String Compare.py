Question:
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
  
Solution:

    def backspaceCompare(self, S, T):
        l1 = self.stack(S, [])
        l2 = self.stack(T, [])
        return l1 == l2
        
    
    def stack(self, S, stack):
        for char in S:
            if char is not "#":
                stack.append(char)
            else:
                if not stack:
                    continue
                stack.pop()
        return stack 
