Question:
Given two lists Aand B, and B is an anagram of A. B is an anagram of A means B is made by randomizing the order of the elements in A.
We want to find an index mapping P, from A to B. A mapping P[i] = j means the ith element in A appears in B at index j.
These lists A and B may contain duplicates. If there are multiple answers, output any of them.
For example, given
A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]
We should return
[1, 4, 3, 2, 0]
as P[0] = 1 because the 0th element of A appears at B[1], and P[1] = 4 because the 1st element of A appears at B[4], and so on.



Solution:
Find A’s numbers’ indices in B.

class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        results = []
        
        for number in A:
            results.append(B.index(number))
        
        return results
        
        
        
Time Complexity: O(N)
Space Complexity: O(N)
