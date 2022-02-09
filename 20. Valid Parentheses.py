Question:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 
Example 1:
Input: s = "()[]{}"
Output: true

Solution:
class Solution:
    def isValid(self, s: str) -> bool:
        
        st=[]
        n=0
        for c in s:
            print(c)
            if (c=='('or c=='{' or c=='['):
                st.append(c)
                n+=1
            else:
                if st==[] : return False
                if c==')' and st[-1] !='(': return False
                if c=='}' and st[-1] !='{': return False
                if c==']' and st[-1] !='[': return False
                st.pop()
                n-=1
        
        if n==0: 
            return True
        else:
            return False
