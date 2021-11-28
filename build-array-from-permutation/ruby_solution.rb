# @param {Integer[]} nums
# @return {Integer[]}

# https://leetcode.com/problems/build-array-from-permutation

def build_array(nums)
    ans = []
    x = 0
    
    while x < nums.length()
        ans.push(nums[nums[x]])
        x = x + 1
    end
    
    return ans
end