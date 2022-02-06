# https://leetcode.com/problems/richest-customer-wealth/

class Solution:
    def maximumWealth(self, accounts) -> int:
        max_wealth = 0
        for account in accounts:
            wealth = sum(account)
            if wealth > max_wealth:
                max_wealth = wealth
        return max_wealth