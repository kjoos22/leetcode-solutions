# https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled_nums = []
        for i in range(n):
            shuffled_nums.append(nums[i])
            shuffled_nums.append(nums[i + n])
        return shuffled_nums