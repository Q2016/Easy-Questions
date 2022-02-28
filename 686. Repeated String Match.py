Question:
Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it. 

Example 1:
Input: a = "abcd", b = "cdabcdab"
Output: 3
Explanation: We return 3 because by repeating a three times "abcdabcdabcd", b is a substring of it.




Solution: One pass or Counter

    def repeatedStringMatch(self, A: str, B: str) -> int:
        temp = ""
        count = 0
        while len(temp) < len(B):
            temp+=A
            count += 1
            if B in temp:
                return count
        temp += A
        if B in temp:
            return count + 1
        return -1
