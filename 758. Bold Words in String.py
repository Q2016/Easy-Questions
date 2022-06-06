Question:
Given a set of keywords words and a string S, make all appearances of all keywords in S bold. Any letters between <b> and </b> tags become bold.
The returned string should use the least number of tags possible, and of course the tags should form a valid combination.

For example, given that words = ["ab", "bc"] and S = "aabcd", we should return "a<b>abc</b>d". Note that returning "a<b>a<b>b</b>c</b>d" 
would use more tags, so it is incorrect.














Solution:
    
https://www.youtube.com/watch?v=4JPKLcpggCE    
    
    
class Solution(object):
    def boldWords(self, words, S):

        n=len(s)
        flag=[0]*n
        cur_end=0
        
        for i in range(n):
            for w in dict:
                if s.startswith(w,i):
                    cur_end=max(cur_end, i+len(w))
                    
            flag[i]=i<cur_end
            
        ans=None
        
        for i in range(n):
            if flag[i]:
                if i==0 or (i>0 and not flag[i-1]):
                    ans+='<b>'
                    
                ans +=s[i]
                
                if i==n-1 or (i<n-1 and not flag[i+1]):
                    ans +='</b>'
                    
        return ans
