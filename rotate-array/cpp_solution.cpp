// https://leetcode.com/problems/rotate-array/

class Solution {
public:
    void rotate(vector<int>& nums, int k) {            
        int n = nums.size();
        vector<int>ans(n);
        k = n - k % n;
        for(int i = 0; i < n; i++){
            ans[i] = nums[(i + k) % n];
        }
        nums = ans;
    }
};