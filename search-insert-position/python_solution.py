# https://leetcode.com/problems/search-insert-position/

import math

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        last = len(nums) - 1
        
        while start <= last:
            mid = math.trunc(math.floor((start + last) / 2))
            
            if nums[mid] == target:
                return mid
            
            if target < nums[mid]:
                last = mid - 1
            else:
                start = mid + 1
        
        for i in nums:
            if i > target:
                return nums.index(i)
            if nums.index(i) == len(nums) - 1:
                return nums.index(i) + 1
        