Question:
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] 
you have to count the number of valid j's such that j != i and nums[j] < nums[i]. Return the answer in an array.
Range of the given numbers is between 1 and 100.

Example 1:
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).







Solution: Dictionary+sort (I like both of the solutions)
    
Very similar to 1331

Record index in sorted nums if it didn't appear before.
Then just dump it's corresponding index in original nums.

Time: O(NlogN) #---> because we sort
Space: O(N) for output list


    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        indices = {}
        for i, num in enumerate(sorted(nums)):
            indices.setdefault(num, i) # Get the value of the "num" item, if the "num" item does not exist, insert "num" with the value "i":
        return [indices[num] for num in nums]

    
    

Soluiton 2
We are already told the range of the given numbers is between 1 and 100.
So we can easily count each number and sum their prefix and dump.

Time: O(N) # This solution is without sorting
Space: O(N) for output list


    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * 102
        for num in nums:
            count[num+1] += 1 # find frequency of each number
        for i in range(1, 102): # in a way sorting is indirectly implemented here
            count[i] += count[i-1] # by this way of counting, we accumulate numbers came before a given number
        return [count[num] for num in nums]
