Question:
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
Input: word1 = “coding”, word2 = “practice”
Output: 3


Solution:

Algorithm:
1. Declare index idx1(-1) and idx2(-1) to store current index that match word1 and word2
2. Declare minDiff(sys.max) to store minimum difference from idx1 and idx2
3. Update minDiff = min(minDiff, abs(idx1 - idx2))
4. Return minDiff
T: O(N + M)
S: O(1)


import sys
def shortestDistance(words, word1, word2):
    if words == None or word1 == None or word2 == None:
        return -1

    idx1 = -1
    idx2 = -1
    minDiff = sys.maxsize

    for i in range(len(words)):
        if words[i] == word1:
            idx1 = i

        if words[i] == word2:
            idx2 = i

        if idx1 != -1 and idx2 != -1:
            minDiff = min(minDiff, abs(idx1 - idx2))

    return 
