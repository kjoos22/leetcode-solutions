# @param {Integer[][]} accounts
# @return {Integer}
# https://leetcode.com/problems/richest-customer-wealth/

def maximum_wealth(accounts)
    max_wealth = 0
    for account in accounts
        wealth = account.sum
        if wealth > max_wealth
            max_wealth = wealth
        end
    end
    return max_wealth
end