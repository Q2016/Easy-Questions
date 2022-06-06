Question:
Given a string licensePlate and an array of strings words, find the shortest completing word in words.
A completing word is a word that contains all the letters in licensePlate. Ignore numbers and spaces in licensePlate, and treat letters 
as case insensitive. If a letter appears more than once in licensePlate, then it must appear in the word the same number of times or more.
For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice. Possible completing words are 
"abccdef", "caaacab", and "cbca". Return the shortest completing word in words. It is guaranteed an answer exists. If there are multiple shortest 
completing words, return the first one that occurs in words.

Example 1:
Input: licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]
Output: "steps"
Explanation: licensePlate contains letters 's', 'p', 's' (ignoring case), and 't'.
"step" contains 't' and 'p', but only contains 1 's'.
"steps" contains 't', 'p', and both 's' characters.
"stripe" is missing an 's'.
"stepple" is missing an 's'.
Since "steps" is the only word containing all the letters, that is the answer.











Solution:
class Solution:
    def shortestCompletingWord(self, lp, words):
        cntr_lp, res = {k: v for k, v in collections.Counter(lp.lower()).items() if k.isalpha()}, None
        for word in words:
            check = collections.Counter(word.lower())
            if all(k in check and v <= check[k] for k, v in cntr_lp.items()):
                if not res or len(word) < len(res): 
                    res = word
        return res
