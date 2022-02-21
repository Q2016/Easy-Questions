Question:
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where 
it would be if it were inserted in order. You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2


Solution:

def searchInsert (nums, target):
    let lo = 0, hi = len(nums) # we might need to inseart at the end
    while(lo < hi): # breaks if lo == hi
        let mid = lo + floor((hi-lo)/2) # always gives the lower mid
        if (target > nums[mid]):
            lo = mid + 1 # no way mid is a valid option
        else:
            hi = mid # it might be possibe to inseart @ mid
    return lo;


Before We Begin
Have you ever wondered when to use while(lo<hi) while(lo <= hi) ?
Have you ever wondered when to use left = mid + 1 or left = mid, right = mid + 1 or right = mid ?
Have you ever wondered why your binary search algorithm stuck in an infinity loop?
Well, at least I did all that, and if you are like me this article is for you.


The Idea
Set lo and hi boundary, compute mid index. Compare target with mid , adjust lo & hi accordingly


Time Complexity
O(log n)

Basic Implementation (JavaScript)
var search = function(nums, target) {
	let lo = 0, hi = nums.length-1;
	while (lo < hi) {
		let mid = lo + Math.floor((hi-lo+1)/2);
		if (target < nums[mid]) {
			hi = mid - 1
		} else {
			lo = mid; 
		}
	}
	return nums[lo]==target?lo:-1;
};
Logic Flow of Solving Binary Search Problems
Choose lo & hi

Always double check what is the maximum range of possible values. For example, <LeetCode 35>, since it's possible to insert a value at 
the very end, the boundary for this problem is actually 0 - n.

Calculate mid
Always use the following, since it avoids overflow.

// when odd, return the only mid
// when even, return the lower mid
int mid = lo + ((hi - lo)/2);

// when odd, return the only mid
// when even, return the upper mid
int mid2 = lo + ((hi - lo + 1) / 2);
How to move lo and hi?
Always use a condition we are 100% sure of. It's always easier to eliminate options when we are 100% sure of something. For eample, 
if we are we are looking for target <= x, then for target>nums[mid] , we are 100% sure that our mid should never be considered. Thus we 
can type lo = mid + 1 with all the confidence.
        if (100% sure logic) {
        	left = mid + 1; // 100% sure target is to the right of mid
        } else {
        	right = mid; 
        }
        
        if (100% sure logic) {
        	right = mid - 1; // 100% sure target is to the left of mid
        } else {
        	left = mid;
        }
while Condition
Always use while (lo < hi) so when the loop breaks, we are 100% sure that lo == hi
If it's possible that target doesn't exist, extra check needs to be performed.
🔥Avoid Infinite loop
// ❌ The following code results in inifite loop
let mid = lo + ((hi - lo)/2); // aka the lower mid
// We should use:
// let mid = lo + ((hi - lo + 1)/2) // aka the upper mid

if (100% sure logic) {
	right = mid - 1
} else {
	left = mid // <-- note here
}
Consider when there's only 2 elements left, if the if condition goes to the else statement, since left = mid, our left boundary will not shrink, 
this code will loop for ever. Thus, we should use the upper mid.

// ❌ The following code results in inifite loop
let mid = lo + ((hi - lo + 1)/2); // aka the upper mid
// We should use:
// let mid = lo + ((hi - lo)/2) // aka the lower mid

if (100% sure logic) {
	left = mid - 1;
} else {
	right = mid // <-- note here
}
Consider when there's only 2 elements left, if the if condition goes to the else statement, since right = mid our right boundary will not shrink, 
this code will loop for ever. Thus, we should use the lower mid.

