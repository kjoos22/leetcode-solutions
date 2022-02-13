# @param {Integer[]} nums
# @param {Integer} n
# @return {Integer[]}

# https://leetcode.com/problems/shuffle-the-array

def shuffle(nums, n)
    shuffled_nums = []
    for i in 0..(n-1)
        shuffled_nums.push(nums[i])
        shuffled_nums.push(nums[i+n])
    end
    return shuffled_nums
end