Question:
You are given an integer array prices where prices[i] is the price of a given stock on the ith day. On each day, you may decide to buy 
and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Solution: Greedy

For the figure
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/discuss/803206/PythonJSGoC%2B%2B-O(n)-by-DP-w-Visualization
	
                                    sell
             ________      <---------------------    ____
            |       |      |                     |  |    |
keep in Not hold     Not holding                Holding  keep in Holding position
            |_______|      |                     |  |____|
                           ---------------------->
                                     Buy
                                     
This link solves all Best Time to Buy Stocks using DP:
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/discuss/900051/Fully-explained-all-buy-and-sell-problems-C%2B%2B-oror-Recursive-oror-Memoization-oror-Minor-difference	


Below is the Greedy solution:

The profit is the sum of sub-profits. Each sub-profit is the difference between selling at day j, and buying at day i (with j > i). The range [i, j] 
should be chosen so that the sub-profit is maximum: sub-profit = prices[j] - prices[i]
We should choose j that prices[j] is as big as possible, and choose i that prices[i] is as small as possible (of course in their local range).
Let's say, we have a range [3, 2, 5], we will choose (2,5) instead of (3,5), because 2<3.
Now, if we add 8 into this range: [3, 2, 5, 8], we will choose (2, 8) instead of (2,5) because 8>5.
From this observation, from day X, the buying day will be the last continuous day that the price is smallest. Then, the selling day will be the 
last continuous day that the price is biggest. Take another range [3, 2, 5, 8, 1, 9], though 1 is the smallest, but 2 is chosen, because 2 is the 
smallest in a consecutive decreasing prices starting from 3. Similarly, 9 is the biggest, but 8 is chosen, because 8 is the biggest in a consecutive 
increasing prices starting from 2 (the buying price). Actually, the range [3, 2, 5, 8, 1, 9] will be splitted into 2 sub-ranges [3, 2, 5, 8] and [1, 9].
We come up with the following code:

	def maxProfit(prices) :
		i = 0, 
		buy, sell, profit = 0, N = len(prices) - 1
		while (i < N):
		    while (i < N and prices[i + 1] <= prices[i]) i++
		    buy = prices[i]
		    while (i < N and prices[i + 1] > prices[i]) i++
		    sell = prices[i]
		    profit += sell - buy
		return profit

