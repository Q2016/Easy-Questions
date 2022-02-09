Qustion:
Winter is coming! During the contest, your first job is to design a standard heater with a fixed warm radius to warm all the houses.
Every house can be warmed, as long as the house is within the heater's warm radius range. 
Given the positions of houses and heaters on a horizontal line, return the minimum radius standard of heaters so that those heaters could cover all houses.
Notice that all the heaters follow your radius standard, and the warm radius will the same.

 

Example 1:

Input: houses = [1,2,3], heaters = [2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.


Solution:
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        
        def binary_search_recursive(array, element, start, end):
            if start > end:
                return -1

            mid = (start + end) // 2
            if element == array[mid]:
                return mid

            if element < array[mid]:
                return binary_search_recursive(array, element, start, mid-1)
            else:
                return binary_search_recursive(array, element, mid+1, end)
        
        
        for h in houses:
            binary_search_recursive(heaters, h, heaters[0], heaters[-1])
