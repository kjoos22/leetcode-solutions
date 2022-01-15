# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for x in range((i + 1), len(nums) - 1):
                if nums[x] == target - nums[i]:
                    return [i, x]
                