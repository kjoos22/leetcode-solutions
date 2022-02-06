// https://leetcode.com/problems/richest-customer-wealth/

class Solution {
    public int maximumWealth(int[][] accounts) {
        int max_wealth = 0;
        for (int i = 0; i < accounts.length; i++) {
            int wealth = Arrays.stream(accounts[i]).sum();
            if (wealth > max_wealth) {
                max_wealth = wealth;
            }
        }
        return max_wealth;
    }
}