# https://leetcode.com/problems/concatenation-of-array/

class Solution:
    def getConcatenation(self, nums):
        ans = []
        
        for num in nums:
            ans.append(num)
        for num in nums:
            ans.append(num)
        
        return ans