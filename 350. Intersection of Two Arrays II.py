Question:
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many 
times as it shows in both arrays and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Solution: Two pointers:

class Solution(object):
    def intersect(self, nums1, nums2):

        nums1, nums2 = sorted(nums1), sorted(nums2)
        pt1 = pt2 = 0
        res = []

        while True:
            try:
                if nums1[pt1] > nums2[pt2]:
                    pt2 += 1
                elif nums1[pt1] < nums2[pt2]:
                    pt1 += 1
                else:
                    res.append(nums1[pt1])
                    pt1 += 1
                    pt2 += 1
            except IndexError:
                break

        return res
use dictionary to count:

class Solution(object):
    def intersect(self, nums1, nums2):

        counts = {}
        res = []

        for num in nums1:
            counts[num] = counts.get(num, 0) + 1

        for num in nums2:
            if num in counts and counts[num] > 0:
                res.append(num)
                counts[num] -= 1

        return res
use Counter to make it cleaner:

class Solution(object):
    def intersect(self, nums1, nums2):

        counts = collections.Counter(nums1)
        res = []

        for num in nums2:
            if counts[num] > 0:
                res += num,
                counts[num] -= 1

        return res