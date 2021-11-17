# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums):
        i = 0
        while i < len(nums):
            nums[i] = nums[i] * nums[i]
            i += 1
        
        nums.sort()
        
        return nums