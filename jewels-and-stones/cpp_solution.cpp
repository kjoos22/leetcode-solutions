// https://leetcode.com/problems/jewels-and-stones/

class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        int totalJewels = 0;
        
        for (int i = 0; i < stones.size(); i++) {
            for (int j = 0; j < jewels.size(); j++) {
                if (jewels[j] == stones [i]) {
                    totalJewels++;
                }
            }
        }
        return totalJewels;
    }
};