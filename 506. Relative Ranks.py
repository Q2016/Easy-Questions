Question:
You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are 
guaranteed to be unique. The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd 
place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:
The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.

Example 1:
Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].

Solution:

Create a mapping of scores to sorted order indices

class Solution(object):
    def findRelativeRanks(self, nums):

        s = {n: i for i, n in enumerate(sorted(nums, reverse=True))}
        medals = ['Gold', 'Silver', 'Bronze']
        return [str(s[n]+1) if s[n] >= len(medals) else (medals[s[n]] + ' Medal') for n in nums]
