Question:
Given two strings first and second, consider occurrences in some text of the form "first second third", where second comes 
immediately after first, and third comes immediately after second.
Return an array of all the words third for each occurrence of "first second third".

Example 1:
Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl","student"]

Solution: Split String

Split the text into words array, then loop through it to check if previous two words are first and second; If yes, add current word into list.

    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ans = []
        words = text.split(' ')
        for i in range(2, len(words)):
            if words[i - 2] == first and words[i - 1] == second:
                ans.append(words[i])
        return ans
Credit to @leihao1313 for the following clean code:

def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ans, words = [], text.split()
        for a, b, c in zip(words, words[1 :], words[2 :]):
            if (a, b) == (first, second):
                ans.append(c)
        return ans        

