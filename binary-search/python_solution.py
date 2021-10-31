#https://leetcode.com/problems/binary-search
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        import math
        
        if nums[-1] < target:
            return -1
        
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = math.trunc(math.floor((start + end) / 2))
            
            if nums[mid] == target:
                return mid
            
            if target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
                
        
        return -1