Question:
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product 
fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. 
You should minimize the number of calls to the API.

Example 1:
Given n = 5, and version = 4 is the first bad version.
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.


Solution: Educational for BS
https://leetcode.com/problems/first-bad-version/discuss/769685/Python-Clear-explanation-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems. 

class Solution:
    def firstBadVersion(self, n) -> int:
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left

    
https://leetcode.com/problems/first-bad-version/discuss/769685/Python-Clear-explanation-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems. 
    
69. Sqrt(x) [Easy]
35. Search Insert Position [Easy]
1011. Capacity To Ship Packages Within D Days [Medium]
410. Split Array Largest Sum [Hard]
875. Koko Eating Bananas [Medium]
1482. Minimum Number of Days to Make m Bouquets [Medium]
668. Kth Smallest Number in Multiplication Table [Hard]
719. Find K-th Smallest Pair Distance [Hard]
1201. Ugly Number III [Medium]
1283. Find the Smallest Divisor Given a Threshold [Medium]
