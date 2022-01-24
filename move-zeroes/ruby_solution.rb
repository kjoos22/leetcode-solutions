# @param {Integer[]} nums
# @return {Void} Do not return anything, modify nums in-place instead.

# https://leetcode.com/problems/move-zeroes/

def move_zeroes(nums)
    count_0s = 0
    for i in 0..(nums.length-1)
        if nums[i] != 0
            nums[count_0s] = nums[i] 
            count_0s += 1
        end
    end
    while count_0s < nums.length
        nums[count_0s] = 0
        count_0s += 1
    end
end