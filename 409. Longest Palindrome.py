Question:
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.






Solution: Greedy
  
A palindrome consists of letters with equal partners, plus possibly a unique center (without a partner). The letter i from the left 
has its partner i from the right. For example in 'abcba', 'aa' and 'bb' are partners, and 'c' is a unique center.
Imagine we built our palindrome. It consists of as many partnered letters as possible, plus a unique center if possible. This motivates a greedy approach.
For each letter, say it occurs v times. We know we have v // 2 * 2 letters that can be partnered for sure. For example, if we have 'aaaaa', 
then we could have 'aaaa' partnered, which is 5 // 2 * 2 = 4 letters partnered.
At the end, if there was any v % 2 == 1, then that letter could have been a unique center. Otherwise, every letter was partnered. To perform 
this check, we will check for v % 2 == 1 and ans % 2 == 0, the latter meaning we haven't yet added a unique center to the answer.
  

    def longestPalindrome(self, s):
        ans = 0
        for f in collections.Counter(s).itervalues(): # I use f for frequency
            ans += f // 2 * 2
            if ans % 2 == 0 and v % 2 == 1: # This condition means f was odd, so we add +1 because ans is always an even number
                ans += 1
        return ans  
      
      
      
or a simpler solution:

    def longestPalindrome(self, s):

        hash = set()
        for c in s:
            if c not in hash:
                hash.add(c)
            else:
                hash.remove(c)
        # len(hash) is the number of the odd letters
        return len(s) - len(hash) + 1 if len(hash) > 0 else len(s)  
