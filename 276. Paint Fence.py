Question:
There is a fence with n posts, each post can be painted with one of the k colors.
You have to paint all the posts such that no more than two adjacent fence posts have the same color.
Return the total number of ways you can paint the fence.

Sample I/O
Example 1
Input: n = 3, k = 2
Output: 6
Explanation: Take c1 as color 1, c2 as color 2. All possible ways are:

            post1  post2  post3      
 -----      -----  -----  -----       
   1         c1     c1     c2 
   2         c1     c2     c1 
   3         c1     c2     c2 
   4         c2     c1     c1  
   5         c2     c1     c2
   6         c2     c2     c1



Solution: DP

How do we go about solving this problem?
If we really think about it, this problem is closely related to counting.
Say we have just a single fence. In how many ways can we colour it with ‘k’ colours?
We can colour it in ‘k’ ways.
If we add another fence to it, how many combinations of coloring are possible now that we have two fences in the 
picture? The first fence can be coloured in ‘k’ ways as seen in the previous step. For the second fence, we can either 
paint it with the same colour as the first fence or we can choose a different colour for it. If we choose the same 
colour as the first fence, the total number of ways for painting the fences is = ‘k’ and if we choose a different 
colour from the first fence, the total number of ways of painting the fences = k * (k-1), where ‘k’ is the number 
of ways of painting the first fence, and (k-1) is the number of ways of painting the second fence (since we no longer 
pick the colour chosen for fence 1, it turns to (k-1) for the second fence). Thus, the total number of ways of 
painting the two fences with same and different colours = k (same) + k*(k-1) (different).
If we move on to 3 fences, the third fence can either be painted with the same colour as the second fence (provided 
the first fence is of a different colour) or it could be painted with a different color altogether. The number of ways 
for the third fence to be painted with the same colour as the second fence = different ways for painting fence 2 from 
fence 1, which = k * (k-1). The number of ways of painting the third fence with a different colour = total number of 
ways of fence 2 * (k-1) = (k + k*(k-1)) * (k-1).



class Solution:
  def numWays(self, n: int, k: int) -> int:
    if n == 0:
      return 0
    if n == 1:
      return k
    if n == 2:
      return k * k

    # dp[i] := # of ways to pan posts with k colors
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = k
    dp[2] = k * k

    for i in range(3, n + 1):
      dp[i] = (dp[i - 1] + dp[i - 2]) * (k - 1)

    return dp[n]


or:
            
public int numWays(int n, int k) {
        if(n == 0)
            return 0;
        if(n == 1)
            return k;
        int same = k;
        int diff = k * (k-1);
        for(int i = 3; i <= n; i++) {
            int same1 = diff;
            int diff2 = (same + diff) * (k-1);
            same = same1;
            diff = diff2;
        }
        return (same + diff);
    }            
