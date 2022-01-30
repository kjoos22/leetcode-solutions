# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_0s = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count_0s] = nums[i]
                count_0s += 1
        while count_0s < len(nums):
            nums[count_0s] = 0
            count_0s += 1
        