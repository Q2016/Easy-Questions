Question:
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

    
    
    
    
    
    
    
    
    
Solution: Dictionary

def singleNumber1(self, nums):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0)+1 #The get() method returns the value of the item with the specified key. 
                                        #"0" is a value to return if the specified key does not exist.
    for key, val in dic.items():
        if val == 1:
            return key

        
        
def singleNumber2(self, nums):
    res = 0
    for num in nums:
        res ^= num
    return res
    
def singleNumber3(self, nums):
    return 2*sum(set(nums))-sum(nums)
    
def singleNumber4(self, nums):
    return reduce(lambda x, y: x ^ y, nums)
    
def singleNumber(self, nums):
    return reduce(operator.xor, nums)
