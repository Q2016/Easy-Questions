Question:
Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will 
be typed 1 or more times. You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, 
with some characters (possibly none) being long pressed.

Example 1:
Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.

    

Solution: Two pointers

    def isLongPressedName(self, name, typed):
        j = 0
        i = 0
        n = len(name)
        t = len(typed)
        
        while j < t:
            if i < n and name[i] == typed[j]:
                i +=1
            elif j == 0 or typed[j] != typed[j-1]:
                return False
            j +=1
        return i == n
