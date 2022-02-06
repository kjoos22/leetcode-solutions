// https://leetcode.com/problems/richest-customer-wealth/

class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int max_wealth = 0;
        for (int i = 0; i < accounts.size(); i++) {
            int wealth = accumulate(accounts[i].begin(), accounts[i].end(), 0);
            if (wealth > max_wealth) {
                max_wealth = wealth;
            }
        }
        return max_wealth;
    }
};