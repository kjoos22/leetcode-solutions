//https://leetcode.com/problems/binary-search/

var search = function(nums, target) {
    if (nums[nums.length - 1] < target)
        return -1
    
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
    return -1
    
    
};