/**
 * @param {number[]} nums
 * @return {number[]}
 */

//https://leetcode.com/problems/squares-of-a-sorted-array/

var sortedSquares = function(nums) {
    for(i = 0; i < nums.length; i++) {
        nums[i] = nums[i] * nums [i]
    }
    
    nums.sort((a, b) => a - b)
    
    return nums
};