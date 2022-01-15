// https://leetcode.com/problems/search-insert-position/

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int start = 0, end = nums.size() - 1;
        
        while (start <= end) {
            int mid = (start + end) / 2;
            
            if (nums[mid] == target) {
                return mid;
            }
            
            if (target < nums[mid]) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] > target) {
                return i;
            }
            if (i == nums.size() - 1) {
                return i + 1;
            }
        }
        //default return required
        return 0;
        
    }
};