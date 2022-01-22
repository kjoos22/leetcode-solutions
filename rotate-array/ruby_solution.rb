# @param {Integer[]} nums
# @param {Integer} k
# @return {Void} Do not return anything, modify nums in-place instead.

# https://leetcode.com/problems/rotate-array/

def rotate(nums, k)
    if nums.length() > k
        rotate = nums.slice!(-k, k) 
        i = 1
        while i <= rotate.length()
            nums.unshift(rotate[-i])
            i = i + 1
        end
    else
        i = 0
        while i < k
            nums.unshift(nums.slice!(- 1))
            i = i + 1
        end
    end
end