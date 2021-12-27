# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums):
        running_sum = 0
        running_sums = []
        for i in range(len(nums)):
            running_sum += nums[i]
            running_sums.append(running_sum)
            
        return running_sums