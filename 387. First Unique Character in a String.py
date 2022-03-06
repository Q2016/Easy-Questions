Question:
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "loveleetcode"
Output: 2

    
    
    
    
    
    
    
    
    
    
    
Solution: Counter
The best possible solution here could be of a linear time because to ensure that the character is unique you have to check the whole string anyway.
The idea is to go through the string and save in a hash map the number of times each character appears in the string. That would take O(N) time, 
where N is a number of characters in the string. And then we go through the string the second time, this time we use the hash map as a reference 
to check if a character is unique or not. If the character is unique, one could just return its index. The complexity of the second iteration is O(N) as well.

    def firstUniqChar(self, s: str) -> int:
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1

    
Linear time solution: O(n)    
