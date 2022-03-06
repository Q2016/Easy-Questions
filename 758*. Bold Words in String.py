Question:
Given a set of keywords words and a string S, make all appearances of all keywords in S bold. Any letters between <b> and </b> tags become bold.
The returned string should use the least number of tags possible, and of course the tags should form a valid combination.
For example, given that words = ["ab", "bc"] and S = "aabcd", we should return "a<b>abc</b>d". Note that returning "a<b>a<b>b</b>c</b>d" 
would use more tags, so it is incorrect.

Solution:
class Solution(object):
    def boldWords(self, words, S):

        N = len(S)
        bold = [0] * (N + 2)
        for word in words:
            start = 0
            while True:
                idx = S[start:].find(word)
                if idx < 0: break
                for x in range(start + idx, start + idx + len(word)):
                    bold[x + 1] = 1
                start += idx + 1
        S = list(S) + ['']
        ans = []
        for x in range(1, N + 1):
            if bold[x] == 1 and bold[x - 1] == 0:
                ans.append('<b>')
            ans.append(S[x - 1])
            if bold[x] == 1 and bold[x + 1] == 0:
                ans.append('</b>')
        return ''.join(ans)
