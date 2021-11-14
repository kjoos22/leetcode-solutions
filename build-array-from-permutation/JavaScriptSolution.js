/**
 * @param {number[]} nums
 * @return {number[]}
 */

//https://leetcode.com/problems/build-array-from-permutation/

var buildArray = function(nums) {
    let ans = []
    
    for (let i = 0; i < nums.length; i++) {
        ans.push(nums[nums[i]])
    }
    
    return ans
};