Question:
We can represent a sentence as an array of words, for example, the sentence "I am happy with leetcode" can be represented as 
arr = ["I","am",happy","with","leetcode"].
Given two sentences sentence1 and sentence2 each represented as a string array and given an array of string pairs similarPairs where 
similarPairs[i] = [xi, yi] indicates that the two words xi and yi are similar.
Return true if sentence1 and sentence2 are similar, or false if they are not similar.
Two sentences are similar if: They have the same length, sentence1[i] and sentence2[i] are similar.

Example 1:
Input: sentence1 = ["great","acting","skills"], sentence2 = ["fine","drama","talent"], similarPairs = [["great","fine"],["drama","acting"],["skills","talent"]]
Output: true
Explanation: The two sentences have the same length and each word i of sentence1 is also similar to the corresponding word in sentence2.


       
Solution:
First compare the length of two sentences. Then check if words in sequences are in pairs.
                                                                                                                                    
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        pairs_dict = defaultdict(set)
        for pair in similarPairs:
            pairs_dict[pair[0]].add(pair[1])
            pairs_dict[pair[1]].add(pair[0])
        for word1, word2 in zip(sentence1, sentence2):
            if word1 != word2 and word2 not in pairs_dict[word1]:           
                return False
            
        return True
          
       
                                                                                                                                    
Time Complexity: O(N).
Space Complexity: O(N).  
