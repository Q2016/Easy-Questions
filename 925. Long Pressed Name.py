Question:
Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will 
be typed 1 or more times. You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, 
with some characters (possibly none) being long pressed.

Example 1:
Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.

    

Solution: Two pointers (good question)

The idea is to iterate through the typed string, because it's longer, checking against a particular location in name as you go. There are only 
a couple of possibilities: There is a match (name[i] == typed[j]). In this case you want to increment both pointers.
There isn't a match and (given by else condition to case 1) there also isn't a match to the previous character in name (not name[i-1] == typed[j]), 
in which case it's clear the strings don't meet the condition.
Note you also have to be careful with the pointer i in to name, because it starts off not large enough to index name at i-1, and it can keep growing so 
long as there are matches. So ensure it's greater than zero before entering the second condition, and cap it at len(name) for the cases like 
['vtkgn', 'vttkgnn']: i ends up being 5 at the end there while j keeps running along the extra 'n's, so we fall in to the second condition and check 
name[i-1] against typed[j].
If we violate both conditions, we know the things don't match, so we can return False immediately. If we meet both conditions for the duration of typed, 
then we only have to make sure we've also gotten entirely through the name so we catch cases like ['pyplrz', 'ppyypllr'].

def isLongPressedName(self, name, typed):
    i = 0
    for j in range(len(typed)):
        if i < len(name) and name[i] == typed[j]:
            i += 1
        elif not i > 0 and name[i-1] == typed[j]:
            return False
    return i == len(name)
