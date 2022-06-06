Question:
For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address. So neglect '.' in the emails.
If you add a plus '+' in the local name, everything after the first plus sign will be ignored. 
Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that 
actually receive mails.

Example 1:
Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.
  
  
  
  
  
  
  
  
  
  
  
Solution:  
https://www.youtube.com/watch?v=TC_xLIWl7qY


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        unique=set()
        
        for e in emails:
            local, domain=e.split("@")
            local=local.split("+")[0]
            local=local.replace(".","")
            unique.add((local,domain))
            
        return len(unique)  

Time O(N.m) with m number of average length of each word, N number of words
