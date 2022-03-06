Question:
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
If the town judge exists, then:
The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.
Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

Example 1:
Input: n = 2, trust = [[1,2]]
Output: 2

Solution:
Given constraints are
1. The judge believes no one.
2. Everybody believes judge.
so, from these two points, we can say that if any person is trusted by N - 1 persons 
and the same person believes no one, then we can say that he is a judge.

Now, let's do this in program.
1. Create an array of Size N + 1 to represent each person.
   arr[i] represents trust score of i th person
   and arr[i] = number of persons trusts him - number of 
   persons he trusts.
2. Now, traverse through given array. 
    a, b = a trusts b.
    if a person trusts others,
	then decrease his score by 1. i.e, arr[a]--
    if a person is trusted by others, 
    then increase his score by 1. i.e, arr[b]++
3. At last traverse through each person,
    if anyone found with N - 1 trusts,
	then return his index.
4. if not found, return -1

IF YOU HAVE ANY DOUBTS, FEEL FREE TO ASK
IF YOU UNDERSTAND, DON'T FORGET TO UPVOTE.
   
time:- O(N)
space:- O(N)

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trusts = [0] * (N+1)
        for (a, b) in trust:
            trusts[a] -= 1
            trusts[b] += 1
            
        for i in range(1, len(trusts)):
            if trusts[i] == N-1:
                return i
        return -1
