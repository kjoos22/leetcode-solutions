/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */

//https://leetcode.com/problems/search-insert-position/
var searchInsert = function(nums, target) {
    let start = 0
    let end = nums.length - 1
    
    while (start <= end) {
        let mid = Math.floor((start + end) / 2)
        
        if (nums[mid] === target)
            return mid
        
        if (target < nums[mid]) {
            end = mid - 1
        } else {
            start = mid + 1
        }
    }
    
    for (i = 0; i <= nums.length-1; i++) {
        if (nums[i] > target)
            return i
        if (i == nums.length - 1)
            return i+1
    }
};