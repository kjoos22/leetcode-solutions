/**
 * @param {number[]} nums
 * @return {number[]}
 */

//https://leetcode.com/problems/running-sum-of-1d-array/

var runningSum = function(nums) {
    let running_sum = 0
    let running_sums = []
    for (let i = 0; i < nums.length; i++) {
        running_sum += nums[i]
        running_sums.push(running_sum)
    }
    return running_sums
};