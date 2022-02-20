/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */

// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

var kidsWithCandies = function(candies, extraCandies) {
    mostCandies = Math.max(...candies)
    haveMostCandies = []
    for (let i = 0; i < candies.length; i++) {
        if (candies[i] + extraCandies >= mostCandies) {
            haveMostCandies.push(true)
        } else {
            haveMostCandies.push(false)
        }
    }
    return haveMostCandies
};