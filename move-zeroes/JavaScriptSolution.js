/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */

// https://leetcode.com/problems/move-zeroes/

var moveZeroes = function(nums) {
    let count_0s = 0
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] != 0) {
            nums[count_0s] = nums[i]
            count_0s += 1
        }
    }
    while (count_0s < nums.length) {
        nums[count_0s] = 0
        count_0s += 1
    }
};