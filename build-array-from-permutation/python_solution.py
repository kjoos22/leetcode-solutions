# https://leetcode.com/problems/build-array-from-permutation/

class Solution:
    def buildArray(self, nums):
        ans = []
        x = 0
        
        while x < len(nums):
            ans.append(nums[nums[x]])
            x = x + 1
            
        return ans
        