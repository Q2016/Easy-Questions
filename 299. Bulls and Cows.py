Question:
You are playing the Bulls and Cows game with your friend.
You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:
The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. 
Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.
The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and 
guess may contain duplicate digits.

Example 1:
Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"7810"

Solution:
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        secret=list(secret)
        guess=list(guess)
        
        bulls=0
        n=0 # index of array
        for i,j in zip(secret, guess):
            if i==j:
                bulls+=1
                secret.pop(n)
                guess.pop(n)
            
            n+=1
            
        cnt_s=Counter(secret)
        cnt_g=Counter(guess)
        
        myset1=set()
        for i,_ in cnt_s.items(): 
            myset1.add(i)
                
        myset2=set()
        for i,_ in cnt_g.items(): 
            myset2.add(i)
            
        m=len(myset1.intersection(myset2))
        
        return str(bulls)+"A"+str(m)+"B"
