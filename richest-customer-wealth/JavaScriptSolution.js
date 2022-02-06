/**
 * @param {number[][]} accounts
 * @return {number}
 */

// https://leetcode.com/problems/richest-customer-wealth/

var maximumWealth = function(accounts) {
    let maxWealth = 0;
    for (let i = 0; i < accounts.length; i++) {
        let wealth = accounts[i].reduce((a, b) => a + b)
        if (wealth > maxWealth) {
            maxWealth = wealth
        }        
    }
    return maxWealth
};