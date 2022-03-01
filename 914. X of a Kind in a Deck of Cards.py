Question:
In a deck of cards, each card has an integer written on it.
Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:
Each group has exactly X cards.
All the cards in each group have the same integer.
 
Example 1:
Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].



Solution: gcd
Again, say there are C_i cards of number i. These must be broken down into piles of X cards each, ie. C_i % X == 0 for all i.
Thus, X must divide the greatest common divisor of C_i. If this greatest common divisor g is greater than 1, then X = g will satisfy. Otherwise, it won't.

class Solution(object):
    def hasGroupsSizeX(self, deck):
        from fractions import gcd
        vals = collections.Counter(deck).values()
        return reduce(gcd, vals) >= 2
