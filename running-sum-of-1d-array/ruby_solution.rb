# @param {Integer[]} nums
# @return {Integer[]}

# https://leetcode.com/problems/running-sum-of-1d-array/

def running_sum(nums)
    running_sum = 0
    running_sums = []
    for i in 0..(nums.length()-1)
        running_sum += nums[i]
        running_sums << running_sum
        i += 1
    end
    return running_sums
end