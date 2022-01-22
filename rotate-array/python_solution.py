# https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) > k:
            sl = slice((len(nums) - k), len(nums))
            rotate = nums[sl]
            del nums[sl]
            i = 1
            while i <= len(rotate):
                nums.insert(0, rotate[-i])
                i = i + 1
        elif len(nums) != 1:
            i = 0
            while i < k:
                rotate = nums[-1]
                del nums[-1]
                nums.insert(0, rotate)
                i = i + 1
            