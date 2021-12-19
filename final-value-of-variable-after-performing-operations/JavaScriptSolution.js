/**
 * @param {string[]} operations
 * @return {number}
 */

// https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

var finalValueAfterOperations = function(operations) {
    value = 0
    for (var i = 0; i < operations.length; i++){
        if (operations[i].includes("+")) {
            value += 1
        }else {
            value -= 1
        }                     
    }
    return value
};