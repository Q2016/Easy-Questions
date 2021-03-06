Question:
We are given a list nums of integers representing a list compressed with run-length encoding. Consider each adjacent pair of 
elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val concatenated 
in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.
Return the decompressed list.

Example 1:
Input: nums = [1,2,3,4]
Output: [2,4,4,4]
Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
At the end the concatenation [2] + [4,4,4] is [2,4,4,4].





Solution:

 def decompressRLElist(self, nums: List[int]) -> List[int]:
        return [nums[i + 1] for i in range(0, len(nums), 2) for _ in range(nums[i])]

  
  
which is equivalent to the following:

    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0, len(nums), 2):
            for _ in range(nums[i]):
                ans.append(nums[i + 1])
        return ans 

       
       
       
Analysis:
Time & space: O(nums[0] + nums[2] + ..,. + nums[2 n - 2]), where n = nums.length.
