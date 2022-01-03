/**
 * @param {string[]} sentences
 * @return {number}
 */

// https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

var mostWordsFound = function(sentences) {
    let max = 0
    for (let i = 0; i < sentences.length; i++) {
        let spaces = sentences[i].split(" ").length - 1;
        if (spaces > max) {
            max = spaces
        }
    }
    return max + 1
};