Question:
Given a pattern and a string s, find if s follows the same pattern. Here follow means a full match, such that there is a bijection between a 
letter in pattern and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
  
Solution: Hashmap
At the first glance, the problem can be solved simply by using a hashmap w_to_p which maps words to letters from the pattern. But consider this example: w = ['dog', 'cat'] and p = 'aa'. In this case, the hashmap doesn't allow us to verify whether we can assign the letter a as a value to the key cat. This case can be handled by comparing length of the unique letters from the pattern and unique words from the string.

Space: O(n) - scan
Time: O(n) - for the hashmap

Runtime: 28 ms, faster than 85.44% of Python3 online submissions for Word Pattern.
Memory Usage: 14 MB, less than 94.65% of Python3 online submissions for Word Pattern.

def wordPattern(self, p: str, s: str) -> bool:
    words, w_to_p = s.split(' '), dict()

    if len(p) != len(words): return False
    if len(set(p)) != len(set(words)): return False # for the case w = ['dog', 'cat'] and p = 'aa'

    for i in range(len(words)):
        if words[i] not in w_to_p: 
            w_to_p[words[i]] = p[i]
        elif w_to_p[words[i]] != p[i]: 
            return False

    return True  
