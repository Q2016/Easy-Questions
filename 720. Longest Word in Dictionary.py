Question:
Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one 
character at a time by other words in words. If there is more than one possible answer, return the longest word with the 
smallest lexicographical order. If there is no answer, return the empty string.

Example 1:
Input: words = ["w","wo","wor","worl","world"]
Output: "world"
Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

    
    
    
    
    
    
    
    
    
    
    
    
    
Solution: Trie + Depth-First Search
    
Approach #1: Brute Force [Accepted]
Intuition

For each word, check if all prefixes word[:k] are present. We can use a Set structure to check this quickly.

Algorithm

Whenever our found word would be superior, we check if all it's prefixes are present, then replace our answer.

Alternatively, we could have sorted the words beforehand, so that we know the word we are considering would be the answer if all it's prefixes are present.

Python

class Solution(object):
    def longestWord(self, words):
    ans = ""
    wordset = set(words)
    for word in words:
        if len(word) > len(ans) or len(word) == len(ans) and word < ans:
            if all(word[:k] in wordset for k in xrange(1, len(word))):
                ans = word

    return ans




Complexity Analysis
Time complexity : O(\sum w_i^2) is the length of words[i]. 
Checking whether all prefixes of words[i] are in the set is O(\sum w_i^2).

Space complexity : O(\sum w_i^2) to create the substrings.
   



Trie + Depth-First Search


As prefixes of strings are involved, this is usually a natural fit for a trie (a prefix tree.)
Put every word in a trie, then depth-first-search from the start of the trie, only searching nodes that ended a word. Every node 
found (except the root, which is a special case) then represents a word with all it's prefixes present. We take the best such word.
In Python, we showcase a method using defaultdict, while in Java, we stick to a more general object-oriented approach.


class Solution(object):
    def longestWord(self, words):
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True

        for i, word in enumerate(words):
            reduce(dict.__getitem__, word, trie)[END] = i

        stack = trie.values()
        ans = ""
        while stack:
            cur = stack.pop()
            if END in cur:
                word = words[cur[END]]
                if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                    ans = word
                stack.extend([cur[letter] for letter in cur if letter != END])

        return ans
