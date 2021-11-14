//https://leetcode.com/problems/search-insert-position/

class Solution {
    public int searchInsert(int[] nums, int target) {
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
        
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > target) {
                return i;
            }
            if (i == nums.length - 1) {
                return i + 1;
            }
        }
        //default return required
        return 0;
    }
}