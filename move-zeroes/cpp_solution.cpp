// https://leetcode.com/problems/move-zeroes/

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int count_0s = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != 0) {
                nums[count_0s] = nums[i];
                count_0s++;
            }
        }
        while (count_0s < nums.size()) {
            nums[count_0s] = 0;
            count_0s++;
        }
    }
};