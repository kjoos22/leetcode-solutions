// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int mostCandies = *max_element(candies.begin(), candies.end());
        vector<bool> haveMostCandies = {};
        for (int i = 0; i < candies.size(); i++) {
            if (candies[i] + extraCandies >= mostCandies) {
                haveMostCandies.push_back(true);
            } else {
                haveMostCandies.push_back(false);
            }
        }
        return haveMostCandies;
    }
};