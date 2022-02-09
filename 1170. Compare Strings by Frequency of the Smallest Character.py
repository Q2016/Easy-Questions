Question:
Let the function f(s) be the frequency of the lexicographically smallest character in a non-empty string s. For example, 
if s = "dcce" then f(s) = 2 because the lexicographically smallest character is 'c', which has a frequency of 2.
You are given an array of strings words and another array of query strings queries. For each query queries[i], count the number 
of words in words such that f(queries[i]) < f(W) for each W in words.
Return an integer array answer, where each answer[i] is the answer to the ith query.

Example 1:
Input: queries = ["cbd"], words = ["zaaaz"]
Output: [1]
Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").
  
Solution:
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        
        def f(string):
            c=sorted(string)[0]
            cnt=Counter(string)
            return cnt[c]
            
        res=[]
        for q in queries:
            for i,w in enumerate(words):
                
                if f(q)<f(w):
                    res.append(i)
        return res  
