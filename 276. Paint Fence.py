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


def numWays(self, n: int, k: int) -> int:
    if n == 0:
      return 0
    if n == 1:
      return k
    if n == 2:
      return k * k

    # dp[i] := # Number of ways to paint 'i' number posts with k colors
    dp = [0] * (n + 1)
    dp[0] = 0 # There are zero number of ways to color 0 number of posts with k colors
    dp[1] = k # There are k number of ways to color 1 number of posts with k colors
    dp[2] = k*(k-1) # There are k*k number of ways to color 2 number of posts with k colors 
                  # but the question has a constraint here, so the solution is k*(k-1)

    for i in range(3, n + 1):
          dp[i] = (dp[i - 1] + dp[i - 2]) * (k - 1)  # this condition is similar to number of steps to take the ladder
                                                     # we can come up with it by dp[2]=(dp[1]+dp[0])*(k-1)

    return dp[n]
         
