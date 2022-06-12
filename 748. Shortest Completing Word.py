Question:
Given a licensePlate and an array of words, find the shortest completing word in words.
A completing word is a word that contains all the letters in licensePlate. 
Ignore numbers and spaces in licensePlate, and treat letters as case insensitive. 
If a letter appears more than once in licensePlate, then it must appear in the word the same number of times or more.

Example 1:
Input: licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]
Output: "steps"











Solution: Counter
    
class Solution:
    def shortestCompletingWord(self, lp, words):
        cntr_lp, res = {k: v for k, v in collections.Counter(lp.lower()).items() if k.isalpha()}, None
        for word in words:
            check = collections.Counter(word.lower())
            if all(k in check and v <= check[k] for k, v in cntr_lp.items()):
                if not res or len(word) < len(res): 
                    res = word
        return res
