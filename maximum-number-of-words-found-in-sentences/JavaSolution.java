// https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

class Solution {
    public int mostWordsFound(String[] sentences) {
        int max = 0;
        for (int i = 0; i < sentences.length; i++) {
            int spaces = 0;
            for (int x = 0; x < sentences[i].length(); x++) {
                if (sentences[i].charAt(x) == ' ') {
                    spaces++;
                }
            }
            if (spaces > max) {
                max = spaces;
            }
        }
        return max + 1;
    }
}