// https://leetcode.com/problems/shuffle-the-array/

class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> shuffled_nums;
        for (int i = 0; i < n; i++) {
            shuffled_nums.push_back(nums[i]);
            shuffled_nums.push_back(nums[i + n]);
        }
        return shuffled_nums;
    }
};