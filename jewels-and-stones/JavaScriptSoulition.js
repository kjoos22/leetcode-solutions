/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */

// https://leetcode.com/problems/jewels-and-stones/

var numJewelsInStones = function(jewels, stones) {
    let totalJewels = 0
    
    let jewelsSet = new Set(jewels)
    for (let stone of stones) {
        if (jewelsSet.has(stone)) {
            totalJewels += 1
        }
    }
    
    return totalJewels
};