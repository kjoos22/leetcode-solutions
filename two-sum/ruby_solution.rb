# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}

# https://leetcode.com/problems/two-sum/

def two_sum(nums, target)
    for i in 0..(nums.length()-1)
        for x in (i + 1)..(nums.length()-1)
            if nums[x] == target - nums[i]
                return [i, x]
            end
        end
    end
end