// https://leetcode.com/problems/squares-of-a-sorted-array/

#include <iostream>
class Solution {   
public:
    vector<int> sortedSquares(vector<int>& nums) {
        for(int i = 0; i < nums.size(); i++) {
            nums[i] = nums[i] * nums[i];
        }
        std::sort(std::begin(nums), std::end(nums));
        return nums;
    }
};