# @param {Integer[]} nums
# @return {Integer[]}

# https://leetcode.com/problems/squares-of-a-sorted-array/

def sorted_squares(nums)
    i = 0
    while i < nums.length
        nums[i] = nums[i] * nums[i]
        i += 1
    end
    
        
    return nums.sort
    
end