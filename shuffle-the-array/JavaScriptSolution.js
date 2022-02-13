/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */

// https://leetcode.com/problems/shuffle-the-array/

var shuffle = function(nums, n) {
    let shuffled_nums = []
    for (let i = 0; i < n; i++) {
        shuffled_nums.push(nums[i])
        shuffled_nums.push(nums[i + n])
    }
    return shuffled_nums    
};