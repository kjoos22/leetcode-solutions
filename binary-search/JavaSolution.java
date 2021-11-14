// https://leetcode.com/problems/binary-search/

import java.lang.Math;

class Solution {
    public int search(int[] nums, int target) {
        if (nums[nums.length - 1] < target) {
            return -1;
        }
        
        int start = 0;
        int end = nums.length - 1;
        
        while (start <= end) {
            int mid = (int) Math.floor((start + end) / 2);
                
            if (nums[mid] == target) {
                return mid;
            }
            
            if (target < nums[mid]) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        return -1;
        
    }
}