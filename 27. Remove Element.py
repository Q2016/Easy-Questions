Question:
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.
Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the 
array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k elements.
Return k after placing the final result in the first k slots of nums.
Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.


Solution: Two Pointers
Since this question is asking us to remove all elements of the given value in-place, we have to handle it with O(1) extra space. 
How to solve it? We can keep two pointers i and j, where i is the slow-runner while j is the fast-runner.
When nums[j] equals to the given value, skip this element by incrementing j. As long as nums[j] != val, we copy nums[j] to nums[i] 
and increment both indexes at the same time. Repeat the process until j reaches the end of the array and the new length is i.

    def removeElement(nums, val) :
        i = 0
        for j in range(len(nums)) :
            if (nums[j] != val) :
                nums[i] = nums[j]
                i+=1
        return i;

