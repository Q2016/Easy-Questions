Question:
Given an array of integers arr, replace each element with its rank.
The rank represents how large the element is. The rank has the following rules:
Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.
 
Example 1:
Input: arr = [40,10,20,30]
Output: [4,1,2,3]
Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.

 
 
Solution: Dic mapping (in a way educational)
 
Remove duplicates with set, then sort, then build a dict mapping values to ranks, then use that dict on the given list.

Time: O(n log n)
Space: O(n)

def arrayRankTransform(self, A):
    return map({a: i+1 for i, a in enumerate(sorted(set(A)))}.get, A)
