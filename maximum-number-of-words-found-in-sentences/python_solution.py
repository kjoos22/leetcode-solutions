# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences

class Solution:
    def mostWordsFound(self, sentences):
        max = 0
        for i in range(len(sentences)):
            spaces = sentences[i].count(" ")
            if spaces > max:
                max = spaces
        return max + 1